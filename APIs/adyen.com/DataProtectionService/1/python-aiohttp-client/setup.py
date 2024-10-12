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
    description="Adyen Data Protection API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Adyen Data Protection API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Adyen Data Protection API provides a way for you to process [Subject Erasure Requests](https://gdpr-info.eu/art-17-gdpr/) as mandated in GDPR.  Use our API to submit a request to delete shopper&#39;s data, including payment details and other related information (for example, delivery address or shopper email).## Authentication Each request to the Data Protection API must be signed with an API key. Get your API Key from your Customer Area, as described in [How to get the API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). Then set this key to the &#x60;X-API-Key&#x60; header value, for example:  &#x60;&#x60;&#x60; curl -H \&quot;Content-Type: application/json\&quot; \\ -H \&quot;X-API-Key: Your_API_key\&quot; \\ ... &#x60;&#x60;&#x60; Note that when going live, you need to generate a new API Key to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).  ## Versioning Data Protection Service API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: \&quot;vXX\&quot;, where XX is the version number.  For example: &#x60;&#x60;&#x60; https://ca-test.adyen.com/ca/services/DataProtectionService/v1/requestSubjectErasure &#x60;&#x60;&#x60;
    """
)

