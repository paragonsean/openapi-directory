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
    description="AWS CloudFormation",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS CloudFormation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;CloudFormation&lt;/fullname&gt; &lt;p&gt;CloudFormation allows you to create and manage Amazon Web Services infrastructure deployments predictably and repeatedly. You can use CloudFormation to leverage Amazon Web Services products, such as Amazon Elastic Compute Cloud, Amazon Elastic Block Store, Amazon Simple Notification Service, Elastic Load Balancing, and Auto Scaling to build highly reliable, highly scalable, cost-effective applications without creating or configuring the underlying Amazon Web Services infrastructure.&lt;/p&gt; &lt;p&gt;With CloudFormation, you declare all your resources and dependencies in a template file. The template defines a collection of resources as a single unit called a stack. CloudFormation creates and deletes all member resources of the stack together and manages all dependencies between the resources for you.&lt;/p&gt; &lt;p&gt;For more information about CloudFormation, see the &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudformation/\&quot;&gt;CloudFormation product page&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;CloudFormation makes use of other Amazon Web Services products. If you need additional technical information about a specific Amazon Web Services product, you can find the product&#39;s technical documentation at &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/\&quot;&gt;docs.aws.amazon.com&lt;/a&gt;.&lt;/p&gt;
    """
)

