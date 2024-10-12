from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multiple_activation_key import MultipleActivationKey
from openapi_server.models.multiple_activation_key_list import MultipleActivationKeyList
from openapi_server.models.multiple_activation_key_update import MultipleActivationKeyUpdate
from openapi_server import util


async def multiple_activation_keys_create(request: web.Request, subscription_id, resource_group_name, api_version, multiple_activation_key_name, multiple_activation_key) -> web.Response:
    """multiple_activation_keys_create

    Create a MAK key.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param multiple_activation_key_name: The name of the MAK key.
    :type multiple_activation_key_name: str
    :param multiple_activation_key: Details of the MAK key.
    :type multiple_activation_key: dict | bytes

    """
    multiple_activation_key = MultipleActivationKey.from_dict(multiple_activation_key)
    return web.Response(status=200)


async def multiple_activation_keys_delete(request: web.Request, subscription_id, resource_group_name, api_version, multiple_activation_key_name) -> web.Response:
    """multiple_activation_keys_delete

    Delete a MAK key.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param multiple_activation_key_name: The name of the MAK key.
    :type multiple_activation_key_name: str

    """
    return web.Response(status=200)


async def multiple_activation_keys_get(request: web.Request, subscription_id, resource_group_name, api_version, multiple_activation_key_name) -> web.Response:
    """multiple_activation_keys_get

    Get a MAK key.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param multiple_activation_key_name: The name of the MAK key.
    :type multiple_activation_key_name: str

    """
    return web.Response(status=200)


async def multiple_activation_keys_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """multiple_activation_keys_list

    List all Multiple Activation Keys (MAK) created for a subscription.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def multiple_activation_keys_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """multiple_activation_keys_list_by_resource_group

    List all Multiple Activation Keys (MAK) in a resource group.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str

    """
    return web.Response(status=200)


async def multiple_activation_keys_update(request: web.Request, subscription_id, resource_group_name, api_version, multiple_activation_key_name, multiple_activation_key) -> web.Response:
    """multiple_activation_keys_update

    Update a MAK key.

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param multiple_activation_key_name: The name of the MAK key.
    :type multiple_activation_key_name: str
    :param multiple_activation_key: Details of the MAK key.
    :type multiple_activation_key: dict | bytes

    """
    multiple_activation_key = MultipleActivationKeyUpdate.from_dict(multiple_activation_key)
    return web.Response(status=200)
