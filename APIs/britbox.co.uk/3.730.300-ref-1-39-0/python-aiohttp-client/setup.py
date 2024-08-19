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
    description="Rocket Services",
    author_email="",
    url="",
    keywords=["OpenAPI", "Rocket Services"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    An Orchestration Layer that takes ISL services and packages them in a more targeted way for front-end applications. This in turn makes client integration easier and reduces the complexity and size of front-end applications.  Rocket is also customisable - allowing UI engineers to ‘remix’ the existing back-end services into something that best suits the application they are developing. 
    """
)

