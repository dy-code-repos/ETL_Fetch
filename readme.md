
# ETL Process with SQS and PostgreSQL

This project demonstrates an ETL (Extract, Transform, Load) process using AWS SQS for message queuing and PostgreSQL for data storage. The messages are extracted from SQS, transformed, and then loaded into a PostgreSQL database.

## Prerequisites
- Python 3
- Git
- Docker

## Steps to Run

### Step 1: Clone the Repository

   ```sh
   git clone https://github.com/dy-code-repos/ETL_Fetch.git
   cd ETL_Fetch
   ```

### Step 2: Run Docker for PostgreSQL and LocalStack
Ensure Docker is running on your computer, then run the following command:

   ```sh
   docker compose up
   ```

   Once PostgreSQL and LocalStack are fully running, proceed to Step 3.

### Step 3: Set Up the Virtual Environment

#### Automatic Setup (Linux/Mac)
You can run `Setup.sh` to set up and run the project automatically:

   ```sh
   bash Setup.sh
   ```

#### Manual Setup

1. **Create a virtual environment**

   ```sh
   python3 -m venv fetch_env
   ```

2. **Activate the virtual environment**

   - On Windows:
     ```sh
     fetch_env\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source fetch_env/bin/activate
     ```

3. **Upgrade pip**

   ```sh
   pip install --upgrade pip
   ```

4. **Install requirements**

   ```sh
   pip install -r requirements.txt --no-cache-dir
   ```

5. **Run the Python script**

   ```sh
   python app/etl_process.py
   ```
