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
    description="Directorate of Economics and Statistics Cum Chief Registrar, Rajasthan, Rajasthan",
    author_email="",
    url="",
    keywords=["OpenAPI", "Directorate of Economics and Statistics Cum Chief Registrar, Rajasthan, Rajasthan"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Birth, Still-Birth, Death and Marriage Certificates issued by the Department, from 01 January 2014 onward, can be pulled into citizens&#39; DigiLocker accounts.
    """
)

