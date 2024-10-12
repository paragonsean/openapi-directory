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
    description="Tradematic Cloud API",
    author_email="support@tradematic.com",
    url="",
    keywords=["OpenAPI", "Tradematic Cloud API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    ### Overview Tradematic Cloud is a trading infrastructure for building investment services.  It’s a trading engine + API + ready-made adapters to stock and forex brokers, crypto exchanges, and market data providers.  You can use it as a cloud API, or you can deploy it on your servers.     ### How to use Tradematic Cloud API  Sign up at [tradematic.cloud](https://tradematic.cloud). After signing up, you will receive your API key.  ### Authorization  Add the &#39;X-API-KEY&#39; header with your API key to each request.  ### Examples of writing code with Tradematic Cloud API  Examples are available at [tradematic.cloud](https://tradematic.cloud).   ### Swagger (.yaml) File Swagger (.yaml) file can be found [here](http://tradematic.cloud/sdk/swagger.yaml). 
    """
)

