

import boto3
import os
import json


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


def vpc_info():
    ec2 = boto3.resource('ec2')

    vpc_info = list()

    vpc_subnets = dict()
    # Create list of maps with 'VpcId', 'VpcCIDR', 'Vpc_instance_tenacy', 'DefaultVpc', 'VpcTags'
    for vpc in ec2.vpcs.all():
        vpc_info.append({'VpcId': vpc.id, 'VpcCIDR': vpc.cidr_block, 'Vpc_instance_tenacy': vpc.instance_tenancy,
                         'DefaultVpc': vpc.is_default, 'VpcTags': vpc.tags})

        all_subnets = vpc.subnets.all()
        for subnet in all_subnets:
            if subnet.vpc_id not in vpc_subnets:
                vpc_subnets[subnet.vpc_id] = []

        for subnet in all_subnets:
            if subnet.vpc_id in vpc_subnets:
                vpc_subnets[subnet.vpc_id].append(subnet.id)

    # Add all subnets per vpc
    for vpc_id in vpc_subnets:
        for v in vpc_info:
            if vpc_id == v['VpcId']:
                ind = vpc_info.index(v)
                vpc_info[ind].update({'subnets': vpc_subnets[vpc_id]})

    return vpc_info


def subnet_info():
    """This function will collect additional information for each subnet"""
    ec2 = boto3.client('ec2')

    subnets_info = list()
    subnets = ec2.describe_subnets()
    for subnet in subnets['Subnets']:
        subnets_info.append({'VpcId': subnet['VpcId'], 'SubnetId': subnet['SubnetId'],
                            'CidrBlock': subnet['CidrBlock'], 'AvailabilityZone': subnet['AvailabilityZone'], 'Tags': subnet['Tags']})

    return subnets_info


def sec_groups_info():
    """This function will collect additional information for each security group"""
    ec2 = boto3.client('ec2')
    security_groups = ec2.describe_security_groups()

    return security_groups['SecurityGroups']


def data(vpcs, sn, sg):
    """This function will combine all of the gathered information into list of maps(map for each vpc with info for it)"""
    for vpc in vpcs:
        for subnet in sn:
            if subnet['VpcId'] == vpc['VpcId']:
                if subnet['SubnetId'] in vpc['subnets']:
                    ind = vpcs.index(vpc)
                    vpcs[ind]['subnet-details-{}'.format(
                        subnet['SubnetId'])] = subnet

        for security_group in sg:
            if security_group['VpcId'] == vpc['VpcId']:
                ind = vpcs.index(vpc)
                vpcs[ind]['security-group-details-{}'.format(
                    security_group['GroupId'])] = security_group

    print(json.dumps(vpcs, sort_keys=True, indent=4))
    session = boto3.Session()
    s3 = session.resource('s3')
    s3_bucket = os.getenv('BUCKET')
    res = s3.Bucket(s3_bucket).put_object(
        Body=json.dumps(vpcs), Key='env-info.txt')


def main():
    vpcs = vpc_info()
    sn = subnet_info()
    sg = sec_groups_info()
    data(vpcs, sn, sg)


main()
