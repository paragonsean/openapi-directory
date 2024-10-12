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
    description="Paramedical Council, Madhya Pradesh",
    author_email="",
    url="",
    keywords=["OpenAPI", "Paramedical Council, Madhya Pradesh"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Registration Certificate, Duplicate Registration Certificate, Good Standing Certificate, Registration Renewal, Tatkal Registration, Tatkal  Registration Renewal and Upadhi/Certificate as issued by MP Paramedical Council (http://www.mppmc.ac.in) from April 2017 onwards can be pulled into citizens&#39; DigiLocker accounts.
    """
)

