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
    description="Adyen Balance Control API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Adyen Balance Control API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Balance Control API lets you transfer funds between merchant accounts that belong to the same legal entity and are under the same company account.  ## Authentication To connect to the Balance Control API, you must authenticate your requests with an [API key or basic auth username and password](https://docs.adyen.com/development-resources/api-authentication). To learn how you can generate these, see [API credentials](https://docs.adyen.com/development-resources/api-credentials).Here is an example of authenticating a request with an API key:  &#x60;&#x60;&#x60; curl -H \&quot;X-API-Key: Your_API_key\&quot; \\ -H \&quot;Content-Type: application/json\&quot; \\ ... &#x60;&#x60;&#x60; Note that when going live, you need to generate API credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).  ## Versioning The Balance Control API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example:  &#x60;&#x60;&#x60; https://pal-test.adyen.com/pal/servlet/BalanceControl/v1/balanceTransfer &#x60;&#x60;&#x60; 
    """
)

