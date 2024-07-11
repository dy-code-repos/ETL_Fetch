# Makefile for setting up and running the ETL process

.PHONY: all setup run clean

# Step to set up the virtual environment, start Docker, and install dependencies
setup:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	@echo "Activating virtual environment and installing requirements..."
	. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

# Step to run the ETL process
run:
	@echo "Running the ETL process..."
	. venv/bin/activate && python app/etl_process.py

# Step to clean the project directory by removing the virtual environment and stopping Docker
clean:
	@echo "Cleaning up..."
	rm -rf venv
	rm -rf app/__pycache__
	
# Default target
all: setup run
