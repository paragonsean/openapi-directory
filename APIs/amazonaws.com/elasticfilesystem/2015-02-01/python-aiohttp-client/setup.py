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
    description="Amazon Elastic File System",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "Amazon Elastic File System"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Amazon Elastic File System&lt;/fullname&gt; &lt;p&gt;Amazon Elastic File System (Amazon EFS) provides simple, scalable file storage for use with Amazon EC2 Linux and Mac instances in the Amazon Web Services Cloud. With Amazon EFS, storage capacity is elastic, growing and shrinking automatically as you add and remove files, so that your applications have the storage they need, when they need it. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/api-reference.html\&quot;&gt;Amazon Elastic File System API Reference&lt;/a&gt; and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html\&quot;&gt;Amazon Elastic File System User Guide&lt;/a&gt;.&lt;/p&gt;
    """
)

