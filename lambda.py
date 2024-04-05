import boto3

def lambda_handler(event, context):
    # Initialize SQS client
    sqs = boto3.client('sqs')
    
    # URL of your SQS queue
    queue_url = 'https://sqs.us-east-1.amazonaws.com/891377293198/test-sqs'
    
    # Receive messages from SQS
    response = sqs.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,  # Maximum number of messages to retrieve
        VisibilityTimeout=30,    # Visibility timeout for the message in seconds
        WaitTimeSeconds=20       # Wait time for long polling in seconds
    )
    
    messages = response.get('Messages', [])
    if messages:
        for message in messages:
            # Process the message
            message_body = message['Body']
            print("Received message:", message_body)
            
            # Delete the message from the queue
            receipt_handle = message['ReceiptHandle']
            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=receipt_handle
            )
            print("Message deleted from the queue.")
    else:
        print("No messages in the queue.")
    
    return {
        'statusCode': 200,
        'body': 'Processed messages from SQS successfully!'
    }
