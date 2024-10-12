# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "openapi_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.14.1",
    "swagger-ui-bundle==0.0.9",
    "aiohttp_jinja2==1.5.0",
]

setup(
    name=NAME,
    version=VERSION,
    description="AWS Control Tower",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Control Tower"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;These interfaces allow you to apply the AWS library of pre-defined &lt;i&gt;controls&lt;/i&gt; to your organizational units, programmatically. In this context, controls are the same as AWS Control Tower guardrails.&lt;/p&gt; &lt;p&gt;To call these APIs, you&#39;ll need to know:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;the &lt;code&gt;ControlARN&lt;/code&gt; for the control--that is, the guardrail--you are targeting,&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;and the ARN associated with the target organizational unit (OU).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;To get the &lt;code&gt;ControlARN&lt;/code&gt; for your AWS Control Tower guardrail:&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The &lt;code&gt;ControlARN&lt;/code&gt; contains the control name which is specified in each guardrail. For a list of control names for &lt;i&gt;Strongly recommended&lt;/i&gt; and &lt;i&gt;Elective&lt;/i&gt; guardrails, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/control-identifiers.html.html\&quot;&gt;Resource identifiers for APIs and guardrails&lt;/a&gt; in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/automating-tasks.html\&quot;&gt;Automating tasks section&lt;/a&gt; of the AWS Control Tower User Guide. Remember that &lt;i&gt;Mandatory&lt;/i&gt; guardrails cannot be added or removed.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;ARN format:&lt;/b&gt; &lt;code&gt;arn:aws:controltower:{REGION}::control/{CONTROL_NAME}&lt;/code&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Example:&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:aws:controltower:us-west-2::control/AWS-GR_AUTOSCALING_LAUNCH_CONFIG_PUBLIC_IP_DISABLED&lt;/code&gt; &lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;To get the ARN for an OU:&lt;/b&gt; &lt;/p&gt; &lt;p&gt;In the AWS Organizations console, you can find the ARN for the OU on the &lt;b&gt;Organizational unit details&lt;/b&gt; page associated with that OU.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;b&gt;OU ARN format:&lt;/b&gt; &lt;/p&gt; &lt;p&gt; &lt;code&gt;arn:${Partition}:organizations::${MasterAccountId}:ou/o-${OrganizationId}/ou-${OrganizationalUnitId}&lt;/code&gt; &lt;/p&gt; &lt;/note&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Details and examples&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/control-identifiers.html\&quot;&gt;List of resource identifiers for APIs and guardrails&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/guardrail-api-examples-short.html\&quot;&gt;Guardrail API examples (CLI)&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/enable-controls.html\&quot;&gt;Enable controls with AWS CloudFormation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/creating-resources-with-cloudformation.html\&quot;&gt;Creating AWS Control Tower resources with AWS CloudFormation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To view the open source resource repository on GitHub, see &lt;a href&#x3D;\&quot;https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-controltower\&quot;&gt;aws-cloudformation/aws-cloudformation-resource-providers-controltower&lt;/a&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Recording API Requests&lt;/b&gt; &lt;/p&gt; &lt;p&gt;AWS Control Tower supports AWS CloudTrail, a service that records AWS API calls for your AWS account and delivers log files to an Amazon S3 bucket. By using information collected by CloudTrail, you can determine which requests the AWS Control Tower service received, who made the request and when, and so on. For more about AWS Control Tower and its support for CloudTrail, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/controltower/latest/userguide/logging-using-cloudtrail.html\&quot;&gt;Logging AWS Control Tower Actions with AWS CloudTrail&lt;/a&gt; in the AWS Control Tower User Guide. To learn more about CloudTrail, including how to turn it on and find your log files, see the AWS CloudTrail User Guide.&lt;/p&gt;
    """
)

