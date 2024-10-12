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
    description="AWSMainframeModernization",
    author_email="mike.ralphson@gmail.com",
    url="",
    keywords=["OpenAPI", "AWSMainframeModernization"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Amazon Web Services Mainframe Modernization provides tools and resources to help you plan and implement migration and modernization from mainframes to Amazon Web Services managed runtime environments. It provides tools for analyzing existing mainframe applications, developing or updating mainframe applications using COBOL or PL/I, and implementing an automated pipeline for continuous integration and continuous delivery (CI/CD) of the applications.
    """
)

