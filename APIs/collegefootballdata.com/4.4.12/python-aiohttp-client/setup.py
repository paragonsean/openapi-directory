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
    description="College Football Data API",
    author_email="admin@collegefootballdata.com",
    url="",
    keywords=["OpenAPI", "College Football Data API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is an API for accessing all sorts of college football data.  Please note that API keys should be supplied with \&quot;Bearer \&quot; prepended (e.g. \&quot;Bearer your_key\&quot;). API keys can be acquired from the CollegeFootballData.com website.
    """
)

