from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.pack import Pack
from openapi_server.models.pack_response import PackResponse
from openapi_server import util


async def root_post(request: web.Request, pack=None) -> web.Response:
    """root_post

    a pure-JSON endpoint for packing requests. 

    :param pack: complete set of items, boxes, and parameters to pack.
    :type pack: dict | bytes

    """
    pack = Pack.from_dict(pack)
    return web.Response(status=200)
