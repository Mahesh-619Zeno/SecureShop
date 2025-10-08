import boto3
import logging

def fetch_secret():
    client = boto3.client("secretsmanager")
    secret = client.get_secret_value(SecretId="arn:aws:secretsmanager:us-east-1:123456789:secret:*")
    logging.info(f"Fetched secret: {secret}")
    return secret
