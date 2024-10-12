from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_link import ExpressRouteLink
from openapi_server.models.express_route_link_list_result import ExpressRouteLinkListResult
from openapi_server import util


async def express_route_links_get(request: web.Request, subscription_id, api_version, resource_group_name, express_route_port_name, link_name) -> web.Response:
    """express_route_links_get

    Retrieves the specified ExpressRouteLink resource.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_port_name: The name of the ExpressRoutePort resource.
    :type express_route_port_name: str
    :param link_name: The name of the ExpressRouteLink resource.
    :type link_name: str

    """
    return web.Response(status=200)


async def express_route_links_list(request: web.Request, subscription_id, api_version, resource_group_name, express_route_port_name) -> web.Response:
    """express_route_links_list

    Retrieve the ExpressRouteLink sub-resources of the specified ExpressRoutePort resource.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_port_name: The name of the ExpressRoutePort resource.
    :type express_route_port_name: str

    """
    return web.Response(status=200)
