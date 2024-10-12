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
    description="Daymet Single Pixel Extraction Tool API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Daymet Single Pixel Extraction Tool API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Welcome to the Daymet Single Pixel Extraction Tool API. You can use this API to download daily surface data within the Daymet database in a &#x60;csv&#x60; or &#x60;json&#x60; format for a single point. This API allows users to query a single geographic point by latitude and longitude in decimal degrees. A routine is executed that translates the (lon, lat) coordinates into projected Daymet (x,y) Lambert Conformal Coordinates. These coordinates are used to access the Daymet database of daily interpolated surface weather variables. Daily data from the nearest 1 km x 1 km Daymet grid cell are extracted from the database.  If you would like to learn how to automate the download of multiple locations for the Daymet Single Pixel Extraction Tool, click [here](https://github.com/ornldaac/daymet-single-pixel-batch).
    """
)

