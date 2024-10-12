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
    description="AWS Amplify UI Builder",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Amplify UI Builder"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;The Amplify UI Builder API provides a programmatic interface for creating and configuring user interface (UI) component libraries and themes for use in your Amplify applications. You can then connect these UI components to an application&#39;s backend Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;You can also use the Amplify Studio visual designer to create UI components and model data for an app. For more information, see &lt;a href&#x3D;\&quot;https://docs.amplify.aws/console/adminui/intro\&quot;&gt;Introduction&lt;/a&gt; in the &lt;i&gt;Amplify Docs&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;The Amplify Framework is a comprehensive set of SDKs, libraries, tools, and documentation for client app development. For more information, see the &lt;a href&#x3D;\&quot;https://docs.amplify.aws/\&quot;&gt;Amplify Framework&lt;/a&gt;. For more information about deploying an Amplify application to Amazon Web Services, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html\&quot;&gt;Amplify User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

