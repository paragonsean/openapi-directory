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
    description="Severa Public Rest API Documentation",
    author_email="",
    url="",
    keywords=["OpenAPI", "Severa Public Rest API Documentation"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The API uses OAuth2 client creadentials flow. To get the Bearer token for the resources you have to request the token by using route &#39;/token&#39;, found from Authentication controller.    You need to provide a Client_Id, client_secret and scope needed. The client_id and client_secret can be obtained from Severa UI Rest Api settings section.    After authentication, calls need to use the Bearer token as authorization header (Bearer {accessToken}). The calls also need to have Client_Id header.    The access token can be refreshed from &#39;/refreshtoken&#39; route using the refresh token which was obtained from the authentication.    
    """
)

