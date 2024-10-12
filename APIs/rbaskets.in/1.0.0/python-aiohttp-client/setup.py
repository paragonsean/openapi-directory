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
    description="Request Baskets API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Request Baskets API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    RESTful API of [Request Baskets](https://rbaskets.in) service.  Request Baskets is an open source project of a service to collect HTTP requests and inspect them via RESTful API or web UI.  Check out the [project page](https://github.com/darklynx/request-baskets) for more detailed description. 
    """
)

