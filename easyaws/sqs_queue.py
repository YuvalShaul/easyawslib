import json
import boto3
import util


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

    def get_queue_url(self, queue_name):
        response = self.sqs_client.get_queue_url(
            QueueName=queue_name,
        )
        return response["QueueUrl"]

    def send_message(self,msg, q_url):
        response = self.sqs_client.send_message(
            QueueUrl=q_url,
            MessageBody=json.dumps(msg)
        )
        return response

    def receive_and_delete_message(self, q_url):
        response1 = self.sqs_client.receive_message(
            QueueUrl=q_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
        )
        messages = response1.get('Messages', [])

        for m in messages:
            response2 = self.sqs_client.delete_message(
                QueueUrl=q_url,
                ReceiptHandle=m['ReceiptHandle']
            )

        return messages





if __name__ == '__main__':
    my_sqs = SQSQueue(queue_name='test1')   # So this is the queue name I want
    my_sqs.get_SQS_queue()              # Create it, or make sure it exist
    q_url = my_sqs.get_queue_url('test1')
    print(q_url)
    msg = {"name": "Dave"}
    response = my_sqs.send_message(msg, q_url)
    msgs = my_sqs.receive_and_delete_message(q_url)
    print(msgs)




