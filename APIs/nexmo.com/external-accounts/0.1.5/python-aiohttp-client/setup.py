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
    description="External Accounts API",
    author_email="devrel@vonage.com",
    url="",
    keywords=["OpenAPI", "External Accounts API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The External Accounts API is used to manage accounts for Viber Business Messages, Facebook Messenger and Whatsapp for use in the [Messages](https://developer.nexmo.com/messages/overview) and [Dispatch](https://developer.nexmo.com/dispatch/overview) APIs.
    """
)

