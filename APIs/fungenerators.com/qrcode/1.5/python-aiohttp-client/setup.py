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
    description="Fun Generators API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Fun Generators API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Fungenerators API gives access to the full set of generators available at fungenerators.com so that you can integrate them in your workflow or an app. [Click here to get details and subscribe](http://fungenerators.com/api) . Here are the individual API links:    ## QR Code API ##   Generate QR Code images for text, url, email , business cards etc. You can decode QR Code images and get the contents as well. The best and complete QR Code API on the cloud. [Click here to subscribe](http://fungenerators.com/api/qrcode) 
    """
)

