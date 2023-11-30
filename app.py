import os

from aws_cdk import App, Environment

from src.vpc import Vpc
from tags import tag_stacks

AWS_ACCOUNT = "882863117075" #os.environ["CDK_DEFAULT_ACCOUNT"]
AWS_DEFAULT_REGION = 'eu-west-1'

CIDR='10.1.0.0/16'


environment = Environment(account=AWS_ACCOUNT, region=AWS_DEFAULT_REGION)

app = App()

vpc = Vpc(
    app,
    "Base",
    env=environment,
    cidr=CIDR
)

tag_stacks([vpc], 'dev', 'mane_Rshiny')

app.synth()
