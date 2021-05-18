'''
The following file denonstrates the use of IAM role that allows an EC2 to access S3 bucket.
Use:
    1 - Use the console to create an EC2 instance and a S3 bucket.
    2 -
'''

from easyaws.ec2_vm import Ec2Tool




def main_role_demo():
    creds = Ec2Tool.get_credentials()
    print('credentials:', creds)
    return creds


main_role_demo()
