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
    description="trash nothing",
    author_email="",
    url="",
    keywords=["OpenAPI", "trash nothing"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is the REST API for [trashnothing.com](https://trashnothing.com).  To learn more about the API or to register your app for use with the API visit the [trash nothing Developer page](https://trashnothing.com/developer).  NOTE: All date-time values are [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) and are in [ISO 8601 format](https://en.wikipedia.org/wiki/ISO_8601) (eg. 2019-02-03T01:23:53). 
    """
)

