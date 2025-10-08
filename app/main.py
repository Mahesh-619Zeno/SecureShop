import os
import logging
import boto3
from flask import Flask, request
from app.user_service import get_user

app = Flask(__name__)

AWS_ACCESS_KEY = "AKIA123456789EXAMPLE"
AWS_SECRET_KEY = "abcd1234SECRETKEY"

s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

@app.route("/login", methods=["POST"])
def login():
    user = request.json.get("username")
    password = request.json.get("password")
    logging.info(f"Login attempt for {user} with password {password}")
    response = s3.list_objects(Bucket="public-bucket", EndpointUrl="http://s3.amazonaws.com")
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
