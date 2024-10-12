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
    description="Hosted onboarding API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Hosted onboarding API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API is used for the classic integration. If you are just starting your implementation, refer to our [new integration guide](https://docs.adyen.com/marketplaces-and-platforms) instead.  The Hosted onboarding API provides endpoints that you can use to generate links to Adyen-hosted pages, such as an [onboarding page](https://docs.adyen.com/marketplaces-and-platforms/classic/hosted-onboarding-page) or a [PCI compliance questionnaire](https://docs.adyen.com/marketplaces-and-platforms/classic/platforms-for-partners). You can provide these links to your account holders so that they can complete their onboarding.  ## Authentication Your Adyen contact will provide your API credential and an API key. To connect to the API, add an &#x60;X-API-Key&#x60; header with the API key as the value, for example:   &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;X-API-Key: YOUR_API_KEY\&quot; \\ ... &#x60;&#x60;&#x60;  Alternatively, you can use the username and password to connect to the API using basic authentication. For example:  &#x60;&#x60;&#x60; curl -U \&quot;ws@MarketPlace.YOUR_PLATFORM_ACCOUNT\&quot;:\&quot;YOUR_WS_PASSWORD\&quot; \\ -H \&quot;Content-Type: application/json\&quot; \\ ... &#x60;&#x60;&#x60; When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).  ## Versioning The Hosted onboarding API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example: &#x60;&#x60;&#x60; https://cal-test.adyen.com/cal/services/Hop/v5/getOnboardingUrl &#x60;&#x60;&#x60;
    """
)

