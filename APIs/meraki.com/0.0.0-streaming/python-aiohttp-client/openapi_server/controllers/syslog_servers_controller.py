from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_syslog_servers_request import UpdateNetworkSyslogServersRequest
from openapi_server import util


async def get_network_syslog_servers(request: web.Request, network_id) -> web.Response:
    """List the syslog servers for a network

    List the syslog servers for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_syslog_servers(request: web.Request, network_id, body) -> web.Response:
    """Update the syslog servers for a network

    Update the syslog servers for a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSyslogServersRequest.from_dict(body)
    return web.Response(status=200)
