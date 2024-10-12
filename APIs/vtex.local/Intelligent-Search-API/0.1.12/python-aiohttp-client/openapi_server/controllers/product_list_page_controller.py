from typing import List, Dict
from aiohttp import web

from openapi_server.models.banners import Banners
from openapi_server.models.correction import Correction
from openapi_server.models.error import Error
from openapi_server.models.facets import Facets
from openapi_server.models.product_search import ProductSearch
from openapi_server.models.search_suggestions import SearchSuggestions
from openapi_server import util


async def banners_facets_get(request: web.Request, facets, query=None, locale=None) -> web.Response:
    """Get list of banners registered for query

    Lists the banners registered for a given query. Check the [configuring banners documentation](https://help.vtex.com/en/tracks/vtex-intelligent-search--19wrbB7nEQcmwzDPl1l4Cb/4ViKEivLJtJsvpaW0aqIQ5) for a full explanation of the banner feature.

    :param facets: # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. | 
    :type facets: str
    :param query: Search term. It can contain any character.
    :type query: str
    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str

    """
    return web.Response(status=200)


async def correction_search_get(request: web.Request, query=None, locale=None) -> web.Response:
    """Get attempt of correction of a misspelled term

    Tries to correct a misspelled term from the search.

    :param query: Search term. It can contain any character.
    :type query: str
    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str

    """
    return web.Response(status=200)


async def facets_facets_get(request: web.Request, facets, query=None, locale=None, hide_unavailable_items=None) -> web.Response:
    """Get list of the possible facets for a given query

    Lists the possible facets for a given query

    :param facets: # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. | 
    :type facets: str
    :param query: Search term. It can contain any character.
    :type query: str
    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str
    :param hide_unavailable_items: Whether the result should hide unavailable items (&#x60;true&#x60;), or not (&#x60;false&#x60;)
    :type hide_unavailable_items: bool

    """
    return web.Response(status=200)


async def product_search_facets_get(request: web.Request, facets, query=None, simulation_behavior=None, count=None, page=None, sort=None, locale=None, hide_unavailable_items=None) -> web.Response:
    """Get list of products for a query

    Lists the products for a given query.

    :param facets: # Format  The &#x60;facets&#x60; parameter follows the format : &#x60;/${facetKey1}/${facetValue1}/${facetKey2}/${facetValue2}/.../${facetKeyN}/${facetValueN}&#x60;.  The order in which the terms appear is not relevant to the search.  You can also repeat the same &#x60;facetKey&#x60; several times for different values. For example: &#x60;category-1/shoes/color/blue/color/red/color/yellow&#x60;  # General filters  The &#x60;facets&#x60; parameter also allows the following general filters.  | &#x60;facetKey&#x60;      | Description                                                                                      | Example                                                                  | | --------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------ | | &#x60;price&#x60;         | Filter the search by a price range. The facet value follows the format &#x60;${minPrice}:${maxPrice}&#x60; | &#x60;/color/blue/price/100:500?query&#x3D;shirt&#x60;                                  | | &#x60;category-${n}&#x60; | Filter the search by category, where &#x60;n&#x60; represents the category tree level (1 &#x3D; department, 2 &#x3D; category, 3 &#x3D; subcategory, and so on) | &#x60;category-1/clothing/category-2/shirts&#x60;                                  | | &#x60;region-id&#x60;     | Filter the search by a region id (aka regionalization). The value is the region id               | &#x60;/color/blue/region-id/v2.26219C7C3DE42BAAD11CFB92CD0BFE91?query&#x3D;shirt&#x60;. | 
    :type facets: str
    :param query: Search term. It can contain any character.
    :type query: str
    :param simulation_behavior: Defines the simulation behavior.   * &#x60;default&#x60; - Calls the simulation for every single seller.  * &#x60;skip&#x60; - Never calls the simulation.  * &#x60;only1P&#x60; - Only calls the simulation for first party sellers.
    :type simulation_behavior: str
    :param count: Number of products per page.
    :type count: 
    :param page: Current search page.
    :type page: 
    :param sort: Defines the sort type. If null, the products will be sorted by relevance.
    :type sort: str
    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str
    :param hide_unavailable_items: Whether the result should hide unavailable items (&#x60;true&#x60;), or not (&#x60;false&#x60;)
    :type hide_unavailable_items: bool

    """
    return web.Response(status=200)


async def search_suggestions_get(request: web.Request, query=None, locale=None) -> web.Response:
    """Get list of suggested terms similar to the search term

    Lists suggested terms similar to the search term.

    :param query: Search term. It can contain any character.
    :type query: str
    :param locale: Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    :type locale: str

    """
    return web.Response(status=200)
