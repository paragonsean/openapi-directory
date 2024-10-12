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
    description="Amazon Cognito Identity Provider",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Cognito Identity Provider"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;With the Amazon Cognito user pools API, you can set up user pools and app clients, and authenticate users. To authenticate users from third-party identity providers (IdPs) in this API, you can &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html\&quot;&gt;link IdP users to native user profiles&lt;/a&gt;. Learn more about the authentication and authorization of federated users in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-userpools-server-contract-reference.html\&quot;&gt;Using the Amazon Cognito user pools API and user pool endpoints&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This API reference provides detailed information about API operations and object types in Amazon Cognito. At the bottom of the page for each API operation and object, under &lt;i&gt;See Also&lt;/i&gt;, you can learn how to use it in an Amazon Web Services SDK in the language of your choice.&lt;/p&gt; &lt;p&gt;Along with resource management operations, the Amazon Cognito user pools API includes classes of operations and authorization models for client-side and server-side user operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/user-pools-API-operations.html\&quot;&gt;Using the Amazon Cognito native and OIDC APIs&lt;/a&gt; in the &lt;i&gt;Amazon Cognito Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can also start reading about the &lt;code&gt;CognitoIdentityProvider&lt;/code&gt; client in the following SDK guides.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cli/latest/reference/cognito-idp/index.html#cli-aws-cognito-idp\&quot;&gt;Amazon Web Services Command Line Interface&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CognitoIdentityProvider/TCognitoIdentityProviderClient.html\&quot;&gt;Amazon Web Services SDK for .NET&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://sdk.amazonaws.com/cpp/api/LATEST/aws-cpp-sdk-cognito-idp/html/class_aws_1_1_cognito_identity_provider_1_1_cognito_identity_provider_client.html\&quot;&gt;Amazon Web Services SDK for C++&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sdk-for-go/api/service/cognitoidentityprovider/#CognitoIdentityProvider\&quot;&gt;Amazon Web Services SDK for Go&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/cognitoidentityprovider/CognitoIdentityProviderClient.html\&quot;&gt;Amazon Web Services SDK for Java V2&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/CognitoIdentityServiceProvider.html\&quot;&gt;Amazon Web Services SDK for JavaScript&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/aws-sdk-php/v3/api/api-cognito-idp-2016-04-18.html\&quot;&gt;Amazon Web Services SDK for PHP V3&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cognito-idp.html\&quot;&gt;Amazon Web Services SDK for Python&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/CognitoIdentityProvider/Client.html\&quot;&gt;Amazon Web Services SDK for Ruby V3&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To get started with an Amazon Web Services SDK, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/developer/tools/\&quot;&gt;Tools to Build on Amazon Web Services&lt;/a&gt;. For example actions and scenarios, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cognito/latest/developerguide/service_code_examples_cognito-identity-provider.html\&quot;&gt;Code examples for Amazon Cognito Identity Provider using Amazon Web Services SDKs&lt;/a&gt;.&lt;/p&gt;
    """
)

