# Trainee Repository

This repository includes both the tasks and tests to familiarise Academy Trainees with manually deploying resources into AWS.

The tasks set out for you will include creating a Key Pair, EC2 Instance, Subnet and Security Group.

Testing if the resources are made correctly can be done either locally (on your mac) or through an online Jenkins instance which will also let the trainer know your current progress...
<br>
<br>

## Prerequisites
To be able to test locally you will need to have the AWS CLI installed on your mac. This can be achieved with the following code:

```
curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"
sudo installer -pkg AWSCLIV2.pkg -target /
```
Enter the password for your mac when prompted. Then do the following steps:

* Go onto AWS and navigate to the IAM console
* Go to the "users" of the navigation pane (on the left)
* Click on your user email
* add permissions until your match those shown in the permissions.png file within this repo
* Go to the "Security credentials" tab
* Under "Access keys" select "Create access key"
* Select to show the Secret access key or optionally download the csv file. ((**if you do not store the csv and close the pop-up you will not be able to retrieve the secret key again**))
* Go to your macs terminal and enter the following command, you will then prompted for a series of values enter as explained below.

```
aws configure
```

  * AWS Access Key ID: \<enter the access key ID from aws>
  * AWS Secret Access Key: \<enter the secret access key from aws>
  * Default region name: eu-west-1
  * Default output format: json

<br>
<br>

-------------------------------------------------------

## Getting started

### Fork this repository and clone to your local machine.

![Fork-repository](./fork-repository.jpeg)

```bash
# Clone your new repository
$ git clone git@github.com:<yourname>/training-project.git
```


There are several python files within this repository: 
    - `aws_resources.py` consists of the python functions which are being called to test to see if the user has correctly met their objectives.
    - `test.py` comprises the pytest which will authenticate and validate the aforementioned `aws_resources.py`


## Completing the Exercises

Navigate to the *tasks* folder and go through the `README.md` within the folder in order to understand the exercises - once these have been completed you can check through your answers as explained below.

## Local Testing

Ensure that `aws_resources.py` and `sg_resources.py` has the <TRAINEE_NAME:> changed to *your name* (e.g. TRAINEE_NAME = 'Samantha')

To locally test and see if you have correctly created the resources, navigate to the root of this repo and use the command:

```
cd tasks
chmod +x main.sh
./main.sh
```
Following this, in order to run the pytest navigate to the root of this repo and use the command:

```
cd tasks
pytest test.py
```

The command should return several lines of code which indicate whether you have succesfully completed the tasks.




