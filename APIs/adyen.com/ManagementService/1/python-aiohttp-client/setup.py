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
    description="Management API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Management API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the &#x60;X-API-Key&#x60; header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to this version of the &#x60;/companies/{companyId}/webhooks&#x60; endpoint, use:  &#x60;&#x60;&#x60;text https://management-test.adyen.com/v1/companies/{companyId}/webhooks &#x60;&#x60;&#x60;  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  &#x60;&#x60;&#x60;text https://management-live.adyen.com/v1 &#x60;&#x60;&#x60;  ## Release notes Have a look at the [release notes](https://docs.adyen.com/release-notes/management-api) to find out what changed in this version!
    """
)

