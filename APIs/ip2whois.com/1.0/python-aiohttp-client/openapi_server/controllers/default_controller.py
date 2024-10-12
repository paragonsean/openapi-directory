from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def root_get(request: web.Request, domain, key, format=None) -> web.Response:
    """root_get

    Lookup WHOIS information

    :param domain: Domain name for lookup purpose.
    :type domain: str
    :param key: API key.
    :type key: str
    :param format: Returns the API response in json (default) or xml format.
    :type format: str

    """
    return web.Response(status=200)
