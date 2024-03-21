#!/bin/bash 

# cd ..

# Check if venv exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment"
    python3 -m venv .venv
    # Activate the virtual environment
    source .venv/bin/activate

    # Install the requirements
    pip3 install -r requirements.txt
fi

mkdir -p ./dev_env/data
mkdir -p ./dev_env/shared

source .venv/bin/activate

cd app && PYTHONUNBUFFERED=TRUE DEBUG=TRUE gunicorn --reload --bind 0.0.0.0:3000 app:start