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
    description="Suggestions",
    author_email="",
    url="",
    keywords=["OpenAPI", "Suggestions"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      The **Marketplace API** enables marketplaces and sellers hosted on VTEX to perform their collaborative operations.      &gt;⚠️ The marketplace must [create an appKey and appToken](https://developers.vtex.com/docs/guides/getting-started-authentication) for each non-VTEX seller that will use this API.    ## Index    ### Notification    Endpoints used by sellers to notify marketplaces that the price or inventory language has changed for one of their SKUs.    &#x60;POST&#x60; [Notify marketplace of price update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/price)    &#x60;POST&#x60; [Notify marketplace of inventory update](https://developers.vtex.com/docs/api-reference/marketplace-apis#post-/notificator/-sellerId-/changenotification/-skuId-/inventory)      ### Suggestions    #### Get Suggestions    Search and filter all suggestions using specific criteria.    &#x60;GET&#x60; [Get all SKU Suggestions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions)    &#x60;GET&#x60; [Get SKU Suggestion by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerSkuId-)      #### Manage Suggestions    Send or delete SKU suggestions from the seller to marketplace.    &#x60;PUT&#x60; [Send SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerSkuId-)    &#x60;DELETE&#x60; [Delete SKU Suggestion](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#delete-/suggestions/-sellerId-/-sellerSkuId-)      #### Get Versions    Search and filter all versions of suggestions, using specific criteria.    &#x60;GET&#x60; [Get all versions](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerskuid-/versions)    &#x60;GET&#x60; [Get version by ID](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/-sellerId-/-sellerskuid-/versions/-version-)      #### Match Received SKUs    Match SKU suggestions received in the marketplace.    &#x60;PUT&#x60; [Match Received SKUs individually](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/-sellerId-/-sellerskuid-/versions/-version-/matches/-matchid-)    &#x60;PUT&#x60; [Match Multiple Received SKUs](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/matches/action/-actionName-)      #### SKU Approval Settings    Allows marketplaces to configure rules for automatically and manually approving SKUs received from sellers.    &#x60;GET&#x60;[Get autoApprove Status in Account Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration/autoapproval/toggle)      &#x60;PUT&#x60;[Activate autoApprove in Marketplace&#39;s Account](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/autoapproval/toggle)      &#x60;GET&#x60;[Get Account&#39;s Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration)    &#x60;PUT&#x60;[Save Account&#39;s Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration)    &#x60;GET&#x60;[Get Seller&#39;s Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#get-/suggestions/configuration/seller/-sellerId-)    &#x60;PUT&#x60;[Save Seller&#39;s Approval Settings](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/seller/-sellerId-)    &#x60;PUT&#x60;[Activate autoApprove Setting for a Seller](https://developers.vtex.com/docs/api-reference/marketplace-apis-suggestions#put-/suggestions/configuration/autoapproval/toggle/seller/-sellerId-)         ### Matched Offers    Offers are seller products and SKUs that were sent to the marketplace, and already have their price and inventory level configured.    &#x60;GET&#x60;[Get Matched Offers List](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/offer-manager/pvt/offers)    &#x60;GET&#x60;[Get Matched Offer&#39;s Data by SKU ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/offer-manager/pvt/product/-productId-/sku/-skuId-)      &#x60;GET&#x60;[Get Matched Offer&#39;s Data by Product ID](https://developers.vtex.com/docs/api-reference/marketplace-apis#get-/offer-manager/pvt/product/-productId-)  
    """
)

