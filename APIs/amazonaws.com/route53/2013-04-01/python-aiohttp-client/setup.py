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
    description="Amazon Route 53",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Route 53"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service.&lt;/p&gt; &lt;p&gt;You can use Route 53 to:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Register domain names.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-domain-registration.html\&quot;&gt;How domain registration works&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Route internet traffic to the resources for your domain&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html\&quot;&gt;How internet traffic is routed to your website or web application&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Check the health of your resources.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-health-checks.html\&quot;&gt;How Route 53 checks the health of your resources&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

