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
    description="AmazonNimbleStudio",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AmazonNimbleStudio"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &lt;p&gt;Welcome to the Amazon Nimble Studio API reference. This API reference provides methods, schema, resources, parameters, and more to help you get the most out of Nimble Studio.&lt;/p&gt; &lt;p&gt;Nimble Studio is a virtual studio that empowers visual effects, animation, and interactive content teams to create content securely within a scalable, private cloud service.&lt;/p&gt;
    """
)

