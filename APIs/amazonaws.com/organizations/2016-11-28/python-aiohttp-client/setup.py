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
    description="AWS Organizations",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Organizations"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Organizations is a web service that enables you to consolidate your multiple Amazon Web Services accounts into an &lt;i&gt;organization&lt;/i&gt; and centrally manage your accounts and their resources.&lt;/p&gt; &lt;p&gt;This guide provides descriptions of the Organizations operations. For more information about using this service, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html\&quot;&gt;Organizations User Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Support and feedback for Organizations&lt;/b&gt; &lt;/p&gt; &lt;p&gt;We welcome your feedback. Send your comments to &lt;a href&#x3D;\&quot;mailto:feedback-awsorganizations@amazon.com\&quot;&gt;feedback-awsorganizations@amazon.com&lt;/a&gt; or post your feedback and questions in the &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/forum.jspa?forumID&#x3D;219\&quot;&gt;Organizations support forum&lt;/a&gt;. For more information about the Amazon Web Services support forums, see &lt;a href&#x3D;\&quot;http://forums.aws.amazon.com/help.jspa\&quot;&gt;Forums Help&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Endpoint to call When using the CLI or the Amazon Web Services SDK&lt;/b&gt; &lt;/p&gt; &lt;p&gt;For the current release of Organizations, specify the &lt;code&gt;us-east-1&lt;/code&gt; region for all Amazon Web Services API and CLI calls made from the commercial Amazon Web Services Regions outside of China. If calling from one of the Amazon Web Services Regions in China, then specify &lt;code&gt;cn-northwest-1&lt;/code&gt;. You can do this in the CLI by using these parameters and commands:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Use the following parameter with each command to specify both the endpoint and its region:&lt;/p&gt; &lt;p&gt; &lt;code&gt;--endpoint-url https://organizations.us-east-1.amazonaws.com&lt;/code&gt; &lt;i&gt;(from commercial Amazon Web Services Regions outside of China)&lt;/i&gt; &lt;/p&gt; &lt;p&gt;or&lt;/p&gt; &lt;p&gt; &lt;code&gt;--endpoint-url https://organizations.cn-northwest-1.amazonaws.com.cn&lt;/code&gt; &lt;i&gt;(from Amazon Web Services Regions in China)&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the default endpoint, but configure your default region with this command:&lt;/p&gt; &lt;p&gt; &lt;code&gt;aws configure set default.region us-east-1&lt;/code&gt; &lt;i&gt;(from commercial Amazon Web Services Regions outside of China)&lt;/i&gt; &lt;/p&gt; &lt;p&gt;or&lt;/p&gt; &lt;p&gt; &lt;code&gt;aws configure set default.region cn-northwest-1&lt;/code&gt; &lt;i&gt;(from Amazon Web Services Regions in China)&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Use the following parameter with each command to specify the endpoint:&lt;/p&gt; &lt;p&gt; &lt;code&gt;--region us-east-1&lt;/code&gt; &lt;i&gt;(from commercial Amazon Web Services Regions outside of China)&lt;/i&gt; &lt;/p&gt; &lt;p&gt;or&lt;/p&gt; &lt;p&gt; &lt;code&gt;--region cn-northwest-1&lt;/code&gt; &lt;i&gt;(from Amazon Web Services Regions in China)&lt;/i&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; &lt;b&gt;Recording API Requests&lt;/b&gt; &lt;/p&gt; &lt;p&gt;Organizations supports CloudTrail, a service that records Amazon Web Services API calls for your Amazon Web Services account and delivers log files to an Amazon S3 bucket. By using information collected by CloudTrail, you can determine which requests the Organizations service received, who made the request and when, and so on. For more about Organizations and its support for CloudTrail, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/organizations/latest/userguide/orgs_incident-response.html#orgs_cloudtrail-integration\&quot;&gt;Logging Organizations Events with CloudTrail&lt;/a&gt; in the &lt;i&gt;Organizations User Guide&lt;/i&gt;. To learn more about CloudTrail, including how to turn it on and find your log files, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awscloudtrail/latest/userguide/what_is_cloud_trail_top_level.html\&quot;&gt;CloudTrail User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

