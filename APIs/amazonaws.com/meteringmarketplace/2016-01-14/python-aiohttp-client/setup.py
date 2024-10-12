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
    description="AWSMarketplace Metering",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWSMarketplace Metering"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;AWS Marketplace Metering Service&lt;/fullname&gt; &lt;p&gt;This reference provides descriptions of the low-level AWS Marketplace Metering Service API.&lt;/p&gt; &lt;p&gt;AWS Marketplace sellers can use this API to submit usage data for custom usage dimensions.&lt;/p&gt; &lt;p&gt;For information on the permissions you need to use this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace/latest/userguide/iam-user-policy-for-aws-marketplace-actions.html\&quot;&gt;AWS Marketplace metering and entitlement API permissions&lt;/a&gt; in the &lt;i&gt;AWS Marketplace Seller Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt; &lt;b&gt;Submitting Metering Records&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;MeterUsage&lt;/i&gt; - Submits the metering record for an AWS Marketplace product. &lt;code&gt;MeterUsage&lt;/code&gt; is called from an EC2 instance or a container running on EKS or ECS.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;BatchMeterUsage&lt;/i&gt; - Submits the metering record for a set of customers. &lt;code&gt;BatchMeterUsage&lt;/code&gt; is called from a software-as-a-service (SaaS) application.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Accepting New Customers&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;ResolveCustomer&lt;/i&gt; - Called by a SaaS application during the registration process. When a buyer visits your website during the registration process, the buyer submits a Registration Token through the browser. The Registration Token is resolved through this API to obtain a &lt;code&gt;CustomerIdentifier&lt;/code&gt; along with the &lt;code&gt;CustomerAWSAccountId&lt;/code&gt; and &lt;code&gt;ProductCode&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Entitlement and Metering for Paid Container Products&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Paid container software products sold through AWS Marketplace must integrate with the AWS Marketplace Metering Service and call the &lt;code&gt;RegisterUsage&lt;/code&gt; operation for software entitlement and metering. Free and BYOL products for Amazon ECS or Amazon EKS aren&#39;t required to call &lt;code&gt;RegisterUsage&lt;/code&gt;, but you can do so if you want to receive usage data in your seller reports. For more information on using the &lt;code&gt;RegisterUsage&lt;/code&gt; operation, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/marketplace/latest/userguide/container-based-products.html\&quot;&gt;Container-Based Products&lt;/a&gt;. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;code&gt;BatchMeterUsage&lt;/code&gt; API calls are captured by AWS CloudTrail. You can use Cloudtrail to verify that the SaaS metering records that you sent are accurate by searching for records with the &lt;code&gt;eventName&lt;/code&gt; of &lt;code&gt;BatchMeterUsage&lt;/code&gt;. You can also use CloudTrail to audit records over time. For more information, see the &lt;i&gt; &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html\&quot;&gt;AWS CloudTrail User Guide&lt;/a&gt;.&lt;/i&gt; &lt;/p&gt;
    """
)

