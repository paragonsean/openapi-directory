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
    description="Adyen Payout API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Adyen Payout API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    A set of API endpoints that allow you to store payout details, confirm, or decline a payout.  For more information, refer to [Online payouts](https://docs.adyen.com/online-payments/online-payouts). ## Authentication To use the Payout API, you need to have [two API credentials](https://docs.adyen.com/online-payments/online-payouts#payouts-to-bank-accounts-and-wallets): one for storing payout details and submitting payouts, and another one for confirming or declining payouts. If you don&#39;t have the required API credentials, contact our [Support Team](https://www.adyen.help/hc/en-us/requests/new).  If using an API key, add an &#x60;X-API-Key&#x60; header with the API key as the value, for example:   &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;X-API-Key: YOUR_API_KEY\&quot; \\ ... &#x60;&#x60;&#x60;  Alternatively, you can use the username and password to connect to the API using [basic authentication](https://docs.adyen.com/development-resources/api-credentials#basic-authentication).  The following example shows how to authenticate your request with basic authentication when submitting a payout:  &#x60;&#x60;&#x60; curl -U \&quot;storePayout@Company.YOUR_COMPANY_ACCOUNT\&quot;:\&quot;YOUR_BASIC_AUTHENTICATION_PASSWORD\&quot; \\ -H \&quot;Content-Type: application/json\&quot; \\ ... &#x60;&#x60;&#x60;  ## Versioning Payments API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example: &#x60;&#x60;&#x60; https://pal-test.adyen.com/pal/servlet/Payout/v40/payout &#x60;&#x60;&#x60;  ## Going live  To authenticate to the live endpoints, you need [API credentials](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.  The live endpoint URLs contain a prefix which is unique to your company account: &#x60;&#x60;&#x60;  https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payout/v40/payout &#x60;&#x60;&#x60;  Get your &#x60;{PREFIX}&#x60; from your live Customer Area under **Developers** &gt; **API URLs** &gt; **Prefix**.
    """
)

