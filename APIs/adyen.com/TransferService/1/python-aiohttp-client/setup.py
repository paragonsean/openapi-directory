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
    description="Transfers API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Transfers API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &gt;Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.  This API provides endpoints that you can use to transfer funds, whether when [paying out to a transfer instrument](https://docs.adyen.com/marketplaces-and-platforms/payout-to-users/on-demand-payouts), [sending funds to third parties](https://docs.adyen.com/marketplaces-and-platforms/business-accounts/send-receive-funds) for users with business bank accounts, or to [request a payout for a grant offer](https://docs.adyen.com/marketplaces-and-platforms/capital). The API also supports use cases for [getting transactions for business bank accounts](https://docs.adyen.com/marketplaces-and-platforms/business-accounts/transactions-api) and getting [grants and its outstanding balances](https://docs.adyen.com/marketplaces-and-platforms/capital#get-balances). .  ## Authentication Your Adyen contact will provide your API credential and an API key. To connect to the API, add an &#x60;X-API-Key&#x60; header with the API key as the value, for example:   &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;X-API-Key: YOUR_API_KEY\&quot; \\ ... &#x60;&#x60;&#x60;  Alternatively, you can use the username and password to connect to the API using basic authentication. For example:  &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -U \&quot;ws@BalancePlatform.YOUR_BALANCE_PLATFORM\&quot;:\&quot;YOUR_WS_PASSWORD\&quot; \\ ... &#x60;&#x60;&#x60; ## Roles and permissions To use the Transfers API, you need an additional role for your API credential. Transfers must also be enabled for the source balance account. Your Adyen contact will set up the roles and permissions for you. ## Versioning The Transfers API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example: &#x60;&#x60;&#x60; https://balanceplatform-api-test.adyen.com/btl/v1/transfers &#x60;&#x60;&#x60; ## Going live When going live, your Adyen contact will provide your API credential for the live environment. You can then use the username and password to send requests to &#x60;https://balanceplatform-api-live.adyen.com/btl/v1&#x60;.  
    """
)

