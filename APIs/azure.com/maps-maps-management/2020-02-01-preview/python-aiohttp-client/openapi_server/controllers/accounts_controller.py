from typing import List, Dict
from aiohttp import web

from openapi_server.models.maps_account import MapsAccount
from openapi_server.models.maps_account_create_parameters import MapsAccountCreateParameters
from openapi_server.models.maps_account_keys import MapsAccountKeys
from openapi_server.models.maps_account_update_parameters import MapsAccountUpdateParameters
from openapi_server.models.maps_accounts import MapsAccounts
from openapi_server.models.maps_key_specification import MapsKeySpecification
from openapi_server.models.maps_list_operations_default_response import MapsListOperationsDefaultResponse
from openapi_server import util


async def accounts_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, maps_account_create_parameters) -> web.Response:
    """accounts_create_or_update

    Create or update a Maps Account. A Maps Account holds the keys which allow access to the Maps REST APIs.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param maps_account_create_parameters: The new or updated parameters for the Maps Account.
    :type maps_account_create_parameters: dict | bytes

    """
    maps_account_create_parameters = MapsAccountCreateParameters.from_dict(maps_account_create_parameters)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_delete

    Delete a Maps Account.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_get

    Get a Maps Account.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """accounts_list_by_resource_group

    Get all Maps Accounts in a Resource Group

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def accounts_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """accounts_list_by_subscription

    Get all Maps Accounts in a Subscription

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def accounts_list_keys(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_list_keys

    Get the keys to use with the Maps APIs. A key is used to authenticate and authorize access to the Maps REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_regenerate_keys(request: web.Request, api_version, subscription_id, resource_group_name, account_name, key_specification) -> web.Response:
    """accounts_regenerate_keys

    Regenerate either the primary or secondary key for use with the Maps APIs. The old key will stop working immediately.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param key_specification: Which key to regenerate:  primary or secondary.
    :type key_specification: dict | bytes

    """
    key_specification = MapsKeySpecification.from_dict(key_specification)
    return web.Response(status=200)


async def accounts_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, maps_account_update_parameters) -> web.Response:
    """accounts_update

    Updates a Maps Account. Only a subset of the parameters may be updated after creation, such as Sku and Tags.

    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the Maps Account.
    :type account_name: str
    :param maps_account_update_parameters: The updated parameters for the Maps Account.
    :type maps_account_update_parameters: dict | bytes

    """
    maps_account_update_parameters = MapsAccountUpdateParameters.from_dict(maps_account_update_parameters)
    return web.Response(status=200)
