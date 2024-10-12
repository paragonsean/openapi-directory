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
    description="Revenue, Registration &amp; Land Reforms Department, Jharkhand",
    author_email="",
    url="",
    keywords=["OpenAPI", "Revenue, Registration &amp; Land Reforms Department, Jharkhand"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Department of Revenue, Registration &amp; Land Reforms, Jharkhand (http://www.jharkhand.gov.in/revenue) is issuing Registration Certificate of Deeds into citizens&#39; DigiLocker accounts from 5th May 2017 onwards.
    """
)

