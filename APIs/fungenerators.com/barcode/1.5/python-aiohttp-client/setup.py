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
    description="Barcode API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Barcode API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Generate Barcode images for a given barcode number. You can decode Barcode images and get the barcodes in a numberic form as well. Many industry standard barcode types are supported. The best and complete Barcode API on the cloud. [Click here to subscribe](http://fungenerators.com/api/barcode/)  
    """
)

