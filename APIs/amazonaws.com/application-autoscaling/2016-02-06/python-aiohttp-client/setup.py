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
    description="Application Auto Scaling",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Application Auto Scaling"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;With Application Auto Scaling, you can configure automatic scaling for the following resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon AppStream 2.0 fleets&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Aurora Replicas&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Comprehend document classification and entity recognizer endpoints&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon DynamoDB tables and global secondary indexes throughput capacity&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon ECS services&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon ElastiCache for Redis clusters (replication groups)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon EMR clusters&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Keyspaces (for Apache Cassandra) tables&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Lambda function provisioned concurrency&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Managed Streaming for Apache Kafka broker storage&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon Neptune clusters&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SageMaker endpoint variants&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon SageMaker Serverless endpoint provisioned concurrency&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Spot Fleets (Amazon EC2)&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Custom resources provided by your own applications or services&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To learn more about Application Auto Scaling, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html\&quot;&gt;Application Auto Scaling User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;API Summary&lt;/b&gt; &lt;/p&gt; &lt;p&gt;The Application Auto Scaling service API includes three key sets of actions: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Register and manage scalable targets - Register Amazon Web Services or custom resources as scalable targets (a resource that Application Auto Scaling can scale), set minimum and maximum capacity limits, and retrieve information on existing scalable targets.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Configure and manage automatic scaling - Define scaling policies to dynamically scale your resources in response to CloudWatch alarms, schedule one-time or recurring scaling actions, and retrieve your recent scaling activity history.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Suspend and resume scaling - Temporarily suspend and later resume automatic scaling by calling the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html\&quot;&gt;RegisterScalableTarget&lt;/a&gt; API action for any Application Auto Scaling scalable target. You can suspend and resume (individually or in combination) scale-out activities that are triggered by a scaling policy, scale-in activities that are triggered by a scaling policy, and scheduled scaling.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

