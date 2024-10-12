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
    description="dweet.io",
    author_email="",
    url="",
    keywords=["OpenAPI", "dweet.io"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Dweet.io allows users to share data from mobile, tablets, and pcs, and them to other devices and accounts across social media platforms. Dweet.io provides an API to access the different functionality of the Dweet.io service. Users can make REST calls to read and create dweets, lock and unlock things, and perform other calls. The API returns JSON and JSONP.
    """
)

