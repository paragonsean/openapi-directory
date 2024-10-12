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
    description="Routing",
    author_email="",
    url="",
    keywords=["OpenAPI", "Routing"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Routing consists of the following service: &lt;b&gt;Calculate Route&lt;/b&gt; Calculates a route between an origin and a destination, passing through waypoints (if specified). Additional routing parameters like traffic, avoidance conditions, departure/arrival time etc. can be taken into account. &lt;b&gt;Calculate Reachable Range&lt;/b&gt; Calculates a set of locations that can be reached from the origin point, subject to the available fuel or energy budget that is specified in the request.
    """
)

