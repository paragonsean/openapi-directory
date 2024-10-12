from typing import List, Dict
from aiohttp import web

from openapi_server.models.baskets import Baskets
from openapi_server.models.config import Config
from openapi_server.models.service_stats import ServiceStats
from openapi_server.models.token import Token
from openapi_server import util


async def api_baskets_get(request: web.Request, max=None, skip=None, q=None) -> web.Response:
    """Get baskets

    Fetches a list of basket names managed by service. Require master token.

    :param max: Maximum number of basket names to return; default 20
    :type max: int
    :param skip: Number of basket names to skip; default 0
    :type skip: int
    :param q: Query string to filter result, only those basket names that match the query will be included in response
    :type q: str

    """
    return web.Response(status=200)


async def api_baskets_name_delete(request: web.Request, name) -> web.Response:
    """Delete basket

    Permanently deletes this basket and all collected requests.

    :param name: The basket name
    :type name: str

    """
    return web.Response(status=200)


async def api_baskets_name_get(request: web.Request, name) -> web.Response:
    """Get basket settings

    Retrieves configuration settings of this basket.

    :param name: The basket name
    :type name: str

    """
    return web.Response(status=200)


async def api_baskets_name_post(request: web.Request, name, config=None) -> web.Response:
    """Create new basket

    Creates a new basket with this name.

    :param name: The name of new basket
    :type name: str
    :param config: Basket configuration
    :type config: dict | bytes

    """
    config = Config.from_dict(config)
    return web.Response(status=200)


async def api_baskets_name_put(request: web.Request, name, config) -> web.Response:
    """Update basket settings

    Updates configuration settings of this basket.  Special configuration parameters for request forwarding:   * &#x60;insecure_tls&#x60; controls certificate verification when forwarding requests. Setting this parameter to &#x60;true&#x60;   allows to forward collected HTTP requests via HTTPS protocol even if the forward end-point is configured with   self-signed TLS/SSL certificate. **Warning:** enabling this feature has known security implications.   * &#x60;expand_path&#x60; changes the logic of constructing taget URL when forwarding requests. If this parameter is   set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. For   example, a basket with name **server1** is configured to forward all requests to &#x60;http://server1.intranet:8001/myservice&#x60;   and it has received an HTTP request like &#x60;GET http://baskets.example.com/server1/component/123/events?status&#x3D;OK&#x60;   then depending on &#x60;expand_path&#x60; settings the request will be forwarded to:     * &#x60;true&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice/component/123/events?status&#x3D;OK&#x60;     * &#x60;false&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice?status&#x3D;OK&#x60; 

    :param name: The basket name
    :type name: str
    :param config: New configuration to apply
    :type config: dict | bytes

    """
    config = Config.from_dict(config)
    return web.Response(status=200)


async def api_stats_get(request: web.Request, max=None) -> web.Response:
    """Get baskets statistics

    Get service statistics about baskets and collected HTTP requests. Require master token.

    :param max: Maximum number of basket names to return; default 5
    :type max: int

    """
    return web.Response(status=200)


async def baskets_get(request: web.Request, max=None, skip=None, q=None) -> web.Response:
    """Get baskets

    Fetches a list of basket names managed by service. Require master token.

    :param max: Maximum number of basket names to return; default 20
    :type max: int
    :param skip: Number of basket names to skip; default 0
    :type skip: int
    :param q: Query string to filter result, only those basket names that match the query will be included in response
    :type q: str

    """
    return web.Response(status=200)


async def baskets_name_delete(request: web.Request, name) -> web.Response:
    """Delete basket

    Permanently deletes this basket and all collected requests.

    :param name: The basket name
    :type name: str

    """
    return web.Response(status=200)


async def baskets_name_get(request: web.Request, name) -> web.Response:
    """Get basket settings

    Retrieves configuration settings of this basket.

    :param name: The basket name
    :type name: str

    """
    return web.Response(status=200)


async def baskets_name_post(request: web.Request, name, config=None) -> web.Response:
    """Create new basket

    Creates a new basket with this name.

    :param name: The name of new basket
    :type name: str
    :param config: Basket configuration
    :type config: dict | bytes

    """
    config = Config.from_dict(config)
    return web.Response(status=200)


async def baskets_name_put(request: web.Request, name, config) -> web.Response:
    """Update basket settings

    Updates configuration settings of this basket.  Special configuration parameters for request forwarding:   * &#x60;insecure_tls&#x60; controls certificate verification when forwarding requests. Setting this parameter to &#x60;true&#x60;   allows to forward collected HTTP requests via HTTPS protocol even if the forward end-point is configured with   self-signed TLS/SSL certificate. **Warning:** enabling this feature has known security implications.   * &#x60;expand_path&#x60; changes the logic of constructing taget URL when forwarding requests. If this parameter is   set to &#x60;true&#x60; the forward URL path will be expanded when original HTTP request contains compound path. For   example, a basket with name **server1** is configured to forward all requests to &#x60;http://server1.intranet:8001/myservice&#x60;   and it has received an HTTP request like &#x60;GET http://baskets.example.com/server1/component/123/events?status&#x3D;OK&#x60;   then depending on &#x60;expand_path&#x60; settings the request will be forwarded to:     * &#x60;true&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice/component/123/events?status&#x3D;OK&#x60;     * &#x60;false&#x60; &#x3D;&gt; &#x60;GET http://server1.intranet:8001/myservice?status&#x3D;OK&#x60; 

    :param name: The basket name
    :type name: str
    :param config: New configuration to apply
    :type config: dict | bytes

    """
    config = Config.from_dict(config)
    return web.Response(status=200)
