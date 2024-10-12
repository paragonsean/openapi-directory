from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cookies_delete_get(request: web.Request, freeform=None) -> web.Response:
    """Deletes cookie(s) as provided by the query string and redirects to cookie list.

    

    :param freeform: 
    :type freeform: Dict[str, str]

    """
    return web.Response(status=200)


async def cookies_get(request: web.Request, ) -> web.Response:
    """Returns cookie data.

    


    """
    return web.Response(status=200)


async def cookies_set_get(request: web.Request, freeform=None) -> web.Response:
    """Sets cookie(s) as provided by the query string and redirects to cookie list.

    

    :param freeform: 
    :type freeform: Dict[str, str]

    """
    return web.Response(status=200)


async def cookies_set_name_value_get(request: web.Request, name, value) -> web.Response:
    """Sets a cookie and redirects to cookie list.

    

    :param name: 
    :type name: str
    :param value: 
    :type value: str

    """
    return web.Response(status=200)
