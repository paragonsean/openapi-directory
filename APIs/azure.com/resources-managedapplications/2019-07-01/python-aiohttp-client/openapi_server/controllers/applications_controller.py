from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def applications_create_or_update(request: web.Request, resource_group_name, application_name, api_version, subscription_id, parameters) -> web.Response:
    """applications_create_or_update

    Creates a new managed application.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: The name of the managed application.
    :type application_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update a managed application.
    :type parameters: dict | bytes

    """
    parameters = Application.from_dict(parameters)
    return web.Response(status=200)


async def applications_create_or_update_by_id(request: web.Request, application_id, api_version, parameters) -> web.Response:
    """applications_create_or_update_by_id

    Creates a new managed application.

    :param application_id: The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
    :type application_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters supplied to the create or update a managed application.
    :type parameters: dict | bytes

    """
    parameters = Application.from_dict(parameters)
    return web.Response(status=200)


async def applications_delete(request: web.Request, resource_group_name, application_name, api_version, subscription_id) -> web.Response:
    """applications_delete

    Deletes the managed application.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: The name of the managed application.
    :type application_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def applications_delete_by_id(request: web.Request, application_id, api_version) -> web.Response:
    """applications_delete_by_id

    Deletes the managed application.

    :param application_id: The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
    :type application_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_get(request: web.Request, resource_group_name, application_name, api_version, subscription_id) -> web.Response:
    """applications_get

    Gets the managed application.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: The name of the managed application.
    :type application_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def applications_get_by_id(request: web.Request, application_id, api_version) -> web.Response:
    """applications_get_by_id

    Gets the managed application.

    :param application_id: The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
    :type application_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def applications_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """applications_list_by_resource_group

    Gets all the applications within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def applications_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """applications_list_by_subscription

    Gets all the applications within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def applications_refresh_permissions(request: web.Request, resource_group_name, application_name, api_version, subscription_id) -> web.Response:
    """applications_refresh_permissions

    Refresh Permissions for application.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: The name of the managed application.
    :type application_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def applications_update(request: web.Request, resource_group_name, application_name, api_version, subscription_id, parameters=None) -> web.Response:
    """applications_update

    Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param application_name: The name of the managed application.
    :type application_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to update an existing managed application.
    :type parameters: dict | bytes

    """
    parameters = Application.from_dict(parameters)
    return web.Response(status=200)


async def applications_update_by_id(request: web.Request, application_id, api_version, parameters=None) -> web.Response:
    """applications_update_by_id

    Updates an existing managed application. The only value that can be updated via PATCH currently is the tags.

    :param application_id: The fully qualified ID of the managed application, including the managed application name and the managed application resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/applications/{application-name}
    :type application_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters supplied to update an existing managed application.
    :type parameters: dict | bytes

    """
    parameters = Application.from_dict(parameters)
    return web.Response(status=200)
