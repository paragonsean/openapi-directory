from typing import List, Dict
from aiohttp import web

from openapi_server.models.appliance_definition import ApplianceDefinition
from openapi_server.models.appliance_definition_list_result import ApplianceDefinitionListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def appliance_definitions_create_or_update(request: web.Request, resource_group_name, appliance_definition_name, api_version, subscription_id, parameters) -> web.Response:
    """appliance_definitions_create_or_update

    Creates a new appliance definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_definition_name: The name of the appliance definition.
    :type appliance_definition_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update an appliance definition.
    :type parameters: dict | bytes

    """
    parameters = ApplianceDefinition.from_dict(parameters)
    return web.Response(status=200)


async def appliance_definitions_create_or_update_by_id(request: web.Request, appliance_definition_id, api_version, parameters) -> web.Response:
    """appliance_definitions_create_or_update_by_id

    Creates a new appliance definition.

    :param appliance_definition_id: The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
    :type appliance_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters supplied to the create or update an appliance definition.
    :type parameters: dict | bytes

    """
    parameters = ApplianceDefinition.from_dict(parameters)
    return web.Response(status=200)


async def appliance_definitions_delete(request: web.Request, resource_group_name, appliance_definition_name, api_version, subscription_id) -> web.Response:
    """appliance_definitions_delete

    Deletes the appliance definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_definition_name: The name of the appliance definition to delete.
    :type appliance_definition_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def appliance_definitions_delete_by_id(request: web.Request, appliance_definition_id, api_version) -> web.Response:
    """appliance_definitions_delete_by_id

    Deletes the appliance definition.

    :param appliance_definition_id: The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
    :type appliance_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def appliance_definitions_get(request: web.Request, resource_group_name, appliance_definition_name, api_version, subscription_id) -> web.Response:
    """appliance_definitions_get

    Gets the appliance definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_definition_name: The name of the appliance definition.
    :type appliance_definition_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def appliance_definitions_get_by_id(request: web.Request, appliance_definition_id, api_version) -> web.Response:
    """appliance_definitions_get_by_id

    Gets the appliance definition.

    :param appliance_definition_id: The fully qualified ID of the appliance definition, including the appliance name and the appliance definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applianceDefinitions/{applianceDefinition-name}
    :type appliance_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def appliance_definitions_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """appliance_definitions_list_by_resource_group

    Lists the appliance definitions in a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
