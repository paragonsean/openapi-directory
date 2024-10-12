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
    description="Amazon Redshift",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Redshift"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Redshift&lt;/fullname&gt; &lt;p&gt; &lt;b&gt;Overview&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This is an interface reference for Amazon Redshift. It contains documentation for one of the programming or command line interfaces you can use to manage Amazon Redshift clusters. Note that Amazon Redshift is asynchronous, which means that some interfaces may require techniques, such as polling or asynchronous callback handlers, to determine when a command has been applied. In this reference, the parameter descriptions indicate whether a change is applied immediately, on the next instance reboot, or during the next maintenance window. For a summary of the Amazon Redshift cluster management interfaces, go to &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/mgmt/using-aws-sdk.html\&quot;&gt;Using the Amazon Redshift Management Interfaces&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Amazon Redshift manages all the work of setting up, operating, and scaling a data warehouse: provisioning capacity, monitoring and backing up the cluster, and applying patches and upgrades to the Amazon Redshift engine. You can focus on using your data to acquire new insights for your business and customers.&lt;/p&gt; &lt;p&gt;If you are a first-time user of Amazon Redshift, we recommend that you begin by reading the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html\&quot;&gt;Amazon Redshift Getting Started Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you are a database developer, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/redshift/latest/dg/welcome.html\&quot;&gt;Amazon Redshift Database Developer Guide&lt;/a&gt; explains how to design, build, query, and maintain the databases that make up your data warehouse. &lt;/p&gt;
    """
)

