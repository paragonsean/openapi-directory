from typing import List, Dict
from aiohttp import web

from openapi_server.models.tfl_api_presentation_entities_search_response import TflApiPresentationEntitiesSearchResponse
from openapi_server import util


async def search_bus_schedules(request: web.Request, query) -> web.Response:
    """Searches the bus schedules folder on S3 for a given bus number.

    

    :param query: The search query
    :type query: str

    """
    return web.Response(status=200)


async def search_get(request: web.Request, query) -> web.Response:
    """Search the site for occurrences of the query string. The maximum number of results returned is equal to the maximum page size              of 100. To return subsequent pages, use the paginated overload.

    

    :param query: The search query
    :type query: str

    """
    return web.Response(status=200)


async def search_meta_categories(request: web.Request, ) -> web.Response:
    """Gets the available search categories.

    


    """
    return web.Response(status=200)


async def search_meta_search_providers(request: web.Request, ) -> web.Response:
    """Gets the available searchProvider names.

    


    """
    return web.Response(status=200)


async def search_meta_sorts(request: web.Request, ) -> web.Response:
    """Gets the available sorting options.

    


    """
    return web.Response(status=200)
