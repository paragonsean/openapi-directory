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
    description="Geocoder REST API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Geocoder REST API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    This API represents address cleaning, correction, completion, geocoding, reverse geocoding, and proximity resources for intersection addresses, physical addresses and their occupants in British Columbia. Please read our [data collection notice](https://github.com/bcgov/api-specs/blob/master/COLLECTION_NOTICE.md#collection-notice).    Please note that you may experience issues when submitting requests to the delivery or test environment if using this [OpenAPI specification](https://github.com/bcgov/api-specs) in other API console viewers.   [API keys](https://api.gov.bc.ca/devportal/api-directory/273) are unique and can be acquired with a GitHub or IDIR account.    **Notification:** If you have applications or web pages that link to the BC Address Geocoder you must use the following URL.    *https://geocoder.api.gov.bc.ca*    Please note that the following URLs were deprecated in September 2018 [More Details](https://www2.gov.bc.ca/gov/content?id&#x3D;103ADC5A956842828554238DEF28D6E5).    - http://apps.gov.bc.ca/pub/geocoder   - https://apps.gov.bc.ca/pub/geocoder \\ \\  
    """
)

