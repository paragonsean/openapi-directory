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
    description="Amazon Simple Email Service",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Simple Email Service"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon SES API v2&lt;/fullname&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/ses\&quot;&gt;Amazon SES&lt;/a&gt; is an Amazon Web Services service that you can use to send email messages to your customers.&lt;/p&gt; &lt;p&gt;If you&#39;re new to Amazon SES API v2, you might find it helpful to review the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/\&quot;&gt;Amazon Simple Email Service Developer Guide&lt;/a&gt;. The &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt; provides information and code samples that demonstrate how to use Amazon SES API v2 features programmatically.&lt;/p&gt;
    """
)

