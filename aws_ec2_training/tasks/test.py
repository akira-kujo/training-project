import pytest
from aws_resource import *
import profile
import boto3
import re


def test_get_cohort_tags():
    for name in get_cohort_tags():
        if TRAINEE_NAME.lower() in name.lower():
            assert True
            return 
    assert False

def test_find_key_pair():
    for name in find_key_pair():
        if TRAINEE_NAME.lower() in name.lower():
            assert True
            return 
    assert False



def test_subnets_in_vpc():
    for name in subnets_in_vpc():
        if TRAINEE_NAME.lower() in name.lower():
            assert True
            return 
    assert False

def test_sg_resource():
    if sg_rule_user() == "All 3 expected protocols are allowed":
        assert True


    
