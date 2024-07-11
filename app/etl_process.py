import json
from datetime import datetime
from postgres_connection import PostgresConnection
from sqs_utility import SQSUtility
import wrangling_utility

class ETLProcess:
    def __init__(self):
        # Initialize PostgreSQL connection and SQS utility
        self.pg_conn = PostgresConnection()
        self.sqs = SQSUtility()

    def extract_data(self):
        # Extract messages from the SQS queue
        messages = self.sqs.read_queue()
        if not messages:
            print("No messages to process, queue is empty")
        return messages

    def transform_data(self, messages):
        # Transform the extracted messages
        transformed_messages = []
        for message in messages:
            try:
                # Extract necessary fields from the message
                ip = message["ip"]
                device_id = message["device_id"]
                app_version = message["app_version"]
            except (json.JSONDecodeError, KeyError) as e:
                # Handle missing or invalid data
                print(f"key missing for a massage: {str(e)}")
                continue
            # Encode IP and device ID, convert app version to integer
            message["ip"] = wrangling_utility.mask_ip(ip)
            message["device_id"] = wrangling_utility.mask_device(device_id)
            message["app_version"] = wrangling_utility.ver_to_int(app_version)
            # Add current date to the message
            message["create_date"] = datetime.now().strftime("%Y-%m-%d")
            transformed_messages.append(message)
        return transformed_messages

    def load_data(self, transformed_data):
        # Load the transformed data into PostgreSQL
        self.pg_conn.load_data_to_postgres(transformed_data)

    def show_loaded_data(self, limit):
        # Retrieve and print the loaded data from PostgreSQL un-masking for easy read
        rows = self.pg_conn.print_user_logins_table(limit)
        print('\nPrinting TABLE: user_logins\n')
        print('\n un-masking ip and device id for viewing\n')
        print('user_id | device_type | masked_ip | masked_device_id | locale | app_version | create_date')
        for row in rows:
            row = list(row)
            # Unmask ip for easy read
            row[2] = wrangling_utility.unmask_ip(row[2])
            # Unmask ip for easy read
            row[3] = wrangling_utility.unmask_device(row[3])
            # Convert app version back to version format
            row[-2] = wrangling_utility.int_to_ver(row[-2])
            print(', '.join(map(str, row)))

def main():
    """The main function to execute the ETL process"""
    # Create an instance of ETLProcess
    etl_process = ETLProcess()
    # Extract data from SQS
    print("----Extracting data from SQS----")
    messages = etl_process.extract_data()
    # Transform the extracted data
    print("----Transforming the extracted data----")
    transformed_data = etl_process.transform_data(messages)
    # Load the transformed data into PostgreSQL
    print("----Loading the transformed data into PostgreSQL----")
    etl_process.load_data(transformed_data)
    # Show the loaded data from PostgreSQL
    print("----Showing the sample data from PostgreSQL----")
    etl_process.show_loaded_data(10)

if __name__ == "__main__":
    main()
