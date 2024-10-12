from typing import List, Dict
from aiohttp import web

from openapi_server.models.filters_api_response import FiltersAPIResponse
from openapi_server.models.meshery_filter import MesheryFilter
from openapi_server import util


async def id_delete_meshery_filter(request: web.Request, id) -> web.Response:
    """Handle Delete for a Meshery Filter

    Deletes a meshery filter with ID: id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_get_filter_file(request: web.Request, ) -> web.Response:
    """Handle GET request for all filters

    Returns all the Meshery Filters saved by the current user


    """
    return web.Response(status=200)


async def id_get_filter_files(request: web.Request, id) -> web.Response:
    """Handle GET request for filter file with given id

    Returns the Meshery Filter file saved by the current user with the given id

    :param id: Automatically added
    :type id: str

    """
    return web.Response(status=200)


async def id_get_meshery_filter(request: web.Request, id) -> web.Response:
    """Handle GET request for a Meshery Filter

    Fetches the Meshery Filter with the given id

    :param id: id for a specific
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def id_post_filter_file(request: web.Request, ) -> web.Response:
    """Handle POST requests for Meshery Filters

    Used to save/update a Meshery Filter


    """
    return web.Response(status=200)
