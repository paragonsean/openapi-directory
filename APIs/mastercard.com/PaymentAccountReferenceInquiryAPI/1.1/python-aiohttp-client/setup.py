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
    description="Payment Account Reference Inquiry API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Payment Account Reference Inquiry API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Payment Account Reference Inquiry API is the unified Mastercard interface for allowing Mastercard Customers involved in payment card acceptance -- whether Merchants, Acquirers, or Digital Activity Customers (DACs) -- to enquire the PAR Vault for getting the PAR, when providing an Account Primary Account Number (PAN) linked to a digitized PAN.
    """
)

