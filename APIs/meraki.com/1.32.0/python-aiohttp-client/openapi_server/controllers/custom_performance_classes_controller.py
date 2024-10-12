from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_appliance_traffic_shaping_custom_performance_class_request import CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server.models.update_network_appliance_traffic_shaping_custom_performance_class_request import UpdateNetworkApplianceTrafficShapingCustomPerformanceClassRequest
from openapi_server import util


async def create_network_appliance_traffic_shaping_custom_performance_class_2(request: web.Request, network_id, body) -> web.Response:
    """Add a custom performance class for an MX network

    Add a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkApplianceTrafficShapingCustomPerformanceClassRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_appliance_traffic_shaping_custom_performance_class_2(request: web.Request, network_id, custom_performance_class_id) -> web.Response:
    """Delete a custom performance class from an MX network

    Delete a custom performance class from an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_custom_performance_class_2(request: web.Request, network_id, custom_performance_class_id) -> web.Response:
    """Return a custom performance class for an MX network

    Return a custom performance class for an MX network

    :param network_id: 
    :type network_id: str
    :param custom_performance_class_id: 
    :type custom_performance_class_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_traffic_shaping_custom_performance_classes_2(request: web.Request, network_id) -> web.Response:
    """List all custom performance classes for an MX network

    List all custom performance classes for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_traffic_shaping_custom_performance_class_2(request: web.Request, network_id, custom_performance_class_id, body=None) -> web.Response:
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
