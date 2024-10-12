from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server import util


async def get_site_metadata(request: web.Request, site_id) -> web.Response:
    """get_site_metadata

    

    :param site_id: 
    :type site_id: str

    """
    return web.Response(status=200)


async def update_site_metadata(request: web.Request, site_id, metadata) -> web.Response:
    """update_site_metadata

    

    :param site_id: 
    :type site_id: str
    :param metadata: 
    :type metadata: 

    """
    return web.Response(status=200)
