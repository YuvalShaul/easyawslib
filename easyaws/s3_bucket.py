import json
import boto3
import util


class S3Bucket:
    def __init__(self, bucket_name, aws_access_key_id=None, aws_secret_access_key=None, region=None):
        confdata = util.get_conf()
        aws_access_key_id = aws_access_key_id or confdata['access_key_id']
        aws_secret_access_key = aws_secret_access_key or confdata['secret_access_key']
        region = region or confdata['region']

        self.s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                      region_name=region)
        self.s3_resource = boto3.resource('s3', aws_access_key_id=aws_access_key_id,
                                      aws_secret_access_key=aws_secret_access_key,
                                          region_name=region)
        self.bucket_name = bucket_name
        self.region = region

    def upload_file(self, *, file_path, key_name ):
        self.s3_resource.meta.client.upload_file(Filename=file_path, Bucket=self.bucket_name, Key=key_name)

    def get_bucket_file_url(self, fname_key):
        bucket_location = self.s3_client.get_bucket_location(Bucket=self.bucket_name)['LocationConstraint']
        object_url = f"https://{self.bucket_name}.s3.{bucket_location}.amazonaws.com/{fname_key}"
        return object_url

    def list_all_files(self):
        response = self.s3_client.list_objects(Bucket=self.bucket_name)
        return response['Contents']

    def get_bucket_s3_uri(self):
        return f's3://{self.bucket_name}/'

    def get_S3_bucket(self):
        '''
        Make sure a bucket (whose name is in self.bucket_name) was created.
        '''
        all = self.s3_resource.buckets.all()
        all_buckets = [bucket for bucket in all]
        # other_buckets = self.get_other_buckets()
        bucket_names = [bucket.name for bucket in all_buckets]
        if self.bucket_name in bucket_names:
            return

        # print(f'Bucket {BUCKET_NAME} not found. Creating...')
        self.s3_client.create_bucket(
            ACL='private',
            # CreateBucketConfiguration={'LocationConstraint': self.region},
            Bucket=self.bucket_name
        )

    def set_policy(self):
        bucket_policy =  {
            "Version": "2012-10-17",
            "Id": "Full public",
            "Statement": [
                {
                    "Sid": "Allow All",
                    "Effect": "Allow",
                    "Principal": "*",
                    # "Resource": "*",
                    "Action": [
                        "s3:*"
                    ],
                    "Resource": f"arn:aws:s3:::{self.bucket_name}/*"
                }
            ]
        }

        # Convert the policy from JSON dict to string
        bucket_policy = json.dumps(bucket_policy)

        # Set the new policy
        self.s3_client.put_bucket_policy(Bucket=self.bucket_name, Policy=bucket_policy)


    def get_other_buckets(self):
        ans = self.s3_client.list_buckets()
        bucket_list = ans['Buckets']
        bucket_owner = ans['Owner']
        return bucket_list, bucket_owner



if __name__ == '__main__':
    my_s3 = S3Bucket(bucket_name='my-first-bucket-84629694625')
    my_s3.get_S3_bucket()
    my_s3.set_policy()
    # buckets = my_s3.get_other_buckets()
    # url = my_s3.get_bucket_file_url('file1.txt')
    # print(my_s3.s3_client.meta.endpoint_url)
    all_files = my_s3.list_all_files()
    print(all)


