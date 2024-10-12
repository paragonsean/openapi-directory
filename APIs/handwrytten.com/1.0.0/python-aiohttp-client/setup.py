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
    description="Handwrytten API",
    author_email="contact@handwrytten.com",
    url="",
    keywords=["OpenAPI", "Handwrytten API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This is the Handwrytten API for sending cards written in the handwriting of your choice. Using this api, you can send cards to users.  You can also customize cards with logos, which can be saved and then used like any other card in the system. For a \&quot;sandbox\&quot; account, please contact contact@handwrytten.com To move from credit card per-transaction to monthly invoicing, also contact us. [https://www.handwrytten.com](https://www.handwrytten.com) 
    """
)

