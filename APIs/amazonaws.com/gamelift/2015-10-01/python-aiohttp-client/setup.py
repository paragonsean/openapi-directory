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
    description="Amazon GameLift",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon GameLift"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Amazon GameLift provides solutions for hosting session-based multiplayer game servers in the cloud, including tools for deploying, operating, and scaling game servers. Built on Amazon Web Services global computing infrastructure, GameLift helps you deliver high-performance, high-reliability, low-cost game servers while dynamically scaling your resource usage to meet player demand. &lt;/p&gt; &lt;p&gt; &lt;b&gt;About Amazon GameLift solutions&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Get more information on these Amazon GameLift solutions in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/\&quot;&gt;Amazon GameLift Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Amazon GameLift managed hosting -- Amazon GameLift offers a fully managed service to set up and maintain computing machines for hosting, manage game session and player session life cycle, and handle security, storage, and performance tracking. You can use automatic scaling tools to balance player demand and hosting costs, configure your game session management to minimize player latency, and add FlexMatch for matchmaking.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Managed hosting with Realtime Servers -- With Amazon GameLift Realtime Servers, you can quickly configure and set up ready-to-go game servers for your game. Realtime Servers provides a game server framework with core Amazon GameLift infrastructure already built in. Then use the full range of Amazon GameLift managed hosting features, including FlexMatch, for your game.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon GameLift FleetIQ -- Use Amazon GameLift FleetIQ as a standalone service while hosting your games using EC2 instances and Auto Scaling groups. Amazon GameLift FleetIQ provides optimizations for game hosting, including boosting the viability of low-cost Spot Instances gaming. For a complete solution, pair the Amazon GameLift FleetIQ and FlexMatch standalone services.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Amazon GameLift FlexMatch -- Add matchmaking to your game hosting solution. FlexMatch is a customizable matchmaking service for multiplayer games. Use FlexMatch as integrated with Amazon GameLift managed hosting or incorporate FlexMatch as a standalone service into your own hosting solution.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;About this API Reference&lt;/b&gt; &lt;/p&gt; &lt;p&gt;This reference guide describes the low-level service API for Amazon GameLift. With each topic in this guide, you can find links to language-specific SDK guides and the Amazon Web Services CLI reference. Useful links:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html\&quot;&gt;Amazon GameLift API operations listed by tasks&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-components.html\&quot;&gt; Amazon GameLift tools and resources&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;
    """
)

