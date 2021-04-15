import boto3
import json

#Boto3 is used to directly interact with AWS resource from python script
sqs_client = boto3.client("sqs", aws_access_key_id =" " , aws_secret_access_key =" " , region_name="us-west-2")

#To create the new sqs queue. 
def create_queue(queuename):
    response = sqs_client.create_queue(
        QueueName=queuename,
        Attributes={
            "DelaySeconds": "0",
            "VisibilityTimeout": "60",  # 60 seconds
        }
    )
    #print(response)

#To get queue url 
def get_queue_url(queuename):
    response = sqs_client.get_queue_url(
        QueueName=queuename,
    )
    #print(response["QueueUrl"])
    return response["QueueUrl"]

#To sent the Message
def send_message(queueurl,message):
    response = sqs_client.send_message(
        QueueUrl=queueurl,
        MessageBody=message
    )
    #print(response)
#To receive the Message
def receive_message(queueurl):
    response = sqs_client.receive_message(
        QueueUrl=queueurl,
        MaxNumberOfMessages=1,
        #WaitTimeSeconds=10,
    )

    #print(f"Number of messages received: {len(response.get('Messages', []))}")

    for message in response.get("Messages", []):
        message_body = message["Body"]
        #print(f"Message : {message_body
        return message_body