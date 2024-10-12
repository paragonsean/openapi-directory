from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response import GetNetworkApplianceTrafficShapingUplinkSelection200Response
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_selection_request import UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest
from openapi_server import util


async def get_network_appliance_traffic_shaping_uplink_selection_2(request: web.Request, network_id) -> web.Response:
    """Show uplink selection settings for an MX network

    Show uplink selection settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_uplink_selection_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update uplink selection settings for an MX network

    Update uplink selection settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.from_dict(body)
    return web.Response(status=200)
