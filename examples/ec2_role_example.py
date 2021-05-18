'''
The following file denonstrates the use of IAM role that allows an EC2 to access S3 bucket.
Use:
    1 - Use the console to create an EC2 instance and a S3 bucket.
    2 -
'''

from easyaws.ec2_vm import Ec2Tool
import easyaws.util

def demo_ec2_role(my_ec2):
    a, b = my_ec2.get_credentials()
    print(a,b)



def main_role_demo():
    confdata = easyaws.util.get_conf('easyaws_conf.json')
    my_ec2_tool = Ec2Tool(aws_access_key_id=confdata['access_key_id'],
                          aws_secret_access_key = confdata['secret_access_key'],
                          region = confdata['region'])
    creds = my_ec2_tool.get_credentials()
    return creds


main_role_demo()
