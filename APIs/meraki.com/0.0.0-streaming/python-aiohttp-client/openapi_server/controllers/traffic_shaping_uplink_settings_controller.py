from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_uplink_settings_request import UpdateNetworkUplinkSettingsRequest
from openapi_server import util


async def get_network_uplink_settings(request: web.Request, network_id) -> web.Response:
    """Returns the uplink settings for your MX network.

    Returns the uplink settings for your MX network.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_uplink_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Updates the uplink settings for your MX network.

    Updates the uplink settings for your MX network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkUplinkSettingsRequest.from_dict(body)
    return web.Response(status=200)
