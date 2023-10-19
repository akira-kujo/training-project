import profile
import boto3
import re
import sys
import pprint
from sg_resources import *
from utilities import *




# Global variables

# PLEASE INPUT YOUR NAME HERE AS A STRING
TRAINEE_NAME = "Samantha"


REGION = "eu-west-1"
KEY_TAG = "Name"
COHORT_IDENTIFIER= "user.+"
DEFAULT_VPC = "" #VPC Identifier via AWS MC

def  make_dict_from_list(l):
    """
        return a python dictionary when given a list of Key-Value dictionaries.

        We use this to parse the results given to us by the boto3 library (in
        turn from the AWS API) into something that's easier to manipulate in Python
    """
    result = {}
    for kv_pair in l:
        k = kv_pair['Key']
        v = kv_pair['Value']
        result[k] = v
    return result

# EC2 Variables

ec2 = boto3.resource('ec2', REGION)
ec2_client = boto3.client('ec2', REGION)
key_pair=ec2_client.describe_key_pairs()
subnet = ec2_client.describe_subnets(Filters=[{'Name': 'tag-key', 'Values': ['Name']}])

    

# Test 1: EC2

# Function for creating list of tags from instances by identifying cohorts 
def get_cohort_tags():
# Iterate through ec2 instances
    instance_iterator = ec2.instances.filter(Filters=[{'Name': 'tag-key', 'Values': ['Name']}])
    cohort_list = []
    for instance in instance_iterator:
# Identify instances by tags - Key: Name
        tags = make_dict_from_list(instance.tags)
        name_tag = tags['Name']
        if re.search(COHORT_IDENTIFIER, name_tag):
# append to list if correct credentials exist
            cohort_list.append(name_tag)

    return cohort_list
  
# Filtering results from cohort identifiers by trainee name
def get_cohort_tags_for_user(username):
# Iterate through ec2 instances
    instance_iterator = ec2.instances.filter(Filters=[{'Name': 'tag-key', 'Values': ['Name']}])
    tag_list = get_cohort_tags()
    results = []
    for tag in tag_list:
# check if trainee has an instance through global var
        if checks_lowercase_string(tag, username):
            results.append(tag)
    
    print(f"DBG: resulting tags for user are: {results}") 
    return results
 
# Test 2: Key Pair

# Create list for rsa keys created with cohort identifier
def find_key_pair():
    data_key_finder=key_pair["KeyPairs"]
    key_list = []
    for key in data_key_finder:
# Identify rsa keys
        if key["KeyType"] == "rsa": 
            result =  key["KeyPairId"], key["KeyFingerprint"], key["KeyName"] 
            for rsa in result:
                if re.search(COHORT_IDENTIFIER, rsa):
                    key_list.append(rsa)
    return key_list

# Check if trainee has rsa key
def check_trainee_key():
# Check to see if tags are correct by name
    if any(checks_lowercase_string(name, TRAINEE_NAME) for name in find_key_pair()):
        print(f"The correct key for {TRAINEE_NAME} exists")    
    else:
        print('The keys are incorrect, please retry')

# Test 3: Subnets

# Checking if default VPC includes trainee name and cohort identifier
def subnets_in_vpc():
    subnet_finder = subnet["Subnets"]
    identified_subnet_list = []
# Allocating subnets by vpc - default vpc
    for vpc_subnet in subnet_finder:
        if vpc_subnet["VpcId"] == DEFAULT_VPC:   
# Listing subnets by tags
            list_of_subnet = vpc_subnet["Tags"] 
# Find trainee's subnets by tags - trainee name and cohort
            for trainee_subnet in list_of_subnet:
                result = trainee_subnet.get('Value')
# Checking trainee name and cohort - code removed extra regex code for cohort identifier 
                if checks_lowercase_string(result, TRAINEE_NAME) and COHORT_IDENTIFIER.replace(".+", "") in result:
                    identified_subnet_list.append(result)
    return identified_subnet_list

# Test if subnet resource exists under studnet's name
def check_trainee_subnet():
# Converting list into string
    string_subnet = ''.join(str(x) for x in subnets_in_vpc())
    if checks_lowercase_string(string_subnet,TRAINEE_NAME):
        print(f"The correct subnet for {TRAINEE_NAME} exists")    
    else:
        print('The subnets are incorrect, please retry')


def main():
    get_cohort_tags_for_user(TRAINEE_NAME)
    check_trainee_key()
    check_trainee_subnet()
    sg_rule_user()
main()
