from typing import List, Dict
from aiohttp import web

from openapi_server.models.taxonomy_attractions200_response import TaxonomyAttractions200Response
from openapi_server.models.taxonomy_attractions_request import TaxonomyAttractionsRequest
from openapi_server.models.taxonomy_categories200_response import TaxonomyCategories200Response
from openapi_server.models.taxonomy_destinations200_response import TaxonomyDestinations200Response
from openapi_server import util


async def taxonomy_attractions(request: web.Request, accept_language, body=None) -> web.Response:
    """/taxonomy/attractions

    Get attractions - Retrieves a list of attractions (things like the Eiffel Tower or Empire State Building) and their associated unique numeric identifiers - The attraction&#39;s identifier (&#x60;seoId&#x60;) can be used as a means of searching for available products; for example, in the [/search/products](#operation/searchProducts) service. 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param body: 
    :type body: dict | bytes

    """
    body = TaxonomyAttractionsRequest.from_dict(body)
    return web.Response(status=200)


async def taxonomy_categories(request: web.Request, accept_language, dest_id=None) -> web.Response:
    """/taxonomy/categories

    Get all product categories - Retrieves a list of product categories for a destination that can be used as a means of filtering when searching for products using the [/search/products](/#operation/searchProducts) service - This service can be used to get a list of all categories and subcategories for a destination by including its &#x60;destId&#x60;, or you can omit the &#x60;destId&#x60; to get a list of all categories and subcategories - **Note:** If no &#x60;destId&#x60; is passed, &#x60;productCount&#x60; and &#x60;thumbnailURL&#x60; will be &#x60;null&#x60; as they are destination-specific fields 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str
    :param dest_id: **unique numeric identifier** of the destination to enquire about (optional) - &#x60;destinationId&#x60; is returned by [/taxonomy/destinations](#operation/taxonomyDestinations) 
    :type dest_id: int

    """
    return web.Response(status=200)


async def taxonomy_destinations(request: web.Request, accept_language) -> web.Response:
    """/taxonomy/destinations

    Get details of all destinations supported by this API - Retrieves all the country taxonomy/city nodes as a flat list - Returns a complete list of Viator destinations, including destination names and parent identifiers - Used to provide navigation through drill down lists or combo boxes 

    :param accept_language: Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    :type accept_language: str

    """
    return web.Response(status=200)
