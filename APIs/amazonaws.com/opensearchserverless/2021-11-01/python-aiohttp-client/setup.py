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
    description="OpenSearch Service Serverless",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "OpenSearch Service Serverless"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Use the Amazon OpenSearch Serverless API to create, configure, and manage OpenSearch Serverless collections and security policies.&lt;/p&gt; &lt;p&gt;OpenSearch Serverless is an on-demand, pre-provisioned serverless configuration for Amazon OpenSearch Service. OpenSearch Serverless removes the operational complexities of provisioning, configuring, and tuning your OpenSearch clusters. It enables you to easily search and analyze petabytes of data without having to worry about the underlying infrastructure and data management.&lt;/p&gt; &lt;p&gt; To learn more about OpenSearch Serverless, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-overview.html\&quot;&gt;What is Amazon OpenSearch Serverless?&lt;/a&gt; &lt;/p&gt;
    """
)

