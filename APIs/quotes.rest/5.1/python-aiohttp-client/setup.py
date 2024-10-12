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
    description="They Said So Quotes API",
    author_email="",
    url="",
    keywords=["OpenAPI", "They Said So Quotes API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
     They Said So Quotes API offers a complete feature rich REST API access to its quotes platform.  This is the documentation for the world famous [quotes API](https://theysaidso.com/api).  If you are a subscriber and you are trying this from a console you can use Bearer token with your api key as the token. You can test and play with the API right here on this web page. Please note recently we closed downs public access without api key to prevent abuse. The public routes are still available to use free of charge but requires a api token. You can get one for free at our website. For using the private end points and subscribing to the API please visit [https://theysaidso.com/api](https://theysaidso.com/api).
    """
)

