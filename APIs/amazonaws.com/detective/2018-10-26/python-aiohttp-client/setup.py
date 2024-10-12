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
    description="Amazon Detective",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Detective"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Detective uses machine learning and purpose-built visualizations to help you to analyze and investigate security issues across your Amazon Web Services (Amazon Web Services) workloads. Detective automatically extracts time-based events such as login attempts, API calls, and network traffic from CloudTrail and Amazon Virtual Private Cloud (Amazon VPC) flow logs. It also extracts findings detected by Amazon GuardDuty.&lt;/p&gt; &lt;p&gt;The Detective API primarily supports the creation and management of behavior graphs. A behavior graph contains the extracted data from a set of member accounts, and is created and managed by an administrator account.&lt;/p&gt; &lt;p&gt;To add a member account to the behavior graph, the administrator account sends an invitation to the account. When the account accepts the invitation, it becomes a member account in the behavior graph.&lt;/p&gt; &lt;p&gt;Detective is also integrated with Organizations. The organization management account designates the Detective administrator account for the organization. That account becomes the administrator account for the organization behavior graph. The Detective administrator account is also the delegated administrator account for Detective in Organizations.&lt;/p&gt; &lt;p&gt;The Detective administrator account can enable any organization account as a member account in the organization behavior graph. The organization accounts do not receive invitations. The Detective administrator account can also invite other accounts to the organization behavior graph.&lt;/p&gt; &lt;p&gt;Every behavior graph is specific to a Region. You can only use the API to manage behavior graphs that belong to the Region that is associated with the currently selected endpoint.&lt;/p&gt; &lt;p&gt;The administrator account for a behavior graph can use the Detective API to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Enable and disable Detective. Enabling Detective creates a new behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;View the list of member accounts in a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Add member accounts to a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Remove member accounts from a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Apply tags to a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The organization management account can use the Detective API to select the delegated administrator for Detective.&lt;/p&gt; &lt;p&gt;The Detective administrator account for an organization can use the Detective API to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Perform all of the functions of an administrator account.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Determine whether to automatically enable new organization accounts as member accounts in the organization behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;An invited member account can use the Detective API to do the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;View the list of behavior graphs that they are invited to.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Accept an invitation to contribute to a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Decline an invitation to contribute to a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Remove their account from a behavior graph.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;All API actions are logged as CloudTrail events. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/detective/latest/adminguide/logging-using-cloudtrail.html\&quot;&gt;Logging Detective API Calls with CloudTrail&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;We replaced the term \&quot;master account\&quot; with the term \&quot;administrator account.\&quot; An administrator account is used to centrally manage multiple accounts. In the case of Detective, the administrator account manages the accounts in their behavior graph.&lt;/p&gt; &lt;/note&gt;
    """
)

