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
    description="Intelligent Search API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Intelligent Search API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['openapi_server=openapi_server.__main__:main']},
    long_description="""\
    &gt;ℹ️ Onboarding guide  &gt;  &gt; Check the new [Search onboarding guide](https://developers.vtex.com/docs/guides/search-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Search and is organized by focusing on the developer&#39;s journey.    This API is from the [VTEX Intelligent Search](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/3qgT47zY08biLP3d5os3DG) solution, an alternative to the platform’s native search, as it assists the customer in their purchase journey, and it presents results since the first interaction with the search bar.    ## Index  - [Get list of the 10 most searched terms](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/top_searches)  - [Get list of suggested terms and attributes similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/autocomplete_suggestions)  - [Get attempt of correction of a misspelled term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/correction_search)  - [Get list of banners registered for query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/banners/-facets-)  - [Get list of suggested terms similar to the search term](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/search_suggestions)  - [Get list of products for a query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/product_search/-facets-)  - [Get list of the possible facets for a given query](https://developers.vtex.com/docs/api-reference/intelligent-search-api#get-/facets/-facets-)
    """
)

