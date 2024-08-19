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
    description="AWS Application Discovery Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Application Discovery Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Web Services Application Discovery Service&lt;/fullname&gt; &lt;p&gt;Amazon Web Services Application Discovery Service (Application Discovery Service) helps you plan application migration projects. It automatically identifies servers, virtual machines (VMs), and network dependencies in your on-premises data centers. For more information, see the &lt;a href&#x3D;\&quot;http://aws.amazon.com/application-discovery/faqs/\&quot;&gt;Amazon Web Services Application Discovery Service FAQ&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;Application Discovery Service offers three ways of performing discovery and collecting data about your on-premises servers:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Agentless discovery&lt;/b&gt; using Amazon Web Services Application Discovery Service Agentless Collector (Agentless Collector), which doesn&#39;t require you to install an agent on each host.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Agentless Collector gathers server information regardless of the operating systems, which minimizes the time required for initial on-premises infrastructure assessment.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Agentless Collector doesn&#39;t collect information about network dependencies, only agent-based discovery collects that information. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Agent-based discovery&lt;/b&gt; using the Amazon Web Services Application Discovery Agent (Application Discovery Agent) collects a richer set of data than agentless discovery, which you install on one or more hosts in your data center.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; The agent captures infrastructure and application information, including an inventory of running processes, system performance information, resource utilization, and network dependencies.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The information collected by agents is secured at rest and in transit to the Application Discovery Service database in the Amazon Web Services cloud. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/discovery-agent.html\&quot;&gt;Amazon Web Services Application Discovery Agent&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Amazon Web Services Partner Network (APN) solutions&lt;/b&gt; integrate with Application Discovery Service, enabling you to import details of your on-premises environment directly into Amazon Web Services Migration Hub (Migration Hub) without using Agentless Collector or Application Discovery Agent.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Third-party application discovery tools can query Amazon Web Services Application Discovery Service, and they can write to the Application Discovery Service database using the public API.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;In this way, you can import data into Migration Hub and view it, so that you can associate applications with servers and track migrations.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Working With This Guide&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This API reference provides descriptions, syntax, and usage examples for each of the actions and data types for Application Discovery Service. The topic for each action shows the API request parameters and the response. Alternatively, you can use one of the Amazon Web Services SDKs to access an API that is tailored to the programming language or platform that you&#39;re using. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/tools/#SDKs\&quot;&gt;Amazon Web Services SDKs&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Remember that you must set your Migration Hub home Region before you call any of these APIs.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must make API calls for write actions (create, notify, associate, disassociate, import, or put) while in your home Region, or a &lt;code&gt;HomeRegionNotSetException&lt;/code&gt; error is returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;API calls for read actions (list, describe, stop, and delete) are permitted outside of your home Region.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Although it is unlikely, the Migration Hub home Region could change. If you call APIs outside the home Region, an &lt;code&gt;InvalidInputException&lt;/code&gt; is returned.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You must call &lt;code&gt;GetHomeRegion&lt;/code&gt; to obtain the latest Migration Hub home Region.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;This guide is intended for use with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/application-discovery/latest/userguide/\&quot;&gt;Amazon Web Services Application Discovery Service User Guide&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;All data is handled according to the &lt;a href&#x3D;\&quot;https://aws.amazon.com/privacy/\&quot;&gt;Amazon Web Services Privacy Policy&lt;/a&gt;. You can operate Application Discovery Service offline to inspect collected data before it is shared with the service.&lt;/p&gt; &lt;/important&gt;
    """
)

