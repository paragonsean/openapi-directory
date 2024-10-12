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
    description="AWS Single Sign-On Admin",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Single Sign-On Admin"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;AWS IAM Identity Center (successor to AWS Single Sign-On) helps you securely create, or connect, your workforce identities and manage their access centrally across AWS accounts and applications. IAM Identity Center is the recommended approach for workforce authentication and authorization in AWS, for organizations of any size and type.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Although AWS Single Sign-On was renamed, the &lt;code&gt;sso&lt;/code&gt; and &lt;code&gt;identitystore&lt;/code&gt; API namespaces will continue to retain their original name for backward compatibility purposes. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html#renamed\&quot;&gt;IAM Identity Center rename&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This reference guide provides information on single sign-on operations which could be used for access management of AWS accounts. For information about IAM Identity Center features, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html\&quot;&gt;IAM Identity Center User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Many operations in the IAM Identity Center APIs rely on identifiers for users and groups, known as principals. For more information about how to work with principals and principal IDs in IAM Identity Center, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html\&quot;&gt;Identity Store API Reference&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;AWS provides SDKs that consist of libraries and sample code for various programming languages and platforms (Java, Ruby, .Net, iOS, Android, and more). The SDKs provide a convenient way to create programmatic access to IAM Identity Center and other AWS services. For more information about the AWS SDKs, including how to download and install them, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/\&quot;&gt;Tools for Amazon Web Services&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;
    """
)

