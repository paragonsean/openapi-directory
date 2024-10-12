from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_root200_response import GetRoot200Response
from openapi_server import util


async def get_root(request: web.Request, ) -> web.Response:
    """get_root

    API entry point  Provides links for: * catalog, your domain&#39;s list of datasets * opendatasoft, all datasets on the Opendatasoft network 


    """
    return web.Response(status=200)
