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
    description="Chaingateway.io",
    author_email="",
    url="",
    keywords=["OpenAPI", "Chaingateway.io"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    # Chaingateway.io  REST API to build the bridge between Ethereum and the real world  Please check out our [website](https://chaingateway.io?utm_source&#x3D;postman) for detailed information about this API.  To use our API, you need an API Key (Described as Authorization header in the examples below). To get one, please create an account on our [website](https://chaingateway.io/register?utm_source&#x3D;postman).  For our internal documentation, please check out our [Docs Site](https://chaingateway.io/docs?utm_source&#x3D;postman).  If you need help with integrating our API in your application, you can reach us via [email](mailto:support@chaingateway.io) or join our official [Telegram](https://t.me/chaingateway) group.
    """
)

