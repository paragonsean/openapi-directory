from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response import GetNetworkApplianceTrafficShapingUplinkBandwidth200Response
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_bandwidth_request import UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest
from openapi_server import util


async def get_network_appliance_traffic_shaping_uplink_bandwidth_2(request: web.Request, network_id) -> web.Response:
    """Returns the uplink bandwidth limits for your MX network

    Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_uplink_bandwidth_2(request: web.Request, network_id, body=None) -> web.Response:
    """Updates the uplink bandwidth settings for your MX network.

    Updates the uplink bandwidth settings for your MX network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.from_dict(body)
    return web.Response(status=200)
