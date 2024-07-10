import os
import sys
import boto3 
import json
import configparser

 
class SQSUtility:

    def __init__(self):
        # Read configuration from the 'config.ini' file
        config = configparser.ConfigParser()
        thisfolder = os.path.dirname(os.path.abspath(__file__))
        initfile = os.path.join(thisfolder, 'config.ini')
        config.read(initfile)

        # Load SQS configuration parameters
        self.endpoint_url = config.get('SQS', 'endpoint_url')
        self.queue_name = config.get('SQS', 'queue_name')
        self.wait_time = config.getint('SQS', 'wait_time')
        self.max_messages = config.getint('SQS', 'max_messages')
        self.queue_url = self.endpoint_url + "/" + self.queue_name

        # Initialize SQS client
        self.sqs_client = boto3.client("sqs", 
                                       region_name="us-east-1", 
                                       endpoint_url=self.endpoint_url)
        
    def get_messages(self):
        """
        Receive messages from the SQS queue.
        Returns a list of messages.
        """
        try:
            response = self.sqs_client.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=self.max_messages,
                WaitTimeSeconds=self.wait_time
            )
            # Return the list of messages or an empty list if no messages are received
            return response.get('Messages', [])
        except Exception as e:
            # Print the error and exit if there is an issue receiving messages
            print(f"Error receiving messages: {str(e)}")
            sys.exit(1)
    
    def delete_message(self, receipt_handle):
        """
        Delete a message from the SQS queue.
        """
        try:
            self.sqs_client.delete_message(
                    QueueUrl=self.queue_url,
                    ReceiptHandle=receipt_handle
                    )
        except Exception as e:
            # Print the error and exit if there is an issue deleting messages
            print(f"Error in deleting messages: {str(e)}")
            sys.exit(1)
    
    def read_queue(self):
        """
        Read all messages from the queue, process them, and delete them from the queue.
        Returns a list of processed message bodies.
        """
        sqs_data = []
        messages = self.get_messages()
        # Continue processing messages until there are no more messages in the queue
        while len(messages) > 0:
            for message in messages:
                # Load the message body as JSON and append it to the list
                message_body = json.loads(message['Body'])
                sqs_data.append(message_body)
                # Delete the message from the queue
                self.delete_message(message["ReceiptHandle"])
            # Get the next batch of messages
            messages = self.get_messages()
        return sqs_data
