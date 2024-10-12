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
    description="Logistics API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Logistics API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
        &gt;Check the [Fulfillment onboarding guide](https://developers.vtex.com/docs/guides/fulfillment). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about fulfillment and is organized by focusing on the developer&#39;s journey.    Logistics or fulfillment is the module responsible for shipping calculation and inventory management.     The variable &#x60;{{environment}}&#x60; can be filled with &#x60;vtexcommercestable&#x60; or &#x60;vtexcommercebeta&#x60;, depending on the environment you want to test.
    """
)

