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
    description="Weatherbit - Interactive Swagger UI Documentation",
    author_email="",
    url="",
    keywords=["OpenAPI", "Weatherbit - Interactive Swagger UI Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This an interactive version of the documentation for the Weatherbit API.  The base URL for the API is [http://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/) or [https://api.weatherbit.io/v2.0/](http://api.weatherbit.io/v2.0/). Below is the Swagger UI documentation for the API. All API requests require the &#x60;key&#x60; parameter.        An Example for a 48 hour forecast for London, UK would be &#x60;http://api.weatherbit.io/v2.0/forecast/hourly?lat&#x3D;51.5072&#x60;&amp;&#x60;lon&#x3D;-0.1276&#x60;. See our [Weather API description page](https://www.weatherbit.io/api) for the full documentation.
    """
)

