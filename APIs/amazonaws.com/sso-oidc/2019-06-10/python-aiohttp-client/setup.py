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
    description="AWS SSO OIDC",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS SSO OIDC"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;AWS IAM Identity Center (successor to AWS Single Sign-On) OpenID Connect (OIDC) is a web service that enables a client (such as AWS CLI or a native application) to register with IAM Identity Center. The service also enables the client to fetch the user’s access token upon successful authentication and authorization with IAM Identity Center.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Although AWS Single Sign-On was renamed, the &lt;code&gt;sso&lt;/code&gt; and &lt;code&gt;identitystore&lt;/code&gt; API namespaces will continue to retain their original name for backward compatibility purposes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html#renamed\&quot;&gt;IAM Identity Center rename&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt; &lt;b&gt;Considerations for Using This Guide&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Before you begin using this guide, we recommend that you first review the following important information about how the IAM Identity Center OIDC service works.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The IAM Identity Center OIDC service currently implements only the portions of the OAuth 2.0 Device Authorization Grant standard (&lt;a href&#x3D;\&quot;https://tools.ietf.org/html/rfc8628\&quot;&gt;https://tools.ietf.org/html/rfc8628&lt;/a&gt;) that are necessary to enable single sign-on authentication with the AWS CLI. Support for other OIDC flows frequently needed for native applications, such as Authorization Code Flow (+ PKCE), will be addressed in future releases.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The service emits only OIDC access tokens, such that obtaining a new token (For example, token refresh) requires explicit user re-authentication.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The access tokens provided by this service grant access to all AWS account entitlements assigned to an IAM Identity Center user, not just a particular application.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The documentation in this guide does not describe the mechanism to convert the access token into AWS Auth (“sigv4”) credentials for use with IAM-protected AWS service endpoints. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/PortalAPIReference/API_GetRoleCredentials.html\&quot;&gt;GetRoleCredentials&lt;/a&gt; in the &lt;i&gt;IAM Identity Center Portal API Reference Guide&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For general information about IAM Identity Center, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html\&quot;&gt;What is IAM Identity Center?&lt;/a&gt; in the &lt;i&gt;IAM Identity Center User Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

