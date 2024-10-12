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
    description="Amazon Pinpoint Email Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Pinpoint Email Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Pinpoint Email Service&lt;/fullname&gt; &lt;p&gt;Welcome to the &lt;i&gt;Amazon Pinpoint Email API Reference&lt;/i&gt;. This guide provides information about the Amazon Pinpoint Email API (version 1.0), including supported operations, data types, parameters, and schemas.&lt;/p&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;https://aws.amazon.com/pinpoint\&quot;&gt;Amazon Pinpoint&lt;/a&gt; is an AWS service that you can use to engage with your customers across multiple messaging channels. You can use Amazon Pinpoint to send email, SMS text messages, voice messages, and push notifications. The Amazon Pinpoint Email API provides programmatic access to options that are unique to the email channel and supplement the options provided by the Amazon Pinpoint API.&lt;/p&gt; &lt;p&gt;If you&#39;re new to Amazon Pinpoint, you might find it helpful to also review the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;. The &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt; provides tutorials, code samples, and procedures that demonstrate how to use Amazon Pinpoint features programmatically and how to integrate Amazon Pinpoint functionality into mobile apps and other types of applications. The guide also provides information about key topics such as Amazon Pinpoint integration with other AWS services and the limits that apply to using the service.&lt;/p&gt; &lt;p&gt;The Amazon Pinpoint Email API is available in several AWS Regions and it provides an endpoint for each of these Regions. For a list of all the Regions and endpoints where the API is currently available, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande.html#pinpoint_region\&quot;&gt;AWS Service Endpoints&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. To learn more about AWS Regions, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/general/latest/gr/rande-manage.html\&quot;&gt;Managing AWS Regions&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;In each Region, AWS maintains multiple Availability Zones. These Availability Zones are physically isolated from each other, but are united by private, low-latency, high-throughput, and highly redundant network connections. These Availability Zones enable us to provide very high levels of availability and redundancy, while also minimizing latency. To learn more about the number of Availability Zones that are available in each Region, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/about-aws/global-infrastructure/\&quot;&gt;AWS Global Infrastructure&lt;/a&gt;.&lt;/p&gt;
    """
)

