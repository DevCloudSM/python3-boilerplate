#!/bin/bash 

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment"
    python3 -m venv .venv
    # Activate the virtual environment
    source .venv/bin/activate

    # Install the requirements
    pip install -r requirements.txt
fi

source .venv/bin/activate

cd app && gunicorn --bind 0.0.0.0:3000 app:start