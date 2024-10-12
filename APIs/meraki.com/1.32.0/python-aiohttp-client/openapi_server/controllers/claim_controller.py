from typing import List, Dict
from aiohttp import web

from openapi_server.models.vmx_network_devices_claim_request import VmxNetworkDevicesClaimRequest
from openapi_server import util


async def vmx_network_devices_claim_2(request: web.Request, network_id, body) -> web.Response:
    """Claim a vMX into a network

    Claim a vMX into a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = VmxNetworkDevicesClaimRequest.from_dict(body)
    return web.Response(status=200)
