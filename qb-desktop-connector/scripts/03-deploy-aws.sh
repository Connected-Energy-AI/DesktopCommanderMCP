#!/bin/bash
# Deploy QBWC Connector to AWS (us-east-1)
# For Talian Technologies - Oil & Gas Operations
#
# Prerequisites:
# - AWS CLI configured with us-east-1 region
# - Docker installed
# - Domain name with Route53 hosted zone

set -e

REGION="us-east-1"
ECR_REPO="qbwc-connector"
ECR_DOMAIN="${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
IMAGE_TAG="latest"

echo "=== Deploying QBWC Connector to AWS us-east-1 ==="
echo ""

# Get AWS account ID
if [ -z "$AWS_ACCOUNT_ID" ]; then
    AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
    echo "Detected AWS Account ID: $AWS_ACCOUNT_ID"
fi

# 1. Create ECR repository
echo "1. Creating ECR repository..."
aws ecr create-repository \
    --repository-name $ECR_REPO \
    --region $REGION \
    --image-scanning-configuration scanOnPush=true \
    2>/dev/null || echo "   Repository already exists"

# 2. Login to ECR
echo "2. Logging into ECR..."
aws ecr get-login-password --region $REGION | \
    docker login --username AWS --password-stdin $ECR_DOMAIN

# 3. Build Docker image
echo "3. Building Docker image..."
cd "$(dirname "$0")/../node-connector"
docker build -t $ECR_DOMAIN/$ECR_REPO:$IMAGE_TAG .

# 4. Push to ECR
echo "4. Pushing image to ECR..."
docker push $ECR_DOMAIN/$ECR_REPO:$IMAGE_TAG

# 5. Create ACM certificate (if domain provided)
if [ -n "$DOMAIN_NAME" ]; then
    echo "5. Requesting ACM certificate for $DOMAIN_NAME..."
    aws acm request-certificate \
        --domain-name $DOMAIN_NAME \
        --validation-method DNS \
        --region $REGION \
        2>/dev/null || echo "   Certificate already exists or validation pending"
fi

# 6. Create SSM parameters for secrets
echo "6. Creating SSM parameters..."
aws ssm put-parameter \
    --name "/qbwc/username" \
    --value "${QBWC_USERNAME:-qbwc_user}" \
    --type SecureString \
    --region $REGION \
    --overwrite

aws ssm put-parameter \
    --name "/qbwc/password" \
    --value "${QBWC_PASSWORD:-change_me}" \
    --type SecureString \
    --region $REGION \
    --overwrite

# 7. Create ECS task definition
echo "7. Creating ECS task definition..."
aws ecs register-task-definition \
    --cli-input-json file://../../aws/task-definition.json \
    --region $REGION \
    2>/dev/null || echo "   Update task-definition.json with your ECR URI first"

echo ""
echo "✅ Deployment preparation complete!"
echo ""
echo "Next steps:"
echo "1. Update aws/task-definition.json with your ECR URI: $ECR_DOMAIN/$ECR_REPO:$IMAGE_TAG"
echo "2. Create ECS cluster: aws ecs create-cluster --cluster-name qbwc-cluster --region $REGION"
echo "3. Create ALB and target group"
echo "4. Create ECS service"
echo ""
echo "Or use AWS Console: ECS > Clusters > Create Service"
echo ""
