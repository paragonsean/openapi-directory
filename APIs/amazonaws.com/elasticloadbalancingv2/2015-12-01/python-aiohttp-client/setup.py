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
    &lt;fullname&gt;Elastic Load Balancing&lt;/fullname&gt; &lt;p&gt;A load balancer distributes incoming traffic across targets, such as your EC2 instances. This enables you to increase the availability of your application. The load balancer also monitors the health of its registered targets and ensures that it routes traffic only to healthy targets. You configure your load balancer to accept incoming traffic by specifying one or more listeners, which are configured with a protocol and port number for connections from clients to the load balancer. You configure a target group with a protocol and port number for connections from the load balancer to the targets, and with health check settings to be used when checking the health status of the targets.&lt;/p&gt; &lt;p&gt;Elastic Load Balancing supports the following types of load balancers: Application Load Balancers, Network Load Balancers, Gateway Load Balancers, and Classic Load Balancers. This reference covers the following load balancer types:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Application Load Balancer - Operates at the application layer (layer 7) and supports HTTP and HTTPS.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Network Load Balancer - Operates at the transport layer (layer 4) and supports TCP, TLS, and UDP.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Gateway Load Balancer - Operates at the network layer (layer 3).&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/\&quot;&gt;Elastic Load Balancing User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;All Elastic Load Balancing operations are idempotent, which means that they complete at most one time. If you repeat an operation, it succeeds.&lt;/p&gt;
    """
)

