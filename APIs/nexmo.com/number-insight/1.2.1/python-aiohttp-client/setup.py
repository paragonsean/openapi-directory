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
    description="Number Insight API",
    author_email="devrel@vonage.com",
    url="",
    keywords=["OpenAPI", "Number Insight API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Number Insight API delivers real-time intelligence about the validity, reachability and roaming status of a phone number and tells you how to format the number correctly in your application. There are three levels of Number Insight API available: [Basic, Standard and Advanced](https://developer.nexmo.com/number-insight/overview#basic-standard-and-advanced-apis). The advanced API is available asynchronously as well as synchronously.
    """
)

