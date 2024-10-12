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
    description="AWS Support",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Support"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Web Services Support&lt;/fullname&gt; &lt;p&gt;The &lt;i&gt;Amazon Web Services Support API Reference&lt;/i&gt; is intended for programmers who need detailed information about the Amazon Web Services Support operations and data types. You can use the API to manage your support cases programmatically. The Amazon Web Services Support API uses HTTP methods that return results in JSON format.&lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If you call the Amazon Web Services Support API from an account that doesn&#39;t have a Business, Enterprise On-Ramp, or Enterprise Support plan, the &lt;code&gt;SubscriptionRequiredException&lt;/code&gt; error message appears. For information about changing your support plan, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/\&quot;&gt;Amazon Web Services Support&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; &lt;p&gt;You can also use the Amazon Web Services Support API to access features for &lt;a href&#x3D;\&quot;http://aws.amazon.com/premiumsupport/trustedadvisor/\&quot;&gt;Trusted Advisor&lt;/a&gt;. You can return a list of checks and their descriptions, get check results, specify checks to refresh, and get the refresh status of checks.&lt;/p&gt; &lt;p&gt;You can manage your support cases with the following Amazon Web Services Support API operations:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;a&gt;CreateCase&lt;/a&gt;, &lt;a&gt;DescribeCases&lt;/a&gt;, &lt;a&gt;DescribeAttachment&lt;/a&gt;, and &lt;a&gt;ResolveCase&lt;/a&gt; operations create Amazon Web Services Support cases, retrieve information about cases, and resolve cases.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;a&gt;DescribeCommunications&lt;/a&gt;, &lt;a&gt;AddCommunicationToCase&lt;/a&gt;, and &lt;a&gt;AddAttachmentsToSet&lt;/a&gt; operations retrieve and add communications and attachments to Amazon Web Services Support cases.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;a&gt;DescribeServices&lt;/a&gt; and &lt;a&gt;DescribeSeverityLevels&lt;/a&gt; operations return Amazon Web Service names, service codes, service categories, and problem severity levels. You use these values when you call the &lt;a&gt;CreateCase&lt;/a&gt; operation.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;You can also use the Amazon Web Services Support API to call the Trusted Advisor operations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/\&quot;&gt;Trusted Advisor&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;For authentication of requests, Amazon Web Services Support uses &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html\&quot;&gt;Signature Version 4 Signing Process&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For more information about this service and the endpoints to use, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html\&quot;&gt;About the Amazon Web Services Support API&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Support User Guide&lt;/i&gt;.&lt;/p&gt;
    """
)

