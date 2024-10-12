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
    description="AWS CloudTrail",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS CloudTrail"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;CloudTrail&lt;/fullname&gt; &lt;p&gt;This is the CloudTrail API Reference. It provides descriptions of actions, data types, common parameters, and common errors for CloudTrail.&lt;/p&gt; &lt;p&gt;CloudTrail is a web service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. The recorded information includes the identity of the user, the start time of the Amazon Web Services API call, the source IP address, the request parameters, and the response elements returned by the service.&lt;/p&gt; &lt;note&gt; &lt;p&gt;As an alternative to the API, you can use one of the Amazon Web Services SDKs, which consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .NET, iOS, Android, etc.). The SDKs provide programmatic access to CloudTrail. For example, the SDKs handle cryptographically signing requests, managing errors, and retrying requests automatically. For more information about the Amazon Web Services SDKs, including how to download and install them, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/\&quot;&gt;Tools to Build on Amazon Web Services&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;See the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html\&quot;&gt;CloudTrail User Guide&lt;/a&gt; for information about the data that is included with each Amazon Web Services API call listed in the log files.&lt;/p&gt;
    """
)

