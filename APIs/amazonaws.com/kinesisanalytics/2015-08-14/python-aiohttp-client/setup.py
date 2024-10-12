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
    description="Amazon Kinesis Analytics",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Kinesis Analytics"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Kinesis Analytics&lt;/fullname&gt; &lt;p&gt; &lt;b&gt;Overview&lt;/b&gt; &lt;/p&gt; &lt;note&gt; &lt;p&gt;This documentation is for version 1 of the Amazon Kinesis Data Analytics API, which only supports SQL applications. Version 2 of the API supports SQL and Java applications. For more information about version 2, see &lt;a href&#x3D;\&quot;/kinesisanalytics/latest/apiv2/Welcome.html\&quot;&gt;Amazon Kinesis Data Analytics API V2 Documentation&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;This is the &lt;i&gt;Amazon Kinesis Analytics v1 API Reference&lt;/i&gt;. The Amazon Kinesis Analytics Developer Guide provides additional information. &lt;/p&gt;
    """
)

