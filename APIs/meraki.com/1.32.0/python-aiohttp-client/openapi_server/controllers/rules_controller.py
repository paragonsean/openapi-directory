from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_traffic_shaping_rules_request import UpdateNetworkApplianceTrafficShapingRulesRequest
from openapi_server.models.update_network_wireless_ssid_traffic_shaping_rules_request import UpdateNetworkWirelessSsidTrafficShapingRulesRequest
from openapi_server import util


async def get_network_appliance_traffic_shaping_rules_2(request: web.Request, network_id) -> web.Response:
    """Display the traffic shaping settings rules for an MX network

    Display the traffic shaping settings rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_traffic_shaping_rules_3(request: web.Request, network_id, number) -> web.Response:
    """Display the traffic shaping settings for a SSID on an MR network

    Display the traffic shaping settings for a SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_rules_2(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic shaping settings rules for an MX network

    Update the traffic shaping settings rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_traffic_shaping_rules_3(request: web.Request, network_id, number, body=None) -> web.Response:
    """Update the traffic shaping settings for an SSID on an MR network

    Update the traffic shaping settings for an SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkWirelessSsidTrafficShapingRulesRequest.from_dict(body)
    return web.Response(status=200)
