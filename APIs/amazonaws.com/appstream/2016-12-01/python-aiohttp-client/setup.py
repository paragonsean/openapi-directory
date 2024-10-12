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
    description="Amazon AppStream",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon AppStream"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon AppStream 2.0&lt;/fullname&gt; &lt;p&gt;This is the &lt;i&gt;Amazon AppStream 2.0 API Reference&lt;/i&gt;. This documentation provides descriptions and syntax for each of the actions and data types in AppStream 2.0. AppStream 2.0 is a fully managed, secure application streaming service that lets you stream desktop applications to users without rewriting applications. AppStream 2.0 manages the AWS resources that are required to host and run your applications, scales automatically, and provides access to your users on demand. &lt;/p&gt; &lt;note&gt; &lt;p&gt;You can call the AppStream 2.0 API operations by using an interface VPC endpoint (interface endpoint). For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/appstream2/latest/developerguide/access-api-cli-through-interface-vpc-endpoint.html\&quot;&gt;Access AppStream 2.0 API Operations and CLI Commands Through an Interface VPC Endpoint&lt;/a&gt; in the &lt;i&gt;Amazon AppStream 2.0 Administration Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To learn more about AppStream 2.0, see the following resources:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/appstream2\&quot;&gt;Amazon AppStream 2.0 product page&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/documentation/appstream2\&quot;&gt;Amazon AppStream 2.0 documentation&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

