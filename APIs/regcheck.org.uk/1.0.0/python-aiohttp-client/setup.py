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
    description="Car Registration API",
    author_email="info@infiniteloop.ie",
    url="",
    keywords=["OpenAPI", "Car Registration API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Car Registration API, An API that retrieves car information from its numberplate in many countries worldwide, uncluding the USA, UK, India, Australia and most of Europe. A username and password is required to access the API, which can be obtained from www.carregistrationapi.com - Use https://www.regcheck.org.uk/api/json.aspx/ as the root of all API calls.
    """
)

