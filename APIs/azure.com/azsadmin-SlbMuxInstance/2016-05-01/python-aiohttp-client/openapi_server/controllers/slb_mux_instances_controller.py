from typing import List, Dict
from aiohttp import web

from openapi_server.models.slb_mux_instance import SlbMuxInstance
from openapi_server.models.slb_mux_instance_list import SlbMuxInstanceList
from openapi_server import util


async def slb_mux_instances_get(request: web.Request, subscription_id, resource_group_name, location, slb_mux_instance, api_version) -> web.Response:
    """slb_mux_instances_get

    Returns the requested software load balancer multiplexer instance.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param slb_mux_instance: Name of a SLB MUX instance.
    :type slb_mux_instance: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def slb_mux_instances_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """slb_mux_instances_list

    Returns a list of all software load balancer instances at a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)
