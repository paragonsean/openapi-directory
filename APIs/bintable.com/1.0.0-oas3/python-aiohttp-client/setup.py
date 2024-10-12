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
    description="BIN Lookup API",
    author_email="hello@bintable.com",
    url="",
    keywords=["OpenAPI", "BIN Lookup API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    BIN lookup API, the free api service from bintable.com to lookup card information using it&#39;s BIN. the service maintains updated database based on the comunity and other third party services to make sure all BINs in the database are accurate and up to date.
    """
)

