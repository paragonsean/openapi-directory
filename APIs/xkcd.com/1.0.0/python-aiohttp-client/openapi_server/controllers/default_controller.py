from typing import List, Dict
from aiohttp import web

from openapi_server.models.comic import Comic
from openapi_server import util


async def comic_id_info0_json_get(request: web.Request, comic_id) -> web.Response:
    """comic_id_info0_json_get

    Fetch comics and metadata  by comic id. 

    :param comic_id: 
    :type comic_id: 

    """
    return web.Response(status=200)


async def info0_json_get(request: web.Request, ) -> web.Response:
    """info0_json_get

    Fetch current comic and metadata. 


    """
    return web.Response(status=200)
