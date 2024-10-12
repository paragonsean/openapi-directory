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
    description="Gisgraphy webservices",
    author_email="",
    url="",
    keywords=["OpenAPI", "Gisgraphy webservices"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Since 2006, [Gisgraphy](http://www.gisgraphy.com) is a free, open source framework that offers the possibility to do geolocalisation and geocoding via Java APIs or REST webservices. Because geocoding is nothing without data, it provides an easy to use importer that will automatically download and import the necessary (free) data to your local database ([OpenStreetMap](http://www.openstreetmap.org/), [Geonames](http://www.geonames.org/) and [Quattroshapes](http://www.quattroshapes.com/): more than 100 million entries). You can also add your own data with the Web interface or the importer connectors provided. Gisgraphy is production ready, and has been designed to be scalable(load balanced), performant and used in other languages than just java : results can be output in XML, JSON, PHP, Python, Ruby, YAML, GeoRSS, and Atom. One of the most popular GPS tracking System (OpenGTS) also includes a Gisgraphy client...Gisgraphy is a framework. As a result it&#39;s flexible and powerful enough to be used in a lot of different use cases. [read more](http://www.gisgraphy.com)   if you use the premium servers, you can use the api key to test the webservices 
    """
)

