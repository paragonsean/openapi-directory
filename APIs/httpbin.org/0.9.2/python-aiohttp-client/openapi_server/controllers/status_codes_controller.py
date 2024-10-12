from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def status_codes_delete(request: web.Request, codes) -> web.Response:
    """Return status code or random status code if more than one are given

    

    :param codes: 
    :type codes: str

    """
    return web.Response(status=200)


async def status_codes_get(request: web.Request, codes) -> web.Response:
    """Return status code or random status code if more than one are given

    

    :param codes: 
    :type codes: str

    """
    return web.Response(status=200)


async def status_codes_patch(request: web.Request, codes) -> web.Response:
    """Return status code or random status code if more than one are given

    

    :param codes: 
    :type codes: str

    """
    return web.Response(status=200)


async def status_codes_post(request: web.Request, codes) -> web.Response:
    """Return status code or random status code if more than one are given

    

    :param codes: 
    :type codes: str

    """
    return web.Response(status=200)


async def status_codes_put(request: web.Request, codes) -> web.Response:
    """Return status code or random status code if more than one are given

    

    :param codes: 
    :type codes: str

    """
    return web.Response(status=200)


async def status_codes_trace(request: web.Request, codes) -> web.Response:
    """Return status code or random status code if more than one are given

    

    :param codes: 
    :type codes: str

    """
    return web.Response(status=200)
