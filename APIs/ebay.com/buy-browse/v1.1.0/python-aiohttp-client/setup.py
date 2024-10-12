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
    description="Browse API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Browse API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    The Browse API has the following resources: item_summary: Lets shoppers search for specific items by keyword, GTIN, category, charity, product, or item aspects and refine the results by using filters, such as aspects, compatibility, and fields values. &amp;nbsp;(Experimental) search_by_image: Lets shoppers search for specific items by image. You can refine the results by using URI parameters and filters. item: Lets you retrieve the details of a specific item or all the items in an item group, which is an item with variations such as color and size and check if a product is compatible with the specified item, such as if a specific car is compatible with a specific part. Provides a bridge between the eBay legacy APIs, such as Finding, and the RESTful APIs, which use different formats for the item IDs. &amp;nbsp;(Experimental) shopping_cart: Provides the ability for eBay members to see the contents of their eBay cart, and add, remove, and change the quantity of items in their eBay cart.&amp;nbsp;&amp;nbsp; Note: This resource is not available in the eBay API Explorer. The item_summary, search_by_image, and item resource calls require an Application access token. The shopping_cart resource calls require a User access token.
    """
)

