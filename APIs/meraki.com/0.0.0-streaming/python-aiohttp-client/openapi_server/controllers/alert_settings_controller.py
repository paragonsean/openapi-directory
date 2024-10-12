from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_alert_settings_request import UpdateNetworkAlertSettingsRequest
from openapi_server import util


async def get_network_alert_settings(request: web.Request, network_id) -> web.Response:
    """Return the alert configuration for this network

    Return the alert configuration for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_alert_settings(request: web.Request, network_id, body=None) -> web.Response:
    """Update the alert configuration for this network

    Update the alert configuration for this network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAlertSettingsRequest.from_dict(body)
    return web.Response(status=200)
