from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_webhooks_http_server_request import CreateNetworkWebhooksHttpServerRequest
from openapi_server.models.get_network_webhooks_http_servers200_response_inner import GetNetworkWebhooksHttpServers200ResponseInner
from openapi_server.models.update_network_webhooks_http_server_request import UpdateNetworkWebhooksHttpServerRequest
from openapi_server import util


async def create_network_webhooks_http_server_2(request: web.Request, network_id, body) -> web.Response:
    """Add an HTTP server to a network

    Add an HTTP server to a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkWebhooksHttpServerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_webhooks_http_server_2(request: web.Request, network_id, http_server_id) -> web.Response:
    """Delete an HTTP server from a network

    Delete an HTTP server from a network

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_http_server_2(request: web.Request, network_id, http_server_id) -> web.Response:
    """Return an HTTP server for a network

    Return an HTTP server for a network

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str

    """
    return web.Response(status=200)


async def get_network_webhooks_http_servers_2(request: web.Request, network_id) -> web.Response:
    """List the HTTP servers for a network

    List the HTTP servers for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_webhooks_http_server_2(request: web.Request, network_id, http_server_id, body=None) -> web.Response:
    """Update an HTTP server

    Update an HTTP server. To change a URL, create a new HTTP server.

    :param network_id: 
    :type network_id: str
    :param http_server_id: 
    :type http_server_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWebhooksHttpServerRequest.from_dict(body)
    return web.Response(status=200)
