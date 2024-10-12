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
    description="AWS Service Catalog",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWS Service Catalog"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;fullname&gt;Service Catalog&lt;/fullname&gt; &lt;p&gt; &lt;a href&#x3D;\&quot;http://aws.amazon.com/servicecatalog\&quot;&gt;Service Catalog&lt;/a&gt; enables organizations to create and manage catalogs of IT services that are approved for Amazon Web Services. To get the most out of this documentation, you should be familiar with the terminology discussed in &lt;a href&#x3D;\&quot;http://docs.aws.amazon.com/servicecatalog/latest/adminguide/what-is_concepts.html\&quot;&gt;Service Catalog Concepts&lt;/a&gt;.&lt;/p&gt;
    """
)

