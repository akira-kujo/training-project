#!/bin/bash


if [ $# == 0 ]
then
    echo "usage: tests/check_aws_resource_creation.sh <your name>"
    echo "enter your name to allow filter to work correctly: "
    read TRAINEE_NAME
else
    TRAINEE_NAME=$1
fi

while [ -z "$TRAINEE_NAME" ]
do
    echo "you must enter a name to filter aws results"
    read TRAINEE_NAME
done

SCORE=0 #keeps track of their score through the tests and returns at end


#task1 - create a keypair in AWS, name it: "CH11_<your name>_ie_general", set type to rsa and give the following tag:
#Project = Academy

#test1 - checks for correctly created key pair

RETURNED_KP=`aws ec2 describe-key-pairs | jq '[.KeyPairs[]|{KeyName: .KeyName, Type: .KeyType, Tags: (.Tags|from_entries)}]|map(select(.KeyName != null))|map(select((.Tags|length) > 0))|map(select(.Tags.Project== "Academy"))|map(select(.Type = "rsa"))|map(select(.KeyName | match('\"$TRAINEE_NAME\_ie_general\"'; "i")))|length'` 

if [ $RETURNED_KP -gt 0 ]
then
    SCORE=$((SCORE+1))
    ERR_LIST+=("Test1 Passed: Correct Key Pair found")
else
    ERR_LIST+=("Test1 Failed: No Key Pair with the correct specification")
fi

#task2 - create an instance in AWS, in the default vpc and subnet, that has the following spec: t2.micro, either AWS Linux or Ubuntu, AcademySG security group and is tagged with:
#Name = CH11_<your name>_test
#Project = Academy

#test2 - checks for correctly created instance
RETURNED_INSTANCES=`aws ec2 describe-instances | jq '[.Reservations[].Instances[]|{IP: .PrivateIpAddress, InstType: .InstanceType, InstanceName: (.Tags|from_entries).Name, Project: (.Tags|from_entries).Project, SG: (.SecurityGroups[].GroupName), VPC: .VpcId, Subnet: .SubnetId}]|map(select(.InstanceName != null))|map(select(.Project == "Academy"))|map(select(.SG == "AcademySG"))|map(select(.InstType == "t2.micro"))|map(select(.VPC == "vpc-4bb64132"))|map(select(.InstanceName | match('\"$TRAINEE_NAME\_test\"'; "i")))|length'`

#echo $RETURNED_INSTANCES

if [ $RETURNED_INSTANCES -gt 0 ]
then
    SCORE=$((SCORE+1))
    ERR_LIST+=("Test2 Passed: Correct EC2 Instance found")
else
    ERR_LIST+=("Test2 Failed: No EC2 Instance with the correct specification")
fi

#task3 - create a subnet in AWS, in the default VPC that has the following tags
#Name = CH11_<your name>_Public
#Project = Academy

#test3 - checks for correctly created subnet
RETURNED_SUBNETS=`aws ec2 describe-subnets | jq '[.Subnets[]|{CIDRBlock: .CidrBlock, AZ: .AvailabilityZone, MapPubIpOnLaunch: .MapPublicIpOnLaunch, SubnetName: (.Tags|from_entries).Name, Project: (.Tags|from_entries).Project, VPC: .VpcId}]|map(select(.SubnetName != null))|map(select(.Project == "Academy"))|map(select(.VPC == "vpc-4bb64132"))|map(select(.SubnetName | match('\"$TRAINEE_NAME\_Public\"'; "i")))|length'`

if [ $RETURNED_SUBNETS -gt 0 ]
then
    SCORE=$((SCORE+1))
    ERR_LIST+=("Test3 Passed: Correct Subnet found")
else
    ERR_LIST+=("Test3 Failed: No Subnet with the correct specification")
fi


#task4 - create a securitygroup in AWS, name it: "CH11_<your name>_SG", give it a description if desired, to inbound rules add:
# HTTP (80), HTTPS (443), SSH(22)  then add the following tag:
#Project = Academy

#test4 - checks for correctly created securitygroup

RETURNED_SG=`aws ec2 describe-security-groups | jq '[.SecurityGroups|map(select(.Tags != null))[] | {SG_Name: .GroupName, Inbound: [.IpPermissions[].FromPort], Outbound: .IpPermissionsEgress[].IpProtocol, VPC: .VpcId, Tags: (.Tags|from_entries)}]|map(select(.Tags.Project == "Academy"))|map(select(.Outbound == "-1"))|map(select(.VPC == "vpc-4bb64132"))|map(select(.SG_Name | match('\"$TRAINEE_NAME\\SG\"'; "i")))|length'`

if [ $RETURNED_SG -gt 0 ]
then
    SCORE=$((SCORE+1))
    ERR_LIST+=("Test4 Passed: Correct Security Group found")
else
    ERR_LIST+=("Test4 Failed: No Security Group with the correct specification")
fi

#returns score to terminal (for now)
echo "Tests Passed: $SCORE/4"

#returns errors if any
for value in "${ERR_LIST[@]}"
do
     echo $value
done