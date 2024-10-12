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
    description="Amazon Simple Queue Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Simple Queue Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the &lt;i&gt;Amazon SQS API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Amazon SQS is a reliable, highly-scalable hosted queue for storing messages as they travel between applications or microservices. Amazon SQS moves data between distributed application components and helps you decouple these components.&lt;/p&gt; &lt;p&gt;For information on the permissions you need to use this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-authentication-and-access-control.html\&quot;&gt;Identity and access management&lt;/a&gt; in the &lt;i&gt;Amazon SQS Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;You can use &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/#sdk\&quot;&gt;Amazon Web Services SDKs&lt;/a&gt; to access Amazon SQS using your favorite programming language. The SDKs perform tasks such as the following automatically:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Cryptographically sign your service requests&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Retry requests&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Handle error responses&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Additional information&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/sqs/\&quot;&gt;Amazon SQS Product Page&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Amazon SQS Developer Guide&lt;/i&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-making-api-requests.html\&quot;&gt;Making API Requests&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-message-metadata.html#sqs-message-attributes\&quot;&gt;Amazon SQS Message Attributes&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html\&quot;&gt;Amazon SQS Dead-Letter Queues&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cli/latest/reference/sqs/index.html\&quot;&gt;Amazon SQS in the &lt;i&gt;Command Line Interface&lt;/i&gt; &lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande.html#sqs_region\&quot;&gt;Regions and Endpoints&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

