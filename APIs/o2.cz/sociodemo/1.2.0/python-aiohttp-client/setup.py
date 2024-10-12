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
    description="Socio-demo API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Socio-demo API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Socio-demo API can be used to obtain time-aggregated data representing groups of people on the given location in the Czech Republic. Having a location, the API can return count of people belonging to age group or gender aggregated by hours. The socio-demo data is based on presence of mobile stations in O2 mobile network.
    """
)

