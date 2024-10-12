from typing import List, Dict
from aiohttp import web

from openapi_server.models.appliance import Appliance
from openapi_server.models.appliance_list_result import ApplianceListResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def appliances_create_or_update(request: web.Request, resource_group_name, appliance_name, api_version, subscription_id, parameters) -> web.Response:
    """appliances_create_or_update

    Creates a new appliance.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_name: The name of the appliance.
    :type appliance_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to the create or update an appliance.
    :type parameters: dict | bytes

    """
    parameters = Appliance.from_dict(parameters)
    return web.Response(status=200)


async def appliances_create_or_update_by_id(request: web.Request, appliance_id, api_version, parameters) -> web.Response:
    """appliances_create_or_update_by_id

    Creates a new appliance.

    :param appliance_id: The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
    :type appliance_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters supplied to the create or update an appliance.
    :type parameters: dict | bytes

    """
    parameters = Appliance.from_dict(parameters)
    return web.Response(status=200)


async def appliances_delete(request: web.Request, resource_group_name, appliance_name, api_version, subscription_id) -> web.Response:
    """appliances_delete

    Deletes the appliance.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_name: The name of the appliance.
    :type appliance_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def appliances_delete_by_id(request: web.Request, appliance_id, api_version) -> web.Response:
    """appliances_delete_by_id

    Deletes the appliance.

    :param appliance_id: The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
    :type appliance_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def appliances_get(request: web.Request, resource_group_name, appliance_name, api_version, subscription_id) -> web.Response:
    """appliances_get

    Gets the appliance.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_name: The name of the appliance.
    :type appliance_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def appliances_get_by_id(request: web.Request, appliance_id, api_version) -> web.Response:
    """appliances_get_by_id

    Gets the appliance.

    :param appliance_id: The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
    :type appliance_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def appliances_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """appliances_list_by_resource_group

    Gets all the appliances within a resource group.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def appliances_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """appliances_list_by_subscription

    Gets all the appliances within a subscription.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def appliances_update(request: web.Request, resource_group_name, appliance_name, api_version, subscription_id, parameters=None) -> web.Response:
    """appliances_update

    Updates an existing appliance. The only value that can be updated via PATCH currently is the tags.

    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param appliance_name: The name of the appliance.
    :type appliance_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param parameters: Parameters supplied to update an existing appliance.
    :type parameters: dict | bytes

    """
    parameters = Appliance.from_dict(parameters)
    return web.Response(status=200)


async def appliances_update_by_id(request: web.Request, appliance_id, api_version, parameters=None) -> web.Response:
    """appliances_update_by_id

    Updates an existing appliance. The only value that can be updated via PATCH currently is the tags.

    :param appliance_id: The fully qualified ID of the appliance, including the appliance name and the appliance resource type. Use the format, /subscriptions/{guid}/resourceGroups/{resource-group-name}/Microsoft.Solutions/appliances/{appliance-name}
    :type appliance_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param parameters: Parameters supplied to update an existing appliance.
    :type parameters: dict | bytes

    """
    parameters = Appliance.from_dict(parameters)
    return web.Response(status=200)
