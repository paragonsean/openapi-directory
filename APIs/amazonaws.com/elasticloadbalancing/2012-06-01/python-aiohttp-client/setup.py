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
    description="Elastic Load Balancing",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Elastic Load Balancing"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Elastic Load Balancing&lt;/fullname&gt; &lt;p&gt;A load balancer can distribute incoming traffic across your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered instances and ensures that it routes traffic only to healthy instances. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer and a protocol and port number for connections from the load balancer to the instances.&lt;/p&gt; &lt;p&gt;Elastic Load Balancing supports three types of load balancers: Application Load Balancers, Network Load Balancers, and Classic Load Balancers. You can select a load balancer based on your application needs. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/\&quot;&gt;Elastic Load Balancing User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This reference covers the 2012-06-01 API, which supports Classic Load Balancers. The 2015-12-01 API supports Application Load Balancers and Network Load Balancers.&lt;/p&gt; &lt;p&gt;To get started, create a load balancer with one or more listeners using &lt;a&gt;CreateLoadBalancer&lt;/a&gt;. Register your instances with the load balancer using &lt;a&gt;RegisterInstancesWithLoadBalancer&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;All Elastic Load Balancing operations are &lt;i&gt;idempotent&lt;/i&gt;, which means that they complete at most one time. If you repeat an operation, it succeeds with a 200 OK response code.&lt;/p&gt;
    """
)

