from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_proxy_result import MultiProxyResult
from openapi_server.models.proxy import Proxy
from openapi_server.models.proxy_create import ProxyCreate
from openapi_server.models.proxy_result import ProxyResult
from openapi_server import util


async def proxy_get(request: web.Request, filters=None) -> web.Response:
    """list proxies

    Get a list of proxies

    :param filters: A JSON encoded array of ProxyFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any ProxyFilter will be included. 
    :type filters: str

    """
    return web.Response(status=200)


async def proxy_post(request: web.Request, proxy) -> web.Response:
    """create proxy

    Create a new proxy

    :param proxy: the proxy to create
    :type proxy: dict | bytes

    """
    proxy = ProxyCreate.from_dict(proxy)
    return web.Response(status=200)


async def proxy_proxy_key_delete(request: web.Request, proxy_key, checksum) -> web.Response:
    """delete proxy

    Delete existing proxy

    :param proxy_key: the proxy key
    :type proxy_key: str
    :param checksum: the current checksum of the proxy to be deleted
    :type checksum: str

    """
    return web.Response(status=200)


async def proxy_proxy_key_get(request: web.Request, proxy_key) -> web.Response:
    """get proxy

    Get details for a single proxy

    :param proxy_key: the proxy key
    :type proxy_key: str

    """
    return web.Response(status=200)
