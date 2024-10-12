from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def absolute_redirect_nget(request: web.Request, n) -> web.Response:
    """Absolutely 302 Redirects n times.

    

    :param n: 
    :type n: int

    """
    return web.Response(status=200)


async def redirect_nget(request: web.Request, n) -> web.Response:
    """302 Redirects n times.

    

    :param n: 
    :type n: int

    """
    return web.Response(status=200)


async def redirect_to_delete(request: web.Request, ) -> web.Response:
    """302/3XX Redirects to the given URL.

    


    """
    return web.Response(status=200)


async def redirect_to_get(request: web.Request, url, status_code=None) -> web.Response:
    """302/3XX Redirects to the given URL.

    

    :param url: 
    :type url: str
    :param status_code: 
    :type status_code: int

    """
    return web.Response(status=200)


async def redirect_to_patch(request: web.Request, ) -> web.Response:
    """302/3XX Redirects to the given URL.

    


    """
    return web.Response(status=200)


async def redirect_to_post(request: web.Request, url, status_code=None) -> web.Response:
    """302/3XX Redirects to the given URL.

    

    :param url: 
    :type url: str
    :param status_code: 
    :type status_code: int

    """
    return web.Response(status=200)


async def redirect_to_put(request: web.Request, url, status_code=None) -> web.Response:
    """302/3XX Redirects to the given URL.

    

    :param url: 
    :type url: str
    :param status_code: 
    :type status_code: int

    """
    return web.Response(status=200)


async def redirect_to_trace(request: web.Request, ) -> web.Response:
    """302/3XX Redirects to the given URL.

    


    """
    return web.Response(status=200)


async def relative_redirect_nget(request: web.Request, n) -> web.Response:
    """Relatively 302 Redirects n times.

    

    :param n: 
    :type n: int

    """
    return web.Response(status=200)
