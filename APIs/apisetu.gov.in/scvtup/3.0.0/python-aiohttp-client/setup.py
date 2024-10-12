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
    description="UP State Council of Vocational Training, Uttar Pradesh, Uttar Pradesh",
    author_email="",
    url="",
    keywords=["OpenAPI", "UP State Council of Vocational Training, Uttar Pradesh, Uttar Pradesh"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The State Council for Vocational Training (SCVT), Uttar Pradesh (http://www.vppup.in/) provides semester and consolidated mark sheets as well as vocational certificates for years 2013 to 2016.
    """
)

