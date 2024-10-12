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
    description="Mobility API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Mobility API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Transit API can be used to obtain time-aggregated data representing moving the people between various spatial points within the Czech Republic. Having A - &#39;from&#39; and B - &#39;to&#39; points, the API can return count of people traveling from A to B or people that are from A and traveling to B, etc. The mobility data is based on moving mobile stations in O2 mobile network.
    """
)

