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
    description="Amazon Pinpoint SMS Voice V2",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Pinpoint SMS Voice V2"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the &lt;i&gt;Amazon Pinpoint SMS and Voice, version 2 API Reference&lt;/i&gt;. This guide provides information about Amazon Pinpoint SMS and Voice, version 2 API resources, including supported HTTP methods, parameters, and schemas.&lt;/p&gt; &lt;p&gt;Amazon Pinpoint is an Amazon Web Services service that you can use to engage with your recipients across multiple messaging channels. The Amazon Pinpoint SMS and Voice, version 2 API provides programmatic access to options that are unique to the SMS and voice channels and supplements the resources provided by the Amazon Pinpoint API.&lt;/p&gt; &lt;p&gt;If you&#39;re new to Amazon Pinpoint, it&#39;s also helpful to review the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/welcome.html\&quot;&gt; Amazon Pinpoint Developer Guide&lt;/a&gt;. The &lt;i&gt;Amazon Pinpoint Developer Guide&lt;/i&gt; provides tutorials, code samples, and procedures that demonstrate how to use Amazon Pinpoint features programmatically and how to integrate Amazon Pinpoint functionality into mobile apps and other types of applications. The guide also provides key information, such as Amazon Pinpoint integration with other Amazon Web Services services, and the quotas that apply to use of the service.&lt;/p&gt;
    """
)

