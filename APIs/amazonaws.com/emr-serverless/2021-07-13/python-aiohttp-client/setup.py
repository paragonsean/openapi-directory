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
    description="EMR Serverless",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "EMR Serverless"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon EMR Serverless is a new deployment option for Amazon EMR. Amazon EMR Serverless provides a serverless runtime environment that simplifies running analytics applications using the latest open source frameworks such as Apache Spark and Apache Hive. With Amazon EMR Serverless, you don’t have to configure, optimize, secure, or operate clusters to run applications with these frameworks.&lt;/p&gt; &lt;p&gt;The API reference to Amazon EMR Serverless is &lt;code&gt;emr-serverless&lt;/code&gt;. The &lt;code&gt;emr-serverless&lt;/code&gt; prefix is used in the following scenarios: &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;It is the prefix in the CLI commands for Amazon EMR Serverless. For example, &lt;code&gt;aws emr-serverless start-job-run&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;It is the prefix before IAM policy actions for Amazon EMR Serverless. For example, &lt;code&gt;\&quot;Action\&quot;: [\&quot;emr-serverless:StartJobRun\&quot;]&lt;/code&gt;. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-actions\&quot;&gt;Policy actions for Amazon EMR Serverless&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;It is the prefix used in Amazon EMR Serverless service endpoints. For example, &lt;code&gt;emr-serverless.us-east-2.amazonaws.com&lt;/code&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

