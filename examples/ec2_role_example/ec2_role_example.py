from easyaws.ec2_vm import Ec2Tool
from easyaws.s3_bucket import S3Bucket
from easyaws.sts import STS

def get_metadata_creds():
    creds = Ec2Tool.get_credentials()
    print('credentials:', creds)
    return creds

def get_metadata_role_arn():
    role_arn = Ec2Tool.get_role()
    print('role arn: ', role_arn)
    return role_arn

def use_s3_with_credentials(aws_access_key_id, aws_secret_access_key, region):
    my_s3 = S3Bucket(bucket_name='my-first-bucket-84629694625', aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key, region=region)
    ans = my_s3.s3_client.list_buckets()
    return ans

def get_sts_credentials(aws_access_key_id, aws_secret_access_key, token, region, role_arn):
    my_sts = STS(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, token=token, region=region)
    creds = my_sts.assume_role(RoleArn=role_arn, RoleSessionName='abcde')
    return creds

def do_all():
    region = 'us-east-1'
    aws_access_key_id, aws_secret_access_key, token = get_metadata_creds()
    role_arn = get_metadata_role_arn()
    try:
        use_s3_with_credentials(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region=region)
    except:
        print('Creds not good!!!')
    print('=*' * 30)
    creds = get_sts_credentials(aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,
                                token=token, region=region, role_arn=role_arn)
    print('STS creds: ', creds)

do_all()