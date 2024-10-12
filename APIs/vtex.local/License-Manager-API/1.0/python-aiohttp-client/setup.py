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
    description="License Manager API",
    author_email="",
    url="",
    keywords=["OpenAPI", "License Manager API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ## Welcome!    The License Manager API allows you to create users, modify their names and emails, as well as add and remove roles from users.    ### ATTRIBUTES    |Attribute name | Description |  |:------------|--------------|  |accountName | Account name in VTEX License Manager |  |environment | Environment on which you want to run the query e.g. vtexcommercestable |  |userId      | Unique user identification string |  |roleId      | Integer that represents a role, can be looked up on the License Manager UI |
    """
)

