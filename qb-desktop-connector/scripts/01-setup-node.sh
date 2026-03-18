#!/bin/bash
# Setup Node.js QBWC Connector
# For Talian Technologies - Oil & Gas Operations

set -e

echo "=== Setting up QBWC Node.js Connector ==="

cd "$(dirname "$0")/../node-connector"

# Install dependencies
echo "Installing npm dependencies..."
npm install

# Copy .env from example if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env with your credentials before running"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env with your credentials"
echo "2. Run: npm start"
echo "3. Test with: npm test"
echo ""
