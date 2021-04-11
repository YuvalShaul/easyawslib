import json
import boto3
import util
import re


class SQSQueue:
    def __init__(self, queue_name, aws_access_key_id=None, aws_secret_access_key=None, region=None):
        confdata = util.get_conf()
        aws_access_key_id = aws_access_key_id or confdata['access_key_id']
        aws_secret_access_key = aws_secret_access_key or confdata['secret_access_key']
        region = region or confdata['region']

        self.sqs_client = boto3.client('sqs', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region)
        self.sqs_resource = boto3.resource('sqs', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                          region_name=region)
        self.queue_name = queue_name
        self.region = region

    def get_SQS_queue(self):
        other_queues = self.get_other_queues()
        queue_names = [q.split('/')[-1] for q in other_queues]
        if self.queue_name in queue_names:
            return

        self.Queue = self.sqs_resource.create_queue(QueueName=self.queue_name, Attributes={'DelaySeconds': '5'})
        return self.Queue

    def get_other_queues(self):
        ans = self.sqs_client.list_queues()
        try:
            sqs_queue_list = ans['QueueUrls']
            return sqs_queue_list
        except:
            return []

if __name__ == '__main__':
    my_sqs = SQSQueue(queue_name='test1')
    q = my_sqs.get_SQS_queue()


