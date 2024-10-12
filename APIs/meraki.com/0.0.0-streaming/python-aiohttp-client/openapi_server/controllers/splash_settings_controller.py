from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_ssid_splash_settings_request import UpdateNetworkSsidSplashSettingsRequest
from openapi_server import util


async def get_network_ssid_splash_settings(request: web.Request, network_id, number) -> web.Response:
    """Display the splash page settings for the given SSID

    Display the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_ssid_splash_settings(request: web.Request, network_id, number, body=None) -> web.Response:
    """Modify the splash page settings for the given SSID

    Modify the splash page settings for the given SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSsidSplashSettingsRequest.from_dict(body)
    return web.Response(status=200)
