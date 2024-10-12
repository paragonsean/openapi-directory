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
    description="AWS Step Functions",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Step Functions"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Step Functions&lt;/fullname&gt; &lt;p&gt;Step Functions is a service that lets you coordinate the components of distributed applications and microservices using visual workflows.&lt;/p&gt; &lt;p&gt;You can use Step Functions to build applications from individual components, each of which performs a discrete function, or &lt;i&gt;task&lt;/i&gt;, allowing you to scale and change applications quickly. Step Functions provides a console that helps visualize the components of your application as a series of steps. Step Functions automatically triggers and tracks each step, and retries steps when there are errors, so your application executes predictably and in the right order every time. Step Functions logs the state of each step, so you can quickly diagnose and debug any issues.&lt;/p&gt; &lt;p&gt;Step Functions manages operations and underlying infrastructure to ensure your application is available at any scale. You can run tasks on Amazon Web Services, your own servers, or any system that has access to Amazon Web Services. You can access and use Step Functions using the console, the Amazon Web Services SDKs, or an HTTP API. For more information about Step Functions, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html\&quot;&gt;Step Functions Developer Guide&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt;
    """
)

