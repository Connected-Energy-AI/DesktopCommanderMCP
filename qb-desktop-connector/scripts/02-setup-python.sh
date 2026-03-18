#!/bin/bash
# Setup Python QBWC Connector
# For Talian Technologies - Oil & Gas Operations

set -e

echo "=== Setting up QBWC Python Connector ==="

cd "$(dirname "$0")/../python-connector"

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate and install dependencies
source venv/bin/activate
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

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
echo "2. Activate venv: source venv/bin/activate"
echo "3. Run: python server.py"
echo ""
