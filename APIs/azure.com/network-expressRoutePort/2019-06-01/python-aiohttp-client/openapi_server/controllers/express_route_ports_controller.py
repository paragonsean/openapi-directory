from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_port import ExpressRoutePort
from openapi_server.models.express_route_port_list_result import ExpressRoutePortListResult
from openapi_server.models.express_route_ports_update_tags_request import ExpressRoutePortsUpdateTagsRequest
from openapi_server import util


async def express_route_ports_create_or_update(request: web.Request, subscription_id, api_version, resource_group_name, express_route_port_name, parameters) -> web.Response:
    """express_route_ports_create_or_update

    Creates or updates the specified ExpressRoutePort resource.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_port_name: The name of the ExpressRoutePort resource.
    :type express_route_port_name: str
    :param parameters: Parameters supplied to the create ExpressRoutePort operation.
    :type parameters: dict | bytes

    """
    parameters = ExpressRoutePort.from_dict(parameters)
    return web.Response(status=200)


async def express_route_ports_delete(request: web.Request, subscription_id, api_version, resource_group_name, express_route_port_name) -> web.Response:
    """express_route_ports_delete

    Deletes the specified ExpressRoutePort resource.

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


async def express_route_ports_get(request: web.Request, subscription_id, api_version, resource_group_name, express_route_port_name) -> web.Response:
    """express_route_ports_get

    Retrieves the requested ExpressRoutePort resource.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_port_name: The name of ExpressRoutePort.
    :type express_route_port_name: str

    """
    return web.Response(status=200)


async def express_route_ports_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """express_route_ports_list

    List all the ExpressRoutePort resources in the specified subscription.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def express_route_ports_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """express_route_ports_list_by_resource_group

    List all the ExpressRoutePort resources in the specified resource group.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def express_route_ports_update_tags(request: web.Request, subscription_id, api_version, resource_group_name, express_route_port_name, parameters) -> web.Response:
    """express_route_ports_update_tags

    Update ExpressRoutePort tags.

    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API version.
    :type api_version: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_port_name: The name of the ExpressRoutePort resource.
    :type express_route_port_name: str
    :param parameters: Parameters supplied to update ExpressRoutePort resource tags.
    :type parameters: dict | bytes

    """
    parameters = ExpressRoutePortsUpdateTagsRequest.from_dict(parameters)
    return web.Response(status=200)
