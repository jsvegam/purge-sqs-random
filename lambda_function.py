import json
import random
import boto3
pipeline = boto3.client('codepipeline')


# Create SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/806175290270/DayliMembers'


def lambda_handler(event, context):
    # TODO implement

    response = sqs.purge_queue(
        QueueUrl=queue_url
    )

    return {
        'statusCode': 200,
        'body': json.dumps('purgin SQS queue')
    }
