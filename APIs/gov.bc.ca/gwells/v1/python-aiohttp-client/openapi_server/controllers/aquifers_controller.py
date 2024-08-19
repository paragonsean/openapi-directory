from typing import List, Dict
from aiohttp import web

from openapi_server.models.aquifer import Aquifer
from openapi_server.models.aquifer_serializer_basic import AquiferSerializerBasic
from openapi_server.models.aquifers_files_list200_response import AquifersFilesList200Response
from openapi_server.models.aquifers_list200_response import AquifersList200Response
from openapi_server import util


async def aquifers_files_list(request: web.Request, aquifer_id) -> web.Response:
    """aquifers_files_list

    list files found for the aquifer identified in the uri

    :param aquifer_id: 
    :type aquifer_id: str

    """
    return web.Response(status=200)


async def aquifers_list(request: web.Request, aquifer_id=None, ordering=None, search=None, limit=None, offset=None) -> web.Response:
    """aquifers_list

    return a list of aquifers

    :param aquifer_id: 
    :type aquifer_id: 
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param search: A search term.
    :type search: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    """
    return web.Response(status=200)


async def aquifers_names_list(request: web.Request, search=None) -> web.Response:
    """aquifers_names_list

    List all aquifers in a simplified format

    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def aquifers_read(request: web.Request, aquifer_id) -> web.Response:
    """aquifers_read

    return details of aquifers

    :param aquifer_id: A unique integer value identifying this aquifer.
    :type aquifer_id: int

    """
    return web.Response(status=200)
