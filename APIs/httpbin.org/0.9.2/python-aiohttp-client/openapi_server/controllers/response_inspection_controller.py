from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def cache_get(request: web.Request, if_modified_since=None, if_none_match=None) -> web.Response:
    """Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.

    

    :param if_modified_since: 
    :type if_modified_since: str
    :param if_none_match: 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def cache_value_get(request: web.Request, value) -> web.Response:
    """Sets a Cache-Control header for n seconds.

    

    :param value: 
    :type value: int

    """
    return web.Response(status=200)


async def etag_etag_get(request: web.Request, etag, if_none_match=None, if_match=None) -> web.Response:
    """Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.

    

    :param etag: Automatically added
    :type etag: str
    :param if_none_match: 
    :type if_none_match: str
    :param if_match: 
    :type if_match: str

    """
    return web.Response(status=200)


async def response_headers_get(request: web.Request, freeform=None) -> web.Response:
    """Returns a set of response headers from the query string.

    

    :param freeform: 
    :type freeform: Dict[str, str]

    """
    return web.Response(status=200)


async def response_headers_post(request: web.Request, freeform=None) -> web.Response:
    """Returns a set of response headers from the query string.

    

    :param freeform: 
    :type freeform: Dict[str, str]

    """
    return web.Response(status=200)
