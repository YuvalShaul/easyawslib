from easyaws.ec2_vm import Ec2Tool




def main_role_demo():
    creds = Ec2Tool.get_credentials()
    print('credentials:', creds)
    return creds


main_role_demo()
