# AWS Resource Creation Tasks
The following tasks will help you gain experience manually deploying resources through the AWS browser interface.

To run the tests navigate to the root of this repo and use these commands: 
```bash
python3 test.py
```
1. Key Pair
User Story: You need to create a new key-pair which will allow you to have a unique key for connecting to resources on AWS.

Your task is to create an AWS key-pair with the following parameters: * Name: CH11_\<your name>_ie_general * Type: RSA * Format: .pem * Tags: * Project: Academy




2. EC2 Instance
User Story: You need to create a new Virtual Machine to allow you to gain experience using concepts such as ssh and bash scripting. You want to make this in AWS.

Your task is to create an EC2 instance with the following parameters: * Name: CH11_\<your name>_test * Tags: * Project: Academy * Application & OS Image: Ubuntu * Instance Type: t2.micro * KeyPair: \<your key pair> * VPC: default * SecurityGroup: AcademySG * Storage: 8 GB



3. Subnet
User Story: You need to create a new subnet inside the VPC to allow you to seperate your resources from others. This is useful if down the line you want to make a subnet "private" meaning it cannot be accessed from the internet.

Your task is to create a subnet with the following parameters: * VPC: default * Subnet name: CH11_\<your name>_Public * AvailabilityZone: No prefernce * CIDR block: choose the next available block from within the VPC. * Tags: * Project: Academy



4. Security Group
User Story: You need to create a new security group for your instances so that you can ensure their safety by only allowing access via certain ports.

Your task is to create a securitygroup with the following parameters:
Name: CH11_\<your name>SG
VPC: default
Inbound Rules (3 respectively):
type: HTTP, HTTPS, SSH
source: anywhere IPv4 (for all)
Tags:
Project: Academy

