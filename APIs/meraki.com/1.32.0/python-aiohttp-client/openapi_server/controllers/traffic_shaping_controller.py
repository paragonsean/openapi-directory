from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_appliance_traffic_shaping_custom_performance_class_request import CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_bandwidth200_response import GetNetworkApplianceTrafficShapingUplinkBandwidth200Response
from openapi_server.models.get_network_appliance_traffic_shaping_uplink_selection200_response import GetNetworkApplianceTrafficShapingUplinkSelection200Response
from openapi_server.models.update_network_appliance_traffic_shaping_custom_performance_class_request import UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.update_network_appliance_traffic_shaping_request import UpdateNetworkApplianceTrafficShapingRequest
from openapi_server.models.update_network_appliance_traffic_shaping_rules_request import UpdateNetworkApplianceTrafficShapingRulesRequest
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_bandwidth_request import UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest
from openapi_server.models.update_network_appliance_traffic_shaping_uplink_selection_request import UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest
from openapi_server.models.update_network_wireless_ssid_traffic_shaping_rules_request import UpdateNetworkWirelessSsidTrafficShapingRulesRequest
from openapi_server import util


async def create_network_appliance_traffic_shaping_custom_performance_class_1(request: web.Request, network_id, body) -> web.Response:
    """Add a custom performance class for an MX network

    Add a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_appliance_traffic_shaping_custom_performance_class_1(request: web.Request, network_id, custom_performance_class_id) -> web.Response:
    """Delete a custom performance class from an MX network

    Delete a custom performance class from an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_1(request: web.Request, network_id) -> web.Response:
    """Display the traffic shaping settings for an MX network

    Display the traffic shaping settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_custom_performance_class_1(request: web.Request, network_id, custom_performance_class_id) -> web.Response:
    """Return a custom performance class for an MX network

    Return a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_custom_performance_classes_1(request: web.Request, network_id) -> web.Response:
    """List all custom performance classes for an MX network

    List all custom performance classes for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_rules_1(request: web.Request, network_id) -> web.Response:
    """Display the traffic shaping settings rules for an MX network

    Display the traffic shaping settings rules for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_uplink_bandwidth_1(request: web.Request, network_id) -> web.Response:
    """Returns the uplink bandwidth limits for your MX network

    Returns the uplink bandwidth limits for your MX network. This may not reflect the affected device&#39;s hardware capabilities.  For more information on your device&#39;s hardware capabilities, please consult our MX Family Datasheet - [https://meraki.cisco.com/product-collateral/mx-family-datasheet/?file]

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_uplink_selection_1(request: web.Request, network_id) -> web.Response:
    """Show uplink selection settings for an MX network

    Show uplink selection settings for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic_shaping_application_categories_1(request: web.Request, network_id) -> web.Response:
    """Returns the application categories for traffic shaping rules.

    Returns the application categories for traffic shaping rules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_traffic_shaping_dscp_tagging_options_1(request: web.Request, network_id) -> web.Response:
    """Returns the available DSCP tagging options for your traffic shaping rules.

    Returns the available DSCP tagging options for your traffic shaping rules.

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_wireless_ssid_traffic_shaping_rules_2(request: web.Request, network_id, number) -> web.Response:
    """Display the traffic shaping settings for a SSID on an MR network

    Display the traffic shaping settings for a SSID on an MR network

    :param network_id: 
    :type network_id: str
    :param number: 
    :type number: str

    """
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic shaping settings for an MX network

    Update the traffic shaping settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_custom_performance_class_1(request: web.Request, network_id, custom_performance_class_id, body=None) -> web.Response:
    """Update a custom performance class for an MX network

    Update a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_rules_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the traffic shaping settings rules for an MX network

    Update the traffic shaping settings rules for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingRulesRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_uplink_bandwidth_1(request: web.Request, network_id, body=None) -> web.Response:
    """Updates the uplink bandwidth settings for your MX network.

    Updates the uplink bandwidth settings for your MX network.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingUplinkBandwidthRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_uplink_selection_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update uplink selection settings for an MX network

    Update uplink selection settings for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceTrafficShapingUplinkSelectionRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_wireless_ssid_traffic_shaping_rules_2(request: web.Request, network_id, number, body=None) -> web.Response:
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
