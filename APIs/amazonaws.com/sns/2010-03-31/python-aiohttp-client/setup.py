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
    description="Amazon Simple Notification Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Simple Notification Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Simple Notification Service&lt;/fullname&gt; &lt;p&gt;Amazon Simple Notification Service (Amazon SNS) is a web service that enables you to build distributed web-enabled applications. Applications can use Amazon SNS to easily push real-time notification messages to interested subscribers over multiple delivery protocols. For more information about this product see the &lt;a href&#x3D;\&quot;http://aws.amazon.com/sns/\&quot;&gt;Amazon SNS product page&lt;/a&gt;. For detailed information about Amazon SNS features and their associated API calls, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/\&quot;&gt;Amazon SNS Developer Guide&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;For information on the permissions you need to use this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sns/latest/dg/sns-authentication-and-access-control.html\&quot;&gt;Identity and access management in Amazon SNS&lt;/a&gt; in the &lt;i&gt;Amazon SNS Developer Guide.&lt;/i&gt; &lt;/p&gt; &lt;p&gt;We also provide SDKs that enable you to access Amazon SNS from your preferred programming language. The SDKs contain functionality that automatically takes care of tasks such as: cryptographically signing your service requests, retrying requests, and handling error responses. For a list of available SDKs, go to &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/\&quot;&gt;Tools for Amazon Web Services&lt;/a&gt;. &lt;/p&gt;
    """
)

