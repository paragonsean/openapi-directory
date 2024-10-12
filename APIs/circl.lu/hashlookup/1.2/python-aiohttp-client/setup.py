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
    description="hashlookup CIRCL API",
    author_email="",
    url="",
    keywords=["OpenAPI", "hashlookup CIRCL API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ![](https://www.circl.lu/assets/images/circl-logo.png) [CIRCL hash lookup](https://hashlookup.circl.lu/) is a public API to lookup hash values against known database of files. For more details about all the datasets included [visit the website of the project](https://www.circl.lu/services/hashlookup/). The API is accessible via HTTP ReST API and the API is also [described as an OpenAPI](https://hashlookup.circl.lu/swagger.json). A [documentation is available with](https://www.circl.lu/services/hashlookup/) with sample queries and software using hashlookup. An offline version as Bloom filter is also [available](https://circl.lu/services/hashlookup/#how-to-quickly-check-a-set-of-files-in-a-local-directory). The API can be tested live in the interface below.
    """
)

