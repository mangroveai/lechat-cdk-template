from aws_cdk import CfnOutput, NestedStack, Stack
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_ssm as ssm
from constructs import Construct


class Vpc(Stack):

    def __init__(
        self,
        scope: Construct,
        id: str,
        cidr: str,
        **kwargs,
    ) -> None:
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            "VPC",
            vpc_name=f"vpc",
            max_azs=3,
            #cidr=cidr,
            ip_addresses= ec2.IpAddresses.cidr(cidr),

            # configuration will create 2 groups in 3 AZs = 6 subnets.
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="public",
                    cidr_mask=25
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    name="private",
                    cidr_mask=25,
                ),
            ],
            nat_gateways=3,
            gateway_endpoints={
                "s3": ec2.GatewayVpcEndpointOptions(
                    service=ec2.GatewayVpcEndpointAwsService.S3
                )
            },
        )
