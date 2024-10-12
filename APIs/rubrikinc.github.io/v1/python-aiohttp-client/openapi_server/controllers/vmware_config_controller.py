from typing import List, Dict
from aiohttp import web

from openapi_server.models.preferred_cdp_network_protocol import PreferredCdpNetworkProtocol
from openapi_server.models.preferred_cdp_network_protocol_object import PreferredCdpNetworkProtocolObject
from openapi_server.models.vmware_network_collection import VmwareNetworkCollection
from openapi_server import util


async def get_preferred_cdp_network_protocol(request: web.Request, ) -> web.Response:
    """Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer

    Returns the current preference of CDM between IPv4 and IPv6 for CDP data transfer.


    """
    return web.Response(status=200)


async def get_vmware_recovery_networks(request: web.Request, compute_resource_id, compute_resource_type) -> web.Response:
    """Get all the VMware recovery networks for a compute resource ID

    Get all the networks for snapshot recovery for the specified compute resource.

    :param compute_resource_id: Get VMware recovery networks for the compute resource ID.
    :type compute_resource_id: str
    :param compute_resource_type: The type of the compute resource.
    :type compute_resource_type: str

    """
    return web.Response(status=200)


async def set_preferred_cdp_network_protocol(request: web.Request, body) -> web.Response:
    """Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer

    Set the current preference of CDM between IPv4 and IPv6 for CDP data transfer.

    :param body: The preferred network protocol to use for transferring CDP data.
    :type body: 

    """
    return web.Response(status=200)
