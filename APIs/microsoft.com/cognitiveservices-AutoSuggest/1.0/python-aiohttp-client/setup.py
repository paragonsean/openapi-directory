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
    description="AutoSuggest Client",
    author_email="",
    url="",
    keywords=["OpenAPI", "AutoSuggest Client"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Autosuggest supplies search terms derived from a root text sent to the service.  The terms Autosuggest supplies are related to the root text based on similarity and their frequency or ratings of usefulness in other searches. For examples that show how to use Autosuggest, see [Search using AutoSuggest](https://docs.microsoft.com/en-us/rest/api/cognitiveservices/bing-autosuggest-api-v7-reference).
    """
)

