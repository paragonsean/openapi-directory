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
    description="Pirates API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Pirates API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Ahoy matey! We help the landlubbers to get to know about the seamen way! You can generate pirate names, get some real pirate insults and pirate filler text. Oh you can translate to pirate lingo as well. [Click here to subscribe](http://fungenerators.com/api/pirate/)  
    """
)

