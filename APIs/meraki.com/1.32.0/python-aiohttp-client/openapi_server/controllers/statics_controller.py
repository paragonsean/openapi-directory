from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_appliance_prefixes_delegated_static_request import CreateNetworkAppliancePrefixesDelegatedStaticRequest
from openapi_server.models.get_network_appliance_prefixes_delegated_statics200_response_inner import GetNetworkAppliancePrefixesDelegatedStatics200ResponseInner
from openapi_server.models.update_network_appliance_prefixes_delegated_static_request import UpdateNetworkAppliancePrefixesDelegatedStaticRequest
from openapi_server import util


async def create_network_appliance_prefixes_delegated_static_3(request: web.Request, network_id, body) -> web.Response:
    """Add a static delegated prefix from a network

    Add a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkAppliancePrefixesDelegatedStaticRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_appliance_prefixes_delegated_static_3(request: web.Request, network_id, static_delegated_prefix_id) -> web.Response:
    """Delete a static delegated prefix from a network

    Delete a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param static_delegated_prefix_id: 
    :type static_delegated_prefix_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_prefixes_delegated_static_3(request: web.Request, network_id, static_delegated_prefix_id) -> web.Response:
    """Return a static delegated prefix from a network

    Return a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param static_delegated_prefix_id: 
    :type static_delegated_prefix_id: str

    """
    return web.Response(status=200)


async def get_network_appliance_prefixes_delegated_statics_3(request: web.Request, network_id) -> web.Response:
    """List static delegated prefixes for a network

    List static delegated prefixes for a network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_appliance_prefixes_delegated_static_3(request: web.Request, network_id, static_delegated_prefix_id, body=None) -> web.Response:
    """Update a static delegated prefix from a network

    Update a static delegated prefix from a network

    :param network_id: 
    :type network_id: str
    :param static_delegated_prefix_id: 
    :type static_delegated_prefix_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkAppliancePrefixesDelegatedStaticRequest.from_dict(body)
    return web.Response(status=200)
