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
    description="Amazon Cognito Identity",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Cognito Identity"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Cognito Federated Identities&lt;/fullname&gt; &lt;p&gt;Amazon Cognito Federated Identities is a web service that delivers scoped temporary credentials to mobile devices and other untrusted environments. It uniquely identifies a device and supplies the user with a consistent identity over the lifetime of an application.&lt;/p&gt; &lt;p&gt;Using Amazon Cognito Federated Identities, you can enable authentication with one or more third-party identity providers (Facebook, Google, or Login with Amazon) or an Amazon Cognito user pool, and you can also choose to support unauthenticated access from your app. Cognito delivers a unique identifier for each user and acts as an OpenID token provider trusted by AWS Security Token Service (STS) to access temporary, limited-privilege AWS credentials.&lt;/p&gt; &lt;p&gt;For a description of the authentication flow from the Amazon Cognito Developer Guide see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flow.html\&quot;&gt;Authentication Flow&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-identity.html\&quot;&gt;Amazon Cognito Federated Identities&lt;/a&gt;.&lt;/p&gt;
    """
)

