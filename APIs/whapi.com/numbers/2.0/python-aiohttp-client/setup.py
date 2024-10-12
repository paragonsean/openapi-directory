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
    description="Numbers API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Numbers API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The William Hill Numbers API uses a single method that allows you to generate random numbers for your application. Numbers can either be unique or can be produced with the chance that some might be the same. For example, you can have a highest value of 6 and a lowest value of 1 with a count of 2 with a unique value of false - this will give you two numbers between 1 and 6 which are independent, just like two dice being rolled.&lt;br /&gt;&lt;br /&gt;The Numbers API is a Private API and therefore not automatically available to developers. To use this API, contact your business manager who will guide you through the separate Terms and Conditions of use before you can have the API assigned to your application.
    """
)

