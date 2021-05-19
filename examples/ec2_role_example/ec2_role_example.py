from easyaws.ec2_vm import Ec2Tool
from easyaws.s3_bucket import S3Bucket

def main_role_demo():
    creds = Ec2Tool.get_credentials()
    print('credentials:', creds)
    return creds

def use_s3_with_credentials(aws_access_key_id, aws_secret_access_key):
    my_s3 = S3Bucket(bucket_name='my-first-bucket-84629694625', aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key, region='us-east-1')
    ans = my_s3.s3_client.list_buckets()
    return ans


def do_all():
    aws_access_key_id, aws_secret_access_key = main_role_demo()
    use_s3_with_credentials(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    print(ans)

do_all()