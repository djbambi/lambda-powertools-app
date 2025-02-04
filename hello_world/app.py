from aws_lambda_powertools import Logger

logger = Logger(service="HelloWorldService")

def lambda_handler(event, context):
    logger.info("Lambda function invoked")
    logger.debug(f"Event received: {event}")

    return {
        "statusCode": 200,
        "body": "Hello from AWS Lambda with Powertools!"
    }