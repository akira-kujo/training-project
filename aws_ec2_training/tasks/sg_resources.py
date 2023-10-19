# 1 -Find ALL Security groups
#   a. We need to grab the Group name alongside the IP address
# 2 -Make a new of security groups that match the names we care about
# 3 - Describe the security groups from step 2
# 4 - Loop over each security group and assert that inbound/outbound is 80
# If assertion fails, print the security group name

import profile
import boto3
import re
import sys
import pprint
from utilities import *





# Global variables

# PLEASE INPUT YOUR NAME HERE AS A STRING
TRAINEE_NAME = "Kitty"


REGION = "eu-west-1"
KEY_TAG = "Name"
COHORT_IDENTIFIER= "CH10"
DEFAULT_VPC = "vpc-4bb64132"



sg = boto3.client('ec2', REGION)

def find_users_sg(sg, username):
    # removes case insensitivity for trainee name
	search_pattern = f'{COHORT_IDENTIFIER}_(i?){TRAINEE_NAME}(SG)?'
	if re.search(search_pattern, sg['GroupName']):
		return True
	

sg = boto3.client('ec2', REGION)

owner_id = boto3.client('sts').get_caller_identity().get('Account')
# print(owner_id)

security_groups = sg.describe_security_groups()['SecurityGroups']
# print("All security groups:")
# pprint.pprint(security_groups)

sg_for_user = list(filter(lambda sg: find_users_sg(sg, TRAINEE_NAME), security_groups))





sg_owner_id = ([{"name": f_group['OwnerId']} for f_group in security_groups])
# print(sg_owner_id)
sg_names = ([{"name": f_group['GroupName']} for f_group in security_groups])
sg_ports = ([{"name": f_group['IpPermissions']} for f_group in security_groups])

allows_ssh = False
allows_http = False
allows_https = False

def sg_rule_user():
    # checking if SG list for trainee is empty or not
    if len(sg_for_user) == 0:
        print("User's security group not found")
        return
    elif len(sg_for_user) > 1:
        print("More than one security group found for user")
    for rule in  sg_for_user[0]['IpPermissions']:
        # Don't be tempted to refactor this into the elif construct else we
        # won't detect the case when there is one rule which allows all three
        # services
        if rule['FromPort'] <=80 and rule['ToPort'] >= 80:
            allows_http = True
        if rule['FromPort'] <= 22 and rule['ToPort']>= 22:
            allows_ssh = True
        if rule['FromPort'] <= 443 and rule['ToPort']>= 443:
            allows_https = True

    if allows_http and allows_https and allows_ssh:
        print("All 3 expected protocols are allowed")
    else:
        print("Not all expected traffic is allowed")

def main():
        sg_rule_user()
        
	    
main()