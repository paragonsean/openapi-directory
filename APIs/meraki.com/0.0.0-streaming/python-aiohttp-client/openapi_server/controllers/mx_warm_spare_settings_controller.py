from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_warm_spare_settings_request import UpdateNetworkWarmSpareSettingsRequest
from openapi_server import util


async def get_network_warm_spare_settings(request: web.Request, network_id) -> web.Response:
    """Return MX warm spare settings

    Return MX warm spare settings

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def swap_network_warm_spare(request: web.Request, network_id) -> web.Response:
    """Swap MX primary and warm spare appliances

    Swap MX primary and warm spare appliances

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_warm_spare_settings(request: web.Request, network_id, body) -> web.Response:
    """Update MX warm spare settings

    Update MX warm spare settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWarmSpareSettingsRequest.from_dict(body)
    return web.Response(status=200)
