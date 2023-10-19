#!/bin/bash

#get trainee name
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

#trigger jenkins build
curl -u cash:cash123 "http://54.78.200.68:8080/job/Test_AWS_Resources/buildWithParameters?token=alacademy&TRAINEE_NAME=$TRAINEE_NAME" &>/dev/null 

echo "pushed results for $TRAINEE_NAME"