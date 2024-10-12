from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_gateway_definition import ConnectionGatewayDefinition
from openapi_server.models.connection_gateway_definition_collection import ConnectionGatewayDefinitionCollection
from openapi_server.models.connection_gateway_installation_definition import ConnectionGatewayInstallationDefinition
from openapi_server.models.connection_gateway_installation_definition_collection import ConnectionGatewayInstallationDefinitionCollection
from openapi_server import util


async def connection_gateway_installations_get(request: web.Request, subscription_id, location, gateway_id, api_version) -> web.Response:
    """Gets an installed gateway that the user is an admin of

    Get a specific installed gateway that the user is an admin of, in a specific subscription and at a certain location

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param gateway_id: Gateway ID
    :type gateway_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_gateway_installations_list(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """Gets a list of installed gateways that the user is an admin of

    Gets a list of installed gateways that the user is an admin of, in a specific subscription and at a certain location

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param location: The location
    :type location: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_gateways_create_or_update(request: web.Request, subscription_id, resource_group_name, connection_gateway_name, api_version, connection_gateway) -> web.Response:
    """Replaces a specific gateway

    Creates or updates a specific gateway for under a subscription and in a specific resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_gateway_name: The connection gateway name
    :type connection_gateway_name: str
    :param api_version: API Version
    :type api_version: str
    :param connection_gateway: The connection gateway
    :type connection_gateway: dict | bytes

    """
    connection_gateway = ConnectionGatewayDefinition.from_dict(connection_gateway)
    return web.Response(status=200)


async def connection_gateways_delete(request: web.Request, subscription_id, resource_group_name, connection_gateway_name, api_version) -> web.Response:
    """Deletes a specific gateway

    Deletes a specific gateway for under a subscription and in a specific resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_gateway_name: The connection gateway name
    :type connection_gateway_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_gateways_get(request: web.Request, subscription_id, resource_group_name, connection_gateway_name, api_version) -> web.Response:
    """Gets a specific gateway

    Gets a specific gateway under a subscription and in a specific resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_gateway_name: The connection gateway name
    :type connection_gateway_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_gateways_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Lists all of the connection gateways

    Gets a list of gateways under a subscription

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_gateways_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """Lists all of the connection gateways

    Gets a list of gateways under a subscription and in a specific resource group

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def connection_gateways_update(request: web.Request, subscription_id, resource_group_name, connection_gateway_name, api_version, connection_gateway) -> web.Response:
    """Updates a specific gateway

    Updates a connection gateway&#39;s tags

    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param connection_gateway_name: The connection gateway name
    :type connection_gateway_name: str
    :param api_version: API Version
    :type api_version: str
    :param connection_gateway: The connection gateway
    :type connection_gateway: dict | bytes

    """
    connection_gateway = ConnectionGatewayDefinition.from_dict(connection_gateway)
    return web.Response(status=200)
