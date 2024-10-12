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
    description="Goa Water Resources Department, Goa",
    author_email="",
    url="",
    keywords=["OpenAPI", "Goa Water Resources Department, Goa"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Goa WRD (https://goawrd.gov.in/) is the official departmental portal of the Water Resources Department, Govt. of Goa, through which citizens can avail time bound service being offered by the department. Certificates issued by it (e.g. Contractor Enlistment, Well Registration etc) are made available in citizens&#39; DigiLocker accounts.
    """
)

