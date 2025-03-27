#!/bin/bash

# Exit on any error
set -e

# Print commands for debugging
set -x

# Set Python version (Render’s on 3.13 now)
PYTHON="python3.13"
if ! command -v $PYTHON &> /dev/null; then
    PYTHON="python3"
fi

# Activate virtualenv (Render handles this, but for local)
if [ ! -d ".venv" ]; then
    $PYTHON -m venv .venv
fi
source env/bin/activate

# Install dependencies
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt

# Run migrations
$PYTHON manage.py migrate

# Collect static files
$PYTHON manage.py collectstatic --noinput

# Deactivate virtualenv
deactivate

echo "Build complete!"