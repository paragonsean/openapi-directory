from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_wireless_ssid_eap_override200_response import GetNetworkWirelessSsidEapOverride200Response
from openapi_server.models.update_network_wireless_ssid_eap_override_request import UpdateNetworkWirelessSsidEapOverrideRequest
from openapi_server import util


async def get_network_wireless_ssid_eap_override_2(request: web.Request, network_id, number) -> web.Response:
    """Return the EAP overridden parameters for an SSID

    Return the EAP overridden parameters for an SSID

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_wireless_ssid_eap_override_2(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the EAP overridden parameters for an SSID.

    Update the EAP overridden parameters for an SSID.

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidEapOverrideRequest.from_dict(body)
    return web.Response(status=200)
