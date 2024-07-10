#!/bin/bash

# Step 0: Start Docker services using Docker Compose
docker-compose up -d

# Step 1: Create virtual environment
python3 -m venv fetch_env

# Step 2: Activate virtual environment
source fetch_env/bin/activate

# Step 3: Upgrade pip
fetch_env/bin/pip3 install --upgrade pip

# Step 4: Install requirements
fetch_env/bin/pip3 install -r requirements.txt --no-cache-dir

# Step 5: Run the Python script
fetch_env/bin/python3 app/etl_process.py
