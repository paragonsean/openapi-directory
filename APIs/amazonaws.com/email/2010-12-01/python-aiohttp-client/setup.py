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
    &lt;fullname&gt;Amazon Simple Email Service&lt;/fullname&gt; &lt;p&gt; This document contains reference information for the &lt;a href&#x3D;\&quot;https://aws.amazon.com/ses/\&quot;&gt;Amazon Simple Email Service&lt;/a&gt; (Amazon SES) API, version 2010-12-01. This document is best used in conjunction with the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;p&gt; For a list of Amazon SES endpoints to use in service requests, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/regions.html\&quot;&gt;Regions and Amazon SES&lt;/a&gt; in the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/Welcome.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;
    """
)

