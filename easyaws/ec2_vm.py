import boto3
import util


class Ec2Tool:
    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region=None):
        confdata = util.get_conf()
        aws_access_key_id = aws_access_key_id or confdata['access_key_id']
        aws_secret_access_key = aws_secret_access_key or confdata['secret_access_key']
        region = region or confdata['region']

        self.ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id,
                                       aws_secret_access_key=aws_secret_access_key, region_name=region)
        self.ec2_resource = boto3.resource('ec2', aws_access_key_id=aws_access_key_id,
                                           aws_secret_access_key=aws_secret_access_key,
                                           region_name=region)
        self.security_group = self.ec2_resource.SecurityGroup('id')

    def find_AMI_image(self, images):
        '''
        Find an image(s) from a list of accepted image ids. Image selected will match the current region ID
        (embedded in the ec2 client), and a filter parameter as defined in boto3 ec2.describe_images
        (see here: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_images)
        filters: boto3 filter parameter
        :param images: A list of image ids to specify as a filter
        Returns: a list of image IDs matching the filter
        '''
        filters = [{'Name': 'image-id', 'Values': images}]
        response = self.ec2_client.describe_images(Filters=filters)
        image_ids = [image['ImageId'] for image in response['Images']]
        return image_ids

    def get_sg_id(self):
        response = self.ec2_client.describe_security_groups()
        pass

    def find_ec2_private_addresses(self, name=None):
        addrs = []
        instances = self.ec2_resource.instances.filter(Filters=[
            {'Name': 'tag:Name', 'Values': [name]},
            {
                'Name': 'instance-state-code',
                'Values': ['16'],  # only running instances
            },
        ])
        for instance in instances:
            addrs.append(instance.private_ip_address)

        return addrs

        # response = self.ec2_client.describe_tags(
        #     Filters=[{'Name': 'tag:Name', 'Values': [name]}])
        # print(response)


if __name__ == '__main__':
    my_ec2_tool = Ec2Tool()
    response = my_ec2_tool.find_AMI_image(images=['ami-0742b4e673072066f'])
    print(response)
    # my_ec2_tool.get_sg_id()

    # addresses = my_ec2_tool.find_ec2_private_addresses(name='bignet-orchestrator')
