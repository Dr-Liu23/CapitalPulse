#!/bin/bash
# Start the backend FastAPI server
cd "$(dirname "$0")"

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

echo "Starting backend on port 8100..."
python -m uvicorn main:app --host 0.0.0.0 --port 8100 --log-level info
