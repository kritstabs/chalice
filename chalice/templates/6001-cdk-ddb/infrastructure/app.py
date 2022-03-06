#!/usr/bin/env python3
import aws_cdk as cdk
from stacks.chaliceapp import ChaliceApp

app = cdk.App()
ChaliceApp(app, '{{app_name}}')

app.synth()
