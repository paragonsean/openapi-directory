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
    description="Amazon CloudDirectory",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon CloudDirectory"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Cloud Directory&lt;/fullname&gt; &lt;p&gt;Amazon Cloud Directory is a component of the AWS Directory Service that simplifies the development and management of cloud-scale web, mobile, and IoT applications. This guide describes the Cloud Directory operations that you can call programmatically and includes detailed information on data types and errors. For information about Cloud Directory features, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/directoryservice/\&quot;&gt;AWS Directory Service&lt;/a&gt; and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/clouddirectory/latest/developerguide/what_is_cloud_directory.html\&quot;&gt;Amazon Cloud Directory Developer Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

