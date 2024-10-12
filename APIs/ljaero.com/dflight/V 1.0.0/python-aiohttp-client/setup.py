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
    description="DFlight API",
    author_email="",
    url="",
    keywords=["OpenAPI", "DFlight API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    [DFlight API](https://ljaero.com/solutions/dflight/) supplies the up-to-date information needed for compliance with UAV preflight assessment requirements. Separate endpoints are available for each of the following information categories: - Airspace - Weather - Temporary Flight Restrictions - Special Security Areas - Restricted Public Venues - Surface Obstacles - Aerodromes - UAS Operating Areas  You can define your geographic area of interest in one of three convenient ways: - Providing a latitude/longitude point and distance around that point - Providing a GeoJSON LineString defining your route - Providing an arbitrary GeoJSON Polygon defining your area of interest
    """
)

