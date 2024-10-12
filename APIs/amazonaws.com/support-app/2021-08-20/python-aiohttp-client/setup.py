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
    description="AWS Support App",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Support App"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;&lt;fullname&gt;Amazon Web Services Support App in Slack&lt;/fullname&gt; &lt;p&gt;You can use the Amazon Web Services Support App in Slack API to manage your support cases in Slack for your Amazon Web Services account. After you configure your Slack workspace and channel with the Amazon Web Services Support App, you can perform the following tasks directly in your Slack channel:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Create, search, update, and resolve your support cases&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Request service quota increases for your account&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Invite Amazon Web Services Support agents to your channel so that you can chat directly about your support cases&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For more information about how to perform these actions in Slack, see the following documentation in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/aws-support-app-for-slack.html\&quot;&gt;Amazon Web Services Support App in Slack&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/joining-a-live-chat-session.html\&quot;&gt;Joining a live chat session with Amazon Web Services Support&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/service-quota-increase.html\&quot;&gt;Requesting service quota increases&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/support-app-commands.html\&quot;&gt;Amazon Web Services Support App commands in Slack&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can also use the Amazon Web Services Management Console instead of the Amazon Web Services Support App API to manage your Slack configurations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html\&quot;&gt;Authorize a Slack workspace to enable the Amazon Web Services Support App&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business or Enterprise Support plan to use the Amazon Web Services Support App API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;For more information about the Amazon Web Services Support App endpoints, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/awssupport.html#awssupport_app_region\&quot;&gt;Amazon Web Services Support App in Slack endpoints&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;&lt;/p&gt;
    """
)

