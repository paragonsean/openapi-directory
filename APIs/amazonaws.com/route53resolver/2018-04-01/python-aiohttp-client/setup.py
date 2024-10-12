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
    description="Amazon Route 53 Resolver",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Route 53 Resolver"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;When you create a VPC using Amazon VPC, you automatically get DNS resolution within the VPC from Route 53 Resolver. By default, Resolver answers DNS queries for VPC domain names such as domain names for EC2 instances or Elastic Load Balancing load balancers. Resolver performs recursive lookups against public name servers for all other domain names.&lt;/p&gt; &lt;p&gt;You can also configure DNS resolution between your VPC and your network over a Direct Connect or VPN connection:&lt;/p&gt; &lt;p&gt; &lt;b&gt;Forward DNS queries from resolvers on your network to Route 53 Resolver&lt;/b&gt; &lt;/p&gt; &lt;p&gt;DNS resolvers on your network can forward DNS queries to Resolver in a specified VPC. This allows your DNS resolvers to easily resolve domain names for Amazon Web Services resources such as EC2 instances or records in a Route 53 private hosted zone. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-network-to-vpc\&quot;&gt;How DNS Resolvers on Your Network Forward DNS Queries to Route 53 Resolver&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Conditionally forward queries from a VPC to resolvers on your network&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can configure Resolver to forward queries that it receives from EC2 instances in your VPCs to DNS resolvers on your network. To forward selected queries, you create Resolver rules that specify the domain names for the DNS queries that you want to forward (such as example.com), and the IP addresses of the DNS resolvers on your network that you want to forward the queries to. If a query matches multiple rules (example.com, acme.example.com), Resolver chooses the rule with the most specific match (acme.example.com) and forwards the query to the IP addresses that you specified in that rule. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-vpc-to-network\&quot;&gt;How Route 53 Resolver Forwards DNS Queries from Your VPCs to Your Network&lt;/a&gt; in the &lt;i&gt;Amazon Route 53 Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Like Amazon VPC, Resolver is Regional. In each Region where you have VPCs, you can choose whether to forward queries from your VPCs to your network (outbound queries), from your network to your VPCs (inbound queries), or both.&lt;/p&gt;
    """
)

