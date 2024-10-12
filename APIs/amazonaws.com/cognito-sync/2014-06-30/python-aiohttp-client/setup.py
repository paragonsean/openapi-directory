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
    description="Amazon Cognito Sync",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Cognito Sync"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Cognito Sync&lt;/fullname&gt; &lt;p&gt;Amazon Cognito Sync provides an AWS service and client library that enable cross-device syncing of application-related user data. High-level client libraries are available for both iOS and Android. You can use these libraries to persist data locally so that it&#39;s available even if the device is offline. Developer credentials don&#39;t need to be stored on the mobile device to access the service. You can use Amazon Cognito to obtain a normalized user ID and credentials. User data is persisted in a dataset that can store up to 1 MB of key-value pairs, and you can have up to 20 datasets per user identity.&lt;/p&gt; &lt;p&gt;With Amazon Cognito Sync, the data stored for each identity is accessible only to credentials assigned to that identity. In order to use the Cognito Sync service, you need to make API calls using credentials retrieved with &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html\&quot;&gt;Amazon Cognito Identity service&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If you want to use Cognito Sync in an Android or iOS application, you will probably want to make API calls via the AWS Mobile SDK. To learn more, see the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/cognito-sync.html\&quot;&gt;Developer Guide for Android&lt;/a&gt; and the &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/mobile/sdkforios/developerguide/cognito-sync.html\&quot;&gt;Developer Guide for iOS&lt;/a&gt;.&lt;/p&gt;
    """
)

