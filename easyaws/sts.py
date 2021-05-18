import json
import boto3
import util


class STS:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region=None):
        confdata = util.get_conf()
        aws_access_key_id = aws_access_key_id or confdata['access_key_id']
        aws_secret_access_key = aws_secret_access_key or confdata['secret_access_key']
        region = region or confdata['region']

        self.sts_client = boto3.client('sts', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region)

        self.region = region

    def assume_role(self, RoleArn, RoleSessionName):
        response = self.sts_client.assume_role(RoleArn, RoleSessionName)
        return response['Credentials']
