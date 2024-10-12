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
    description="AWS Health APIs and Notifications",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Health APIs and Notifications"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Health&lt;/fullname&gt; &lt;p&gt;The Health API provides access to the Health information that appears in the &lt;a href&#x3D;\&quot;https://health.aws.amazon.com/health/home\&quot;&gt;Health Dashboard&lt;/a&gt;. You can use the API operations to get information about events that might affect your Amazon Web Services and resources.&lt;/p&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan from &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt; to use the Health API. If you call the Health API from an Amazon Web Services account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, you receive a &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error.&lt;/p&gt; &lt;p&gt;For API access, you need an access key ID and a secret access key. Use temporary credentials instead of long-term access keys when possible. Temporary credentials include an access key ID, a secret access key, and a security token that indicates when the credentials expire. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/aws-access-keys-best-practices.html\&quot;&gt;Best practices for managing Amazon Web Services access keys&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can use the Health endpoint health.us-east-1.amazonaws.com (HTTPS) to call the Health API operations. Health supports a multi-Region application architecture and has two regional endpoints in an active-passive configuration. You can use the high availability endpoint example to determine which Amazon Web Services Region is active, so that you can get the latest information from the API. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/health-api.html\&quot;&gt;Accessing the Health API&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For authentication of requests, Health uses the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 Signing Process&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;If your Amazon Web Services account is part of Organizations, you can use the Health organizational view feature. This feature provides a centralized view of Health events across all accounts in your organization. You can aggregate Health events in real time to identify accounts in your organization that are affected by an operational event or get notified of security vulnerabilities. Use the organizational view API operations to enable this feature and return event information. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/ug/aggregate-events.html\&quot;&gt;Aggregating Health events&lt;/a&gt; in the &lt;i&gt;Health User Guide&lt;/i&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;When you use the Health API operations to return Health events, see the following recommendations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html#AWSHealth-Type-Event-eventScopeCode\&quot;&gt;eventScopeCode&lt;/a&gt; parameter to specify whether to return Health events that are public or account-specific.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use pagination to view all events from the response. For example, if you call the &lt;code&gt;DescribeEventsForOrganization&lt;/code&gt; operation to get all events in your organization, you might receive several page results. Specify the &lt;code&gt;nextToken&lt;/code&gt; in the next request to return more results.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt;
    """
)

