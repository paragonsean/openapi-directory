from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def root_get(request: web.Request, ip, key, package=None, format=None) -> web.Response:
    """root_get

    Check if an IP address is proxy

    :param ip: IP address (IPv4) for lookup purpose. If not present, the server IP address will be used for the lookup.
    :type ip: str
    :param key: API key. Please sign up free trial license key at ip2location.com
    :type key: str
    :param package: Package name from PX1 to PX11. If not present, the web service will assume the PX1 package query.
    :type package: str
    :param format: If not present, json format will be returned as the search result.
    :type format: str

    """
    return web.Response(status=200)
