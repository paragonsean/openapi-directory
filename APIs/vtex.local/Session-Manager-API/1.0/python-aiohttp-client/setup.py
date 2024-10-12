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
    description="Session Manager API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Session Manager API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This documentation goes in detail how to interact with Session Manager&#39;s API. For a more top-level approach, check the [design documentation](https://help.vtex.com/tutorial/using-session-manager-to-track-browsing-sessions-in-vtex-stores--1pA0tqsD4BFnJYhQ7ORQBd).
    """
)

