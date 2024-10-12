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
    description="AWS Global Accelerator",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Global Accelerator"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Global Accelerator&lt;/fullname&gt; &lt;p&gt;This is the &lt;i&gt;Global Accelerator API Reference&lt;/i&gt;. This guide is for developers who need detailed information about Global Accelerator API actions, data types, and errors. For more information about Global Accelerator features, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html\&quot;&gt;Global Accelerator Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Global Accelerator is a service in which you create &lt;i&gt;accelerators&lt;/i&gt; to improve the performance of your applications for local and global users. Depending on the type of accelerator you choose, you can gain additional benefits. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;By using a standard accelerator, you can improve availability of your internet applications that are used by a global audience. With a standard accelerator, Global Accelerator directs traffic to optimal endpoints over the Amazon Web Services global network. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For other scenarios, you might choose a custom routing accelerator. With a custom routing accelerator, you can use application logic to directly map one or more users to a specific endpoint among many endpoints.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;important&gt; &lt;p&gt;Global Accelerator is a global service that supports endpoints in multiple Amazon Web Services Regions but you must specify the US West (Oregon) Region to create, update, or otherwise work with accelerators. That is, for example, specify &lt;code&gt;--region us-west-2&lt;/code&gt; on AWS CLI commands.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;By default, Global Accelerator provides you with static IP addresses that you associate with your accelerator. The static IP addresses are anycast from the Amazon Web Services edge network. For IPv4, Global Accelerator provides two static IPv4 addresses. For dual-stack, Global Accelerator provides a total of four addresses: two static IPv4 addresses and two static IPv6 addresses. With a standard accelerator for IPv4, instead of using the addresses that Global Accelerator provides, you can configure these entry points to be IPv4 addresses from your own IP address ranges that you bring toGlobal Accelerator (BYOIP). &lt;/p&gt; &lt;p&gt;For a standard accelerator, they distribute incoming application traffic across multiple endpoint resources in multiple Amazon Web Services Regions , which increases the availability of your applications. Endpoints for standard accelerators can be Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic IP addresses that are located in one Amazon Web Services Region or multiple Amazon Web Services Regions. For custom routing accelerators, you map traffic that arrives to the static IP addresses to specific Amazon EC2 servers in endpoints that are virtual private cloud (VPC) subnets.&lt;/p&gt; &lt;important&gt; &lt;p&gt;The static IP addresses remain assigned to your accelerator for as long as it exists, even if you disable the accelerator and it no longer accepts or routes traffic. However, when you &lt;i&gt;delete&lt;/i&gt; an accelerator, you lose the static IP addresses that are assigned to it, so you can no longer route traffic by using them. You can use IAM policies like tag-based permissions with Global Accelerator to limit the users who have permissions to delete an accelerator. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/access-control-manage-access-tag-policies.html\&quot;&gt;Tag-based policies&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For standard accelerators, Global Accelerator uses the Amazon Web Services global network to route traffic to the optimal regional endpoint based on health, client location, and policies that you configure. The service reacts instantly to changes in health or configuration to ensure that internet traffic from clients is always directed to healthy endpoints.&lt;/p&gt; &lt;p&gt;For more information about understanding and using Global Accelerator, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html\&quot;&gt;Global Accelerator Developer Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

