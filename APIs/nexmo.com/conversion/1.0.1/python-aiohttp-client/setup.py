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
    description="Nexmo Conversion API",
    author_email="devrel@nexmo.com",
    url="",
    keywords=["OpenAPI", "Nexmo Conversion API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Conversion API allows you to tell Nexmo about the reliability of your 2FA communications. Sending conversion data back to us means that Nexmo can deliver messages faster and more reliably. The conversion data you send us is confidential: Nexmo does not share it with third parties. In order to identify the carriers who provide the best performance, Nexmo continually tests the routes we use to deliver SMS and voice calls. Using Adaptive Routing™, Nexmo actively reroutes messages through different carrier routes and ensures faster and more reliable delivery for your messages. The route choice is made using millions of real-time conversion data points.
    """
)

