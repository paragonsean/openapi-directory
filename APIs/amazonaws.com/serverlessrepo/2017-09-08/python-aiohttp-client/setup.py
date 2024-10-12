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
    description="AWSServerlessApplicationRepository",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWSServerlessApplicationRepository"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;The AWS Serverless Application Repository makes it easy for developers and enterprises to quickly find  and deploy serverless applications in the AWS Cloud. For more information about serverless applications,  see Serverless Computing and Applications on the AWS website.&lt;/p&gt;&lt;p&gt;The AWS Serverless Application Repository is deeply integrated with the AWS Lambda console, so that developers of   all levels can get started with serverless computing without needing to learn anything new. You can use category   keywords to browse for applications such as web and mobile backends, data processing applications, or chatbots.   You can also search for applications by name, publisher, or event source. To use an application, you simply choose it,   configure any required fields, and deploy it with a few clicks. &lt;/p&gt;&lt;p&gt;You can also easily publish applications, sharing them publicly with the community at large, or privately  within your team or across your organization. To publish a serverless application (or app), you can use the  AWS Management Console, AWS Command Line Interface (AWS CLI), or AWS SDKs to upload the code. Along with the  code, you upload a simple manifest file, also known as the AWS Serverless Application Model (AWS SAM) template.  For more information about AWS SAM, see AWS Serverless Application Model (AWS SAM) on the AWS Labs  GitHub repository.&lt;/p&gt;&lt;p&gt;The AWS Serverless Application Repository Developer Guide contains more information about the two developer  experiences available:&lt;/p&gt;&lt;ul&gt;  &lt;li&gt;  &lt;p&gt;Consuming Applications – Browse for applications and view information about them, including  source code and readme files. Also install, configure, and deploy applications of your choosing. &lt;/p&gt;  &lt;p&gt;Publishing Applications – Configure and upload applications to make them available to other  developers, and publish new versions of applications. &lt;/p&gt;  &lt;/li&gt;  &lt;/ul&gt;
    """
)

