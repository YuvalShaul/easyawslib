import json
import boto3


class STS:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region):
        self.sts_client = boto3.client('sts', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region)

        self.region = region

    def assume_role(self, RoleArn, RoleSessionName):
        response = self.sts_client.assume_role(RoleArn=RoleArn, RoleSessionName=RoleSessionName)
        return response['Credentials']
