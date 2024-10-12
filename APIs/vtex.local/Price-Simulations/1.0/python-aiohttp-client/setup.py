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
    description="Price Simulations API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Price Simulations API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      &gt; Check the new [Pricing onboarding guide](https://developers.vtex.com/docs/guides/pricing-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Pricing and is organized by focusing on the developer&#39;s journey    The Price Simulations API allows you to configure custom price selectors for B2B stores, based on the context set by the [Orders Configuration app](https://developers.vtex.com/docs/guides/vtex-order-configuration).    ## Custom Prices    In this section, you can create a specific shopping scenario with the criteria you want. For explaining purpose, we used the &#x60;orderType&#x60; and &#x60;state&#x60; as default values, but it can be others too.    &#x60;GET&#x60; [Get custom prices schema](https://developers.vtex.com/docs/api-reference/price-simulations#get-/_v/custom-prices/session/schema)  &#x60;POST&#x60; [Create or Update custom prices schema](https://developers.vtex.com/docs/api-reference/price-simulations#post-/_v/custom-prices/session/schema)    ## Session Management    Every time you edit a configuration value set on the Custom Prices session, you must use this endpoint to update the Order Configuration.    &#x60;POST&#x60; [Update Order Configuration](https://developers.vtex.com/docs/api-reference/price-simulations#post-/sessions/)      ## Price Association    Use these routes to associate a shopping scenario, created at the Custom Price session, to a specific price table.    &#x60;GET&#x60; [Get price association by ID](https://developers.vtex.com/docs/api-reference/price-simulations#get-/_v/custom-prices/rules/-priceAssociationId-)  &#x60;POST&#x60; [Create price association](https://developers.vtex.com/docs/api-reference/price-simulations#post-/_v/custom-prices/rules)  &#x60;PUT&#x60; [Update price association by ID](https://developers.vtex.com/docs/api-reference/price-simulations#put-/_v/custom-prices/rules/-priceAssociationId-)  &#x60;DELETE&#x60; [Disassociate price association by ID](https://developers.vtex.com/docs/api-reference/price-simulations#delete-/_v/custom-prices/rules/-priceAssociationId-)
    """
)

