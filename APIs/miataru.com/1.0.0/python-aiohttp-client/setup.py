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
    description="Miataru",
    author_email="info@miataru.com",
    url="",
    keywords=["OpenAPI", "Miataru"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Miataru API is very simple and straight forward. Generally you&#39;re posting (HTTP POST) a JSON formatted request to a service method locations and you get back a JSON formatted answer. Please take into consideration that this has the request-for-comment status and that it can change while there&#39;s work done on client and server applications. Versioning therefore is done by prepending the version number - /v1/ for version 1 - to the method call.
    """
)

