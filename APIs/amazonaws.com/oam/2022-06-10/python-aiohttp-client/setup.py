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
    description="CloudWatch Observability Access Manager",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "CloudWatch Observability Access Manager"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Use Amazon CloudWatch Observability Access Manager to create and manage links between source accounts and monitoring accounts by using &lt;i&gt;CloudWatch cross-account observability&lt;/i&gt;. With CloudWatch cross-account observability, you can monitor and troubleshoot applications that span multiple accounts within a Region. Seamlessly search, visualize, and analyze your metrics, logs, and traces in any of the linked accounts without account boundaries.&lt;/p&gt; &lt;pre&gt;&lt;code&gt; &amp;lt;p&amp;gt;Set up one or more Amazon Web Services accounts as &amp;lt;i&amp;gt;monitoring accounts&amp;lt;/i&amp;gt; and link them with multiple &amp;lt;i&amp;gt;source accounts&amp;lt;/i&amp;gt;. A monitoring account is a central Amazon Web Services account that can view and interact with observability data generated from source accounts. A source account is an individual Amazon Web Services account that generates observability data for the resources that reside in it. Source accounts share their observability data with the monitoring account. The shared observability data can include metrics in Amazon CloudWatch, logs in Amazon CloudWatch Logs, and traces in X-Ray.&amp;lt;/p&amp;gt; &lt;/code&gt;&lt;/pre&gt;
    """
)

