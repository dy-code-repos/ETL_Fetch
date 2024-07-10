import sys
import psycopg2
import configparser

class PostgresConnection:
    def __init__(self):
        # Read configuration from the 'config.ini' file
        config = configparser.ConfigParser()
        config.read("config.ini")

        # Load PostgreSQL configuration parameters
        self.username = config.get("postgres", "username")
        self.password = config.get("postgres", "password")
        self.host = config.get("postgres", "host")
        self.port = config.getint("postgres", "port")
        self.database = config.get("postgres", "database")
        self.table = config.get("postgres", "table")

        try:
            # Establish a connection to the PostgreSQL database
            self.connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.username,
                password=self.password,
            )
        except Exception as e:
            # Print the error and exit if there is an issue connecting to the database
            print(f"Error connecting to PostgreSQL: {str(e)}")
            sys.exit(1)

    def load_data_to_postgres(self, message_list):
        """Function to load data to PostgreSQL"""

        if not message_list:
            print("Error: No transformed messages to load")

        # Define the SQL INSERT query with the table name parameterized
        insert_query = f"""
                        INSERT INTO {self.table} (
                            user_id, 
                            app_version, 
                            device_type, 
                            masked_ip, 
                            locale, 
                            masked_device_id, 
                            create_date
                            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """

        for message in message_list:
            # Convert the message values to a list
            values = list(message.values())
            cursor = self.connection.cursor()
            try:
                # Execute the INSERT query with the values
                cursor.execute(insert_query, values)
                # Commit the transaction
                self.connection.commit()
            except Exception as e:
                # Print the error and rollback if there is an issue inserting data
                print(f"Error inserting data: {str(e)}")
                self.connection.rollback()

    def print_user_logins_table(self, limit):
        """Print the contents of the user_logins table after insertion of flattened JSON data"""
        cursor = self.connection.cursor()
        rows = []
        try:
            # Define the SQL SELECT query to fetch rows from the user_logins table with a limit
            select_query = f"SELECT * FROM user_logins limit {limit};"
            cursor.execute(select_query)
            # Fetch all rows from the result
            rows = cursor.fetchall()
        except Exception as e:
            # Print the error if there is an issue reading from the database
            print(f"Error reading from PostgreSQL: {str(e)}")
        return rows
