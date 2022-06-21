Script that will output information for:
*   vpcs
*   subnets in vpc
*   security groups in vpc
*   ec2 instances in vpc

How to get information only for given vpc:
*   python extract-ec2.py -vpcid vpc-0d9bb3757b5b7f14d
*   export VPCID=vpc-0d9bb3757b5b7f14d; python extract-ec2.py

How to get information for all vpcs:
*   python extract-ec2.py