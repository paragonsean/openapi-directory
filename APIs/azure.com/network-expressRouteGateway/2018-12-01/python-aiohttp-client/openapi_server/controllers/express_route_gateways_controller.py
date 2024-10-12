from typing import List, Dict
from aiohttp import web

from openapi_server.models.express_route_gateway import ExpressRouteGateway
from openapi_server.models.express_route_gateway_list import ExpressRouteGatewayList
from openapi_server import util


async def express_route_gateways_create_or_update(request: web.Request, resource_group_name, express_route_gateway_name, api_version, subscription_id, put_express_route_gateway_parameters) -> web.Response:
    """express_route_gateways_create_or_update

    Creates or updates a ExpressRoute gateway in a specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param put_express_route_gateway_parameters: Parameters required in an ExpressRoute gateway PUT operation.
    :type put_express_route_gateway_parameters: dict | bytes

    """
    put_express_route_gateway_parameters = ExpressRouteGateway.from_dict(put_express_route_gateway_parameters)
    return web.Response(status=200)


async def express_route_gateways_delete(request: web.Request, resource_group_name, express_route_gateway_name, api_version, subscription_id) -> web.Response:
    """express_route_gateways_delete

    Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_gateways_get(request: web.Request, resource_group_name, express_route_gateway_name, api_version, subscription_id) -> web.Response:
    """express_route_gateways_get

    Fetches the details of a ExpressRoute gateway in a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param express_route_gateway_name: The name of the ExpressRoute gateway.
    :type express_route_gateway_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_gateways_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """express_route_gateways_list_by_resource_group

    Lists ExpressRoute gateways in a given resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def express_route_gateways_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """express_route_gateways_list_by_subscription

    Lists ExpressRoute gateways under a given subscription.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
