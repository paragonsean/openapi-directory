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
    description="Active Documentation for /v1",
    author_email="",
    url="",
    keywords=["OpenAPI", "Active Documentation for /v1"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Our active docs provide the ability to test out your account and to see the responses to your queries. The services are RESTful, and are accessed using standard HTTP methods over a secure HTTPS channel. Requests and responses are currently sent in JSON format, and have a base URL of /v1.
    """
)

