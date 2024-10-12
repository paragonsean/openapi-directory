from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.programmes_response import ProgrammesResponse
from openapi_server import util


async def get_collection_members(request: web.Request, x_api_key, pid, offset=None, limit=None) -> web.Response:
    """Collection Members

    Episodes and Clips from Collection 

    :param x_api_key: API_KEY
    :type x_api_key: str
    :param pid: pid
    :type pid: str
    :param offset: Paginated results offset
    :type offset: int
    :param limit: Paginated results limit
    :type limit: int

    """
    return web.Response(status=200)
