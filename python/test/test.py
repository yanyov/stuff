import subprocess
import boto3
import botocore
import os
import json
import argparse

region = os.getenv('AWS_REGION')


def vpc():
    parser = argparse.ArgumentParser()
    parser.add_argument('-filter', help='filter vpc id')
    args = parser.parse_args()

    info = list()

    ec2 = boto3.Session().client('ec2', region_name=region)
    if args.filter is None:
        vpcs = ec2.describe_vpcs()
        rt = ec2.describe_route_tables()
        subnets = ec2.describe_subnets()
    else:
        vpcs = ec2.describe_vpcs(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [args.filter]
            }])
        rt = ec2.describe_route_tables(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [args.filter]
            }])
        subnets = ec2.describe_subnets(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [args.filter]
            }])

    for v in vpcs['Vpcs']:
        info.append({'VpcId': v['VpcId']})
    for subnet in subnets['Subnets']:
        print(subnet)
    # print(info)
    return vpcs['Vpcs'], rt['RouteTables']


def main():

    # subprocess.run(['cd', '../../services/vpc/'], shell=True)
    # subprocess.run(['ls', '-l'], shell=True)
    cmd = list()
    vpcs, route_tables = vpc()
    # for v in vpcs:
    #     print(json.dumps(v, sort_keys=True, indent=4))

    # for rt in route_tables:
    #     print(json.dumps(rt, sort_keys=True, indent=4))


if __name__ == '__main__':
    try:
        main()
    except (botocore.exceptions.NoCredentialsError, botocore.exceptions.PartialCredentialsError, botocore.exceptions.NoRegionError) as e:
        print('Missing credentials. Check your programatic access and region.')
