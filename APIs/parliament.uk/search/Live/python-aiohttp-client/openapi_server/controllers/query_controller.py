from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def query_extension_get(request: web.Request, extension, q, start=None, count=None, subdomains=None, in_url_prefixes=None) -> web.Response:
    """Search results

    

    :param extension: extension
    :type extension: str
    :param q: 
    :type q: str
    :param start: 
    :type start: 
    :param count: 
    :type count: 
    :param subdomains: 
    :type subdomains: str
    :param in_url_prefixes: 
    :type in_url_prefixes: str

    """
    return web.Response(status=200)


async def query_get(request: web.Request, q, start=None, count=None, subdomains=None, in_url_prefixes=None) -> web.Response:
    """Search results

    

    :param q: 
    :type q: str
    :param start: 
    :type start: 
    :param count: 
    :type count: 
    :param subdomains: 
    :type subdomains: str
    :param in_url_prefixes: 
    :type in_url_prefixes: str

    """
    return web.Response(status=200)
