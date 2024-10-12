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
    description="United India Insurance Company Limited",
    author_email="",
    url="",
    keywords=["OpenAPI", "United India Insurance Company Limited"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    United India Insurance Co. Ltd. is a Public Sector General Insurance Company incorporated in 1938, having its presence all over India providing risk cover to 1.74 Crore policyholders. General Insurance Policies such as Motor, Health, Personal Accident, Travel, e.t.c issued by United India Insurance Co. Ltd. (https://uiic.co.in/) are available to be downloaded by citizens of India to their DigiLocker account.
    """
)

