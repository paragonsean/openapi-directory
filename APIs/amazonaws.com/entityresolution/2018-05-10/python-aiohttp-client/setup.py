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
    description="AWS EntityResolution",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS EntityResolution"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the &lt;i&gt;AWS Entity Resolution API Reference&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;AWS Entity Resolution is an AWS service that provides pre-configured entity resolution capabilities that enable developers and analysts at advertising and marketing companies to build an accurate and complete view of their consumers.&lt;/p&gt; &lt;p&gt; With AWS Entity Resolution, you have the ability to match source records containing consumer identifiers, such as name, email address, and phone number. This holds true even when these records have incomplete or conflicting identifiers. For example, AWS Entity Resolution can effectively match a source record from a customer relationship management (CRM) system, which includes account information like first name, last name, postal address, phone number, and email address, with a source record from a marketing system containing campaign information, such as username and email address.&lt;/p&gt; &lt;p&gt;To learn more about AWS Entity Resolution concepts, procedures, and best practices, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/entityresolution/latest/userguide/what-is-service.html\&quot;&gt;AWS Entity Resolution User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

