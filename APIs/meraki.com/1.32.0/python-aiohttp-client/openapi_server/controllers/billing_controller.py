from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_wireless_billing_request import UpdateNetworkWirelessBillingRequest
from openapi_server import util


async def get_network_wireless_billing_1(request: web.Request, network_id) -> web.Response:
    """Return the billing settings of this network

    Return the billing settings of this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_wireless_billing_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the billing settings

    Update the billing settings

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessBillingRequest.from_dict(body)
    return web.Response(status=200)
