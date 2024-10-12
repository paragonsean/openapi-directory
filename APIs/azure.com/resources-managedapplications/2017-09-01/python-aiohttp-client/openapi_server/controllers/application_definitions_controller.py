from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_definition import ApplicationDefinition
from openapi_server.models.application_definition_list_result import ApplicationDefinitionListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def application_definitions_create_or_update(request: web.Request, resource_group_name, application_definition_name, api_version, subscription_id, parameters) -> web.Response:
    """application_definitions_create_or_update

    Creates a new managed application definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_definition_name: The name of the managed application definition.
    :type application_definition_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update an managed application definition.
    :type parameters: dict | bytes

    """
    parameters = ApplicationDefinition.from_dict(parameters)
    return web.Response(status=200)


async def application_definitions_create_or_update_by_id(request: web.Request, application_definition_id, api_version, parameters) -> web.Response:
    """application_definitions_create_or_update_by_id

    Creates a new managed application definition.

    :param application_definition_id: The fully qualified ID of the managed application definition, including the managed application name and the managed application definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applicationDefinitions/{applicationDefinition-name}
    :type application_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters supplied to the create or update a managed application definition.
    :type parameters: dict | bytes

    """
    parameters = ApplicationDefinition.from_dict(parameters)
    return web.Response(status=200)


async def application_definitions_delete(request: web.Request, resource_group_name, application_definition_name, api_version, subscription_id) -> web.Response:
    """application_definitions_delete

    Deletes the managed application definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_definition_name: The name of the managed application definition to delete.
    :type application_definition_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_definitions_delete_by_id(request: web.Request, application_definition_id, api_version) -> web.Response:
    """application_definitions_delete_by_id

    Deletes the managed application definition.

    :param application_definition_id: The fully qualified ID of the managed application definition, including the managed application name and the managed application definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applicationDefinitions/{applicationDefinition-name}
    :type application_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def application_definitions_get(request: web.Request, resource_group_name, application_definition_name, api_version, subscription_id) -> web.Response:
    """application_definitions_get

    Gets the managed application definition.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_definition_name: The name of the managed application definition.
    :type application_definition_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def application_definitions_get_by_id(request: web.Request, application_definition_id, api_version) -> web.Response:
    """application_definitions_get_by_id

    Gets the managed application definition.

    :param application_definition_id: The fully qualified ID of the managed application definition, including the managed application name and the managed application definition resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applicationDefinitions/{applicationDefinition-name}
    :type application_definition_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def application_definitions_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """application_definitions_list_by_resource_group

    Lists the managed application definitions in a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)
