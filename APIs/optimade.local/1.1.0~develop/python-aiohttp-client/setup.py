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
    description="OPTIMADE API",
    author_email="",
    url="",
    keywords=["OpenAPI", "OPTIMADE API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The [Open Databases Integration for Materials Design (OPTIMADE) consortium](https://www.optimade.org/) aims to make materials databases interoperational by developing a common REST API.  This specification is generated using [&#x60;optimade-python-tools&#x60;](https://github.com/Materials-Consortia/optimade-python-tools/tree/v0.16.0) v0.16.0.
    """
)

