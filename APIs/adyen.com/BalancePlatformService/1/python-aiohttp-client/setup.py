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
    description="Configuration API",
    author_email="developer-experience@adyen.com",
    url="",
    keywords=["OpenAPI", "Configuration API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Configuration API enables you to create a platform where you can onboard your users as account holders and create balance accounts, cards, and business accounts.  ## Authentication Your Adyen contact will provide your API credential and an API key. To connect to the API, add an &#x60;X-API-Key&#x60; header with the API key as the value, for example:   &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;X-API-Key: YOUR_API_KEY\&quot; \\ ... &#x60;&#x60;&#x60;  Alternatively, you can use the username and password to connect to the API using basic authentication. For example:  &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -U \&quot;ws@BalancePlatform.YOUR_BALANCE_PLATFORM\&quot;:\&quot;YOUR_WS_PASSWORD\&quot; \\ ... &#x60;&#x60;&#x60; ## Versioning The Configuration API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example: &#x60;&#x60;&#x60; https://balanceplatform-api-test.adyen.com/bcl/v1/accountHolders &#x60;&#x60;&#x60; ## Going live When going live, your Adyen contact will provide your API credential for the live environment. You can then use the API key or the username and password to send requests to &#x60;https://balanceplatform-api-live.adyen.com/bcl/v1&#x60;.
    """
)

