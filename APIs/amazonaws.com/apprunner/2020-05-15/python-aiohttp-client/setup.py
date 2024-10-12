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
    description="AWS App Runner",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS App Runner"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;App Runner&lt;/fullname&gt; &lt;p&gt;App Runner is an application service that provides a fast, simple, and cost-effective way to go directly from an existing container image or source code to a running service in the Amazon Web Services Cloud in seconds. You don&#39;t need to learn new technologies, decide which compute service to use, or understand how to provision and configure Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;App Runner connects directly to your container registry or source code repository. It provides an automatic delivery pipeline with fully managed operations, high performance, scalability, and security.&lt;/p&gt; &lt;p&gt;For more information about App Runner, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apprunner/latest/dg/\&quot;&gt;App Runner Developer Guide&lt;/a&gt;. For release information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/apprunner/latest/relnotes/\&quot;&gt;App Runner Release Notes&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; To install the Software Development Kits (SDKs), Integrated Development Environment (IDE) Toolkits, and command line tools that you can use to access the API, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/\&quot;&gt;Tools for Amazon Web Services&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Endpoints&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For a list of Region-specific endpoints that App Runner supports, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/apprunner.html\&quot;&gt;App Runner endpoints and quotas&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt;
    """
)

