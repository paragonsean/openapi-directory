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
    description="Notification Configuration API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Notification Configuration API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API is used for the classic integration. If you are just starting your implementation, refer to our [new integration guide](https://docs.adyen.com/marketplaces-and-platforms) instead.  The Notification Configuration API provides endpoints for setting up and testing notifications that inform you of events on your platform, for example when a verification check or a payout has been completed.  For more information, refer to our [documentation](https://docs.adyen.com/marketplaces-and-platforms/classic/notifications). ## Authentication Your Adyen contact will provide your API credential and an API key. To connect to the API, add an &#x60;X-API-Key&#x60; header with the API key as the value, for example:   &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;X-API-Key: YOUR_API_KEY\&quot; \\ ... &#x60;&#x60;&#x60;  Alternatively, you can use the username and password to connect to the API using basic authentication. For example:  &#x60;&#x60;&#x60; curl -U \&quot;ws@MarketPlace.YOUR_PLATFORM_ACCOUNT\&quot;:\&quot;YOUR_WS_PASSWORD\&quot; \\ -H \&quot;Content-Type: application/json\&quot; \\ ... &#x60;&#x60;&#x60; When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).  ## Versioning The Notification Configuration API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example: &#x60;&#x60;&#x60; https://cal-test.adyen.com/cal/services/Notification/v4/createNotificationConfiguration &#x60;&#x60;&#x60;
    """
)

