from typing import List, Dict
from aiohttp import web

from openapi_server.models.entry_info_response import EntryInfoResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.info_response import InfoResponse
from openapi_server import util


async def get_entry_info_info_entry_get(request: web.Request, entry) -> web.Response:
    """Get Entry Info

    

    :param entry: 
    :type entry: str

    """
    return web.Response(status=200)


async def get_info_info_get(request: web.Request, ) -> web.Response:
    """Get Info

    


    """
    return web.Response(status=200)
