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
    description="nFusion Solutions Market Data API",
    author_email="support@nfusionsolutions.com",
    url="",
    keywords=["OpenAPI", "nFusion Solutions Market Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    [nFusion Solutions](https://nfusionsolutions.com) provides [REST APIs](https://nfusionsolutions.com/data-feeds/) that deliver enterprise-grade financial data. Data sets include real-time and historical pricing for Spot prices of precious metals such as Gold, Silver, Platinum, and Palladium, exchange rates for major currency pairs, exchange rates for Crypto Currencies such as BTC, ETH, and LTC. All API access requires authentication. In order to be issued access credentials you must first enter into a service agreement with nFusion Solutions and acquire a commercial license. For information on how to obtain a licence [take a tour of our products](https://nfusionsolutions.com/nfusion-solutions-metals-gold-price-feed-tour/) or email sales@nfusionsolutions.com.
    """
)

