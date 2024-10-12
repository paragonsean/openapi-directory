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
    description="Tata AIA Life Insurance Co. Ltd.",
    author_email="",
    url="",
    keywords=["OpenAPI", "Tata AIA Life Insurance Co. Ltd."],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Tata AIA Life Insurance Company Limited provides life insurance solutions to its consumers. Customers can access their policy details [Insurance Policy � Life] and premium receipts [Premium Receipt] that are available to be pulled by the policy holders into their DigiLocker account (only documents issued on or after 28-June-2019 are currently available)
    """
)

