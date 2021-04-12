import json
import boto3
import util

class SNSTool:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region=None):
        confdata = util.get_conf()
        aws_access_key_id = aws_access_key_id or confdata['access_key_id']
        aws_secret_access_key = aws_secret_access_key or confdata['secret_access_key']
        region = region or confdata['region']

        self.sns_client = boto3.client('sns', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region)
        self.sns_resource = boto3.resource('sns', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                          region_name=region)

    def send_dict_msg(self, msg, target_arn):
        response = self.sns_client.publish(
            TargetArn=target_arn,
            Message=json.dumps({'default': json.dumps(msg),
                                'sms': 'here a short version of the message',
                                'email': 'here a longer version of the message'}),
            Subject='a short subject for your message',
            MessageStructure='json')
        return response


if __name__ == '__main__':
    my_sns = SNSTool()
    msg =  {"foo": "bar"}

    ans = my_sns.send_dict_msg(msg, 'arn:aws:sns:us-east-1:647000152682:news')