from typing import List, Dict
from aiohttp import web

from openapi_server.models.update_network_appliance_connectivity_monitoring_destinations_request import UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest
from openapi_server.models.update_network_cellular_gateway_connectivity_monitoring_destinations_request import UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest
from openapi_server import util


async def get_network_appliance_connectivity_monitoring_destinations_1(request: web.Request, network_id) -> web.Response:
    """Return the connectivity testing destinations for an MX network

    Return the connectivity testing destinations for an MX network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_cellular_gateway_connectivity_monitoring_destinations_1(request: web.Request, network_id) -> web.Response:
    """Return the connectivity testing destinations for an MG network

    Return the connectivity testing destinations for an MG network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_connectivity_monitoring_destinations_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the connectivity testing destinations for an MX network

    Update the connectivity testing destinations for an MX network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkApplianceConnectivityMonitoringDestinationsRequest.from_dict(body)
    return web.Response(status=200)


async def update_network_cellular_gateway_connectivity_monitoring_destinations_1(request: web.Request, network_id, body=None) -> web.Response:
    """Update the connectivity testing destinations for an MG network

    Update the connectivity testing destinations for an MG network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkCellularGatewayConnectivityMonitoringDestinationsRequest.from_dict(body)
    return web.Response(status=200)
