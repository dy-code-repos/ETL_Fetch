!/bin/bash


# Step 1: Create virtual environment
echo "Creating virtual Env"
python3 -m venv fetch_env

# Step 2: Activate virtual environment
source fetch_env/bin/activate

# Step 3: Upgrade pip
echo "Installing Requirements Env"
fetch_env/bin/pip3 install --upgrade pip

# Step 4: Install requirements
fetch_env/bin/pip3 install -r requirements.txt --no-cache-dir

# Step 5: Run the Python script
echo "=============Running the ETL process=============="
fetch_env/bin/python3 app/etl_process.py
