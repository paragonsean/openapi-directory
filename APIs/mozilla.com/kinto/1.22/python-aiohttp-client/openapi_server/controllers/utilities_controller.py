from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def contribute(request: web.Request, ) -> web.Response:
    """contribute

    


    """
    return web.Response(status=200)


async def get_openapi_spec(request: web.Request, ) -> web.Response:
    """get_openapi_spec

    


    """
    return web.Response(status=200)


async def heartbeat(request: web.Request, ) -> web.Response:
    """heartbeat

    


    """
    return web.Response(status=200)


async def lbheartbeat(request: web.Request, ) -> web.Response:
    """lbheartbeat

    


    """
    return web.Response(status=200)


async def server_info(request: web.Request, ) -> web.Response:
    """server_info

    


    """
    return web.Response(status=200)


async def version(request: web.Request, ) -> web.Response:
    """version

    


    """
    return web.Response(status=200)
