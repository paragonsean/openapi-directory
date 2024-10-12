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
    description="Amazon EventBridge",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon EventBridge"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon EventBridge helps you to respond to state changes in your Amazon Web Services resources. When your resources change state, they automatically send events to an event stream. You can create rules that match selected events in the stream and route them to targets to take action. You can also use rules to take action on a predetermined schedule. For example, you can configure rules to:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Automatically invoke an Lambda function to update DNS entries when an event notifies you that Amazon EC2 instance enters the running state.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Direct specific API records from CloudTrail to an Amazon Kinesis data stream for detailed analysis of potential security or availability risks.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Periodically invoke a built-in target to create a snapshot of an Amazon EBS volume.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about the features of Amazon EventBridge, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/eventbridge/latest/userguide\&quot;&gt;Amazon EventBridge User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

