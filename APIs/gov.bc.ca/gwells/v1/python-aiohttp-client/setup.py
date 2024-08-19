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
    description="Groundwater Wells, Aquifers and Registry API",
    author_email="groundwater@gov.bc.ca",
    url="",
    keywords=["OpenAPI", "Groundwater Wells, Aquifers and Registry API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The groundwater wells, aquifers and registry API contains information related to groundwater wells and aquifers as well as a register of qualified well drillers and well pump installers registered to operate in B.C.
    """
)

