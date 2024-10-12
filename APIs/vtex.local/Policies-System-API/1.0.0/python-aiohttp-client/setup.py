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
    description="Policies System API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Policies System API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
       This API will create promotion alarms when selling products with undesired prices and promotions. It will create conditions that will check if the prices and the promotions are correct. If not, the system will alarm the store with information about the product sold at unexpected prices.     ## Index     &#x60;GET&#x60; [Get Policy List](https://developers.vtex.com/docs/api-reference/policies-system-api#get-/api/policy-engine/policies)   &#x60;POST&#x60; [Evaluate Policies](https://developers.vtex.com/docs/api-reference/policies-system-api#post-/api/policy-engine/evaluate)   &#x60;GET&#x60; [Get Policy by ID](https://developers.vtex.com/docs/api-reference/policies-system-api#get-/api/policy-engine/policies/-id-)   &#x60;POST&#x60; [Create Policy](https://developers.vtex.com/docs/api-reference/policies-system-api#post-/api/policy-engine/policies/-id-)   &#x60;PUT&#x60; [Update Policy](https://developers.vtex.com/docs/api-reference/policies-system-api#put-/api/policy-engine/policies/-id-)   &#x60;DELETE&#x60; [Delete Policy by ID](https://developers.vtex.com/docs/api-reference/policies-system-api#delete-/api/policy-engine/policies/-id-)
    """
)

