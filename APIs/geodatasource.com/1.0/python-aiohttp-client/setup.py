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
    description="GeoDataSource Location Search",
    author_email="",
    url="",
    keywords=["OpenAPI", "GeoDataSource Location Search"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    GeoDataSource™ Web Service is a REST API enable user to lookup for a city by using latitude and longitude coordinate. It will return the result in either JSON or XML containing the information of country, region, city, latitude and longitude. Visit https://www.geodatasource.com/web-service for further information.
    """
)

