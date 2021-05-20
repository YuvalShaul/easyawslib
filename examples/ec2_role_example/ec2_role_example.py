from easyaws.ec2_vm import Ec2Tool
from easyaws.s3_bucket import S3Bucket

def get_metadata_creds():
    creds = Ec2Tool.get_credentials()
    print('metadata credentials:', creds)
    return creds

def get_metadata_role_arn():
    role_arn = Ec2Tool.get_role()
    print('role arn: ', role_arn)
    return role_arn

def list_s3_buckets():
    my_s3 = S3Bucket(bucket_name='my-first-bucket-84629694625')
    ans = my_s3.s3_client.list_buckets()
    print(ans)
    return ans


def do_all():
    region = 'us-east-1'
    aws_access_key_id, aws_secret_access_key, token = get_metadata_creds()
    role_arn = get_metadata_role_arn()
    try:
        list_s3_buckets()
    except Exception as e:
        print('Creds not good!!!', e)


do_all()