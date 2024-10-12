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
    description="AWS DataSync",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS DataSync"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;DataSync&lt;/fullname&gt; &lt;p&gt;DataSync is an online data movement and discovery service that simplifies data migration and helps you quickly, easily, and securely transfer your file or object data to, from, and between Amazon Web Services storage services.&lt;/p&gt; &lt;p&gt;This API interface reference includes documentation for using DataSync programmatically. For complete information, see the &lt;i&gt; &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/datasync/latest/userguide/what-is-datasync.html\&quot;&gt;DataSync User Guide&lt;/a&gt; &lt;/i&gt;.&lt;/p&gt;
    """
)

