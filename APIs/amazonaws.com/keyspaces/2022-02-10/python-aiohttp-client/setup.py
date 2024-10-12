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
    description="Amazon Keyspaces",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Keyspaces"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra-compatible database service. Amazon Keyspaces makes it easy to migrate, run, and scale Cassandra workloads in the Amazon Web Services Cloud. With just a few clicks on the Amazon Web Services Management Console or a few lines of code, you can create keyspaces and tables in Amazon Keyspaces, without deploying any infrastructure or installing software. &lt;/p&gt; &lt;p&gt;In addition to supporting Cassandra Query Language (CQL) requests via open-source Cassandra drivers, Amazon Keyspaces supports data definition language (DDL) operations to manage keyspaces and tables using the Amazon Web Services SDK and CLI, as well as infrastructure as code (IaC) services and tools such as CloudFormation and Terraform. This API reference describes the supported DDL operations in detail.&lt;/p&gt; &lt;p&gt;For the list of all supported CQL APIs, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/cassandra-apis.html\&quot;&gt;Supported Cassandra APIs, operations, and data types in Amazon Keyspaces&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To learn how Amazon Keyspaces API actions are recorded with CloudTrail, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/keyspaces/latest/devguide/logging-using-cloudtrail.html#service-name-info-in-cloudtrail\&quot;&gt;Amazon Keyspaces information in CloudTrail&lt;/a&gt; in the &lt;i&gt;Amazon Keyspaces Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For more information about Amazon Web Services APIs, for example how to implement retry logic or how to sign Amazon Web Services API requests, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-apis.html\&quot;&gt;Amazon Web Services APIs&lt;/a&gt; in the &lt;i&gt;General Reference&lt;/i&gt;.&lt;/p&gt;
    """
)

