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
    description="Bets API",
    author_email="platform@williamhill.com",
    url="",
    keywords=["OpenAPI", "Bets API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Bets API methods are used to place single, multiple and complex bets and to retrieve a customer’s bet history. When retrieving a customer’s bet history you can organize the bets from the betting history in terms of date, bet type and whether the bet is settled or not. You can also specify what fields to be included/excluded or return a list of all default fields the method returns. &lt;br /&gt;&lt;br /&gt; The Bets API will also generate a bet delay if you’re placing a single/multiple bet in-Play by creating a time margin to negate the effects of major changes to the market (for example, goals during a football match). Note that in version 2 of our APIs, Bets API contains the functionality of both Bets API v1 and the Betslips API v1.
    """
)

