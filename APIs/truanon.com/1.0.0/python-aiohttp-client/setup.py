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
    description="TruAnon Private API",
    author_email="",
    url="",
    keywords=["OpenAPI", "TruAnon Private API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Welcome to TruAnon! Thank you for helping make the Internet a safer place to be.  Adopting TruAnon is simple. There is no setup or dependencies, nothing to store or process. Making identity part of your service is fun, and you’ll be up and running in a matter of minutes.  TruAnon Private Token is used anytime you request information from TruAnon and you must edit this into the Variables section for this collection.  This API contains two endpoints and both require these same two arguments, also found in the Variables section of this collection.  These two arguments are:  TruAnon Service Identifier  and  Your Member Name  Your TruAnon Service Identifier was provided by TruAnon and is likely the root domain of your site or service. Your Member Name is the unique member ID on your system that you would like to query.  Information is continuously updated for display purposes and aside from performance considerations, there should be no need to capture or save anything from TruAnon.
    """
)

