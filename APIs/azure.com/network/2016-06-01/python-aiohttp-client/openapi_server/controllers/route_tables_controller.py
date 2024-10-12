from typing import List, Dict
from aiohttp import web

from openapi_server.models.route_table import RouteTable
from openapi_server.models.route_table_list_result import RouteTableListResult
from openapi_server import util


async def route_tables_create_or_update(request: web.Request, resource_group_name, route_table_name, api_version, subscription_id, parameters) -> web.Response:
    """route_tables_create_or_update

    The Put RouteTable operation creates/updates a route table in the specified resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create/update Route Table operation
    :type parameters: dict | bytes

    """
    parameters = RouteTable.from_dict(parameters)
    return web.Response(status=200)


async def route_tables_delete(request: web.Request, resource_group_name, route_table_name, api_version, subscription_id) -> web.Response:
    """route_tables_delete

    The Delete RouteTable operation deletes the specified Route Table

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_tables_get(request: web.Request, resource_group_name, route_table_name, api_version, subscription_id, expand=None) -> web.Response:
    """route_tables_get

    The Get RouteTables operation retrieves information about the specified route table.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param route_table_name: The name of the route table.
    :type route_table_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: expand references resources.
    :type expand: str

    """
    return web.Response(status=200)


async def route_tables_list(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """route_tables_list

    The list RouteTables returns all route tables in a resource group

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def route_tables_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """route_tables_list_all

    The list RouteTables returns all route tables in a subscription

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
