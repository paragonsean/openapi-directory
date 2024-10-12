from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.territories_response import TerritoriesResponse
from openapi_server import util


async def territories_get_collection(request: web.Request, fields_territories=None, limit=None) -> web.Response:
    """territories_get_collection

    

    :param fields_territories: the fields to include for returned resources of type territories
    :type fields_territories: List[str]
    :param limit: maximum resources per page
    :type limit: int

    """
    return web.Response(status=200)
