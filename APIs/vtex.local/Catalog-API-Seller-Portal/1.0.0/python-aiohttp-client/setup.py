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
    description="Catalog API - Seller Portal",
    author_email="",
    url="",
    keywords=["OpenAPI", "Catalog API - Seller Portal"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
      With the Catalog API for Seller Portal, you will be able to create, edit and consult products and their variations, brands, and categories.    &gt; This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).    ## Index    ### Product    &#x60;GET&#x60; [Get Product by ID](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/products/-productId-)  &#x60;PUT&#x60; [Update Product](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#put-/api/catalog-seller-portal/products/-productId-)  &#x60;GET&#x60; [Get Product Description by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/products/-productId-/description)  &#x60;PUT&#x60; [Update Product Description by Product ID](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#put-/api/catalog-seller-portal/products/-productId-/description)  &#x60;GET&#x60; [Get Product by external ID, SKU ID, SKU external ID or slug](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/products/-param-)  &#x60;POST&#x60; [Create Product](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#post-/api/catalog-seller-portal/products)    ### SKU    &#x60;GET&#x60; [Search for SKU](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/skus/_search)  &#x60;GET&#x60; [Get List of SKUs](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/skus/ids)    ### Brand    &#x60;GET&#x60; [Get List of Brands](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/brands)  &#x60;POST&#x60; [Create a Brand](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#post-/api/catalog-seller-portal/brands)  &#x60;GET&#x60; [Get Brand by ID](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/brands/-brandId-)  &#x60;PUT&#x60; [Update Brand](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#put-/api/catalog-seller-portal/brands/-brandId-)    ### Category    &#x60;GET&#x60; [Get Category Tree](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/category-tree)  &#x60;PUT&#x60; [Update Category Tree](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#put-/api/catalog-seller-portal/category-tree)  &#x60;GET&#x60; [Get Category by ID](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#get-/api/catalog-seller-portal/category-tree/categories/-categoryId-)  &#x60;POST&#x60; [Create a Category](https://developers.vtex.com/docs/api-reference/catalog-api-seller-portal#post-/api/catalog-seller-portal/category-tree/categories)
    """
)

