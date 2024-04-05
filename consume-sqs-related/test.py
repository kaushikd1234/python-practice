import boto3

# Initialize SQS client
sqs = boto3.client('sqs', region_name='us-east-1')  # Change the region as per your SQS queue's region

def consume_from_sqs():
    # Replace 'your_queue_url' with the URL of your SQS queue
    queue_url = 'https://sqs.us-east-1.amazonaws.com/891377293198/test-cli-sqs'

    # Retrieve messages from the SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=10  # Adjust this value based on your requirements
    )

    # Process received messages
    messages = response.get('Messages', [])
    for message in messages:
        # Print message body
        print("Received message:", message['Body'])

        # Delete the message from the queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=message['ReceiptHandle']
        )

if __name__ == "__main__":
    consume_from_sqs()

