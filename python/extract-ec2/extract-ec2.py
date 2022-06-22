import boto3
import botocore
import os
import json
import argparse


def main():
    region = os.getenv('AWS_REGION')
    ec2 = boto3.Session().client('ec2', region_name=region)
    vpc_info = list()
    vpc_subnets = dict()
    parser = argparse.ArgumentParser()
    parser.add_argument('-vpcid', help='filter vpc id')
    args = parser.parse_args()

    if args.vpcid:
        filtr = args.vpcid
    elif os.getenv('VPCID'):
        filtr = os.getenv('VPCID')
    else:
        filtr = None

    if filtr is None:
        vpcs = ec2.describe_vpcs()
        subnets = ec2.describe_subnets()
        security_groups = ec2.describe_security_groups()
        instances = ec2.describe_instances(Filters=[
            {'Name': 'instance-state-name', 'Values': ['pending', 'running', 'shutting-down', 'stopping', 'stopped']}])
        internet_gws = ec2.describe_internet_gateways()
        nat_gws = ec2.describe_nat_gateways()
    else:
        vpcs = ec2.describe_vpcs(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [filtr]
            }])
        subnets = ec2.describe_subnets(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [filtr]
            }])
        security_groups = ec2.describe_security_groups(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [filtr]
            }])
        instances = ec2.describe_instances(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [filtr]
            }, {
                'Name': 'instance-state-name',
                'Values': ['pending', 'running', 'shutting-down', 'stopping', 'stopped']
            }])
        internet_gws = ec2.describe_internet_gateways(Filters=[
            {
                'Name': 'attachment.vpc-id',
                'Values': [filtr]
            }])
        nat_gws = ec2.describe_nat_gateways(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [filtr]
            }])

    for vpc in vpcs['Vpcs']:
        if 'Tags' in vpc.keys():
            vpc_info.append({'VpcId': vpc['VpcId'], 'VpcCIDR': vpc['CidrBlock'], 'Vpc_instance_tenacy': vpc['InstanceTenancy'],
                             'DefaultVpc': vpc['IsDefault'], 'VpcTags': vpc['Tags']})
        else:
            vpc_info.append({'VpcId': vpc['VpcId'], 'VpcCIDR': vpc['CidrBlock'], 'Vpc_instance_tenacy': vpc['InstanceTenancy'],
                             'DefaultVpc': vpc['IsDefault']})

    vpc_subnets = dict()
    for subnet in subnets['Subnets']:
        if subnet['VpcId'] not in vpc_subnets:
            vpc_subnets[subnet['VpcId']] = []

    for subnet in subnets['Subnets']:
        if subnet['VpcId'] in vpc_subnets:
            vpc_subnets[subnet['VpcId']].append(subnet['SubnetId'])

    for vpc_id in vpc_subnets:
        for v in vpc_info:
            if vpc_id == v['VpcId']:
                ind = vpc_info.index(v)
                vpc_info[ind].update({'subnets': vpc_subnets[vpc_id]})

    for vpc in vpc_info:
        for subnet in subnets['Subnets']:
            if subnet['VpcId'] == vpc['VpcId']:
                if subnet['SubnetId'] in vpc['subnets']:
                    ind = vpc_info.index(vpc)
                    vpc_info[ind]['subnet-details-{}'.format(
                        subnet['SubnetId'])] = subnet

        for security_group in security_groups['SecurityGroups']:
            if security_group['VpcId'] == vpc['VpcId']:
                ind = vpc_info.index(vpc)
                vpc_info[ind]['security-group-details-{}'.format(
                    security_group['GroupId'])] = security_group

    for instance in instances['Reservations']:
        for i in instance['Instances']:
            for vpc in vpc_info:
                if i['VpcId'] == vpc['VpcId']:
                    ind = vpc_info.index(vpc)
                    vpc_info[ind]['Instance-{}-{}'.format(
                        vpc['VpcId'], i['InstanceId'])] = i

    for nat_gw in nat_gws['NatGateways']:
        for vpc in vpc_info:
            if nat_gw['VpcId'] == vpc['VpcId']:
                ind = vpc_info.index(vpc)
                vpc_info[ind]['Nat-GW-{}-{}'.format(
                    vpc['VpcId'], nat_gw['NatGatewayId'])] = nat_gw

    for internet_gw in internet_gws['InternetGateways']:
        for internetgw in internet_gw['Attachments']:
            for vpc in vpc_info:
                if internetgw['VpcId'] == vpc['VpcId']:
                    ind = vpc_info.index(vpc)
                    vpc_info[ind]['Internet-GW-{}-{}'.format(
                        vpc['VpcId'], internet_gw['InternetGatewayId'])] = internet_gw

    print(json.dumps(vpc_info, sort_keys=True, default=str, indent=4))

    # # print(json.dumps(nat_gws['NatGateways'], sort_keys=True, default=str, indent=4))
    # print(json.dumps(internet_gws['InternetGateways'],
    #       sort_keys=True, default=str, indent=4))


if __name__ == '__main__':
    try:
        main()
    except (botocore.exceptions.NoCredentialsError, botocore.exceptions.PartialCredentialsError, botocore.exceptions.NoRegionError) as e:
        print('Missing credentials. Check your programatic access and region.')
