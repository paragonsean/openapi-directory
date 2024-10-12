from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.location_based_services_account import LocationBasedServicesAccount
from openapi_server.models.location_based_services_account_create_parameters import LocationBasedServicesAccountCreateParameters
from openapi_server.models.location_based_services_account_keys import LocationBasedServicesAccountKeys
from openapi_server.models.location_based_services_account_update_parameters import LocationBasedServicesAccountUpdateParameters
from openapi_server.models.location_based_services_accounts import LocationBasedServicesAccounts
from openapi_server.models.location_based_services_accounts_move_request import LocationBasedServicesAccountsMoveRequest
from openapi_server.models.location_based_services_key_specification import LocationBasedServicesKeySpecification
from openapi_server.models.location_based_services_operations import LocationBasedServicesOperations
from openapi_server import util


async def accounts_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, location_based_services_account_create_parameters) -> web.Response:
    """accounts_create_or_update

    Create or update a Location Based Services Account. A Location Based Services Account holds the keys which allow access to the Location Based Services REST APIs.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str
    :param account_name: The name of the Location Based Services Account.
    :type account_name: str
    :param location_based_services_account_create_parameters: The new or updated parameters for the Location Based Services Account.
    :type location_based_services_account_create_parameters: dict | bytes

    """
    location_based_services_account_create_parameters = LocationBasedServicesAccountCreateParameters.from_dict(location_based_services_account_create_parameters)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_delete

    Delete a Location Based Services Account

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str
    :param account_name: The name of the Location Based Services Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_get

    Get a Location Based Services Account

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str
    :param account_name: The name of the Location Based Services Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """accounts_list_by_resource_group

    Get all Location Based Services Accounts in a Resource Group

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def accounts_list_by_subscription(request: web.Request, api_version, subscription_id) -> web.Response:
    """accounts_list_by_subscription

    Get all Location Based Services Accounts in a Subscription

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def accounts_list_keys(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_list_keys

    Get the keys to use with the Location Based Services APIs. A key is used to authenticate and authorize access to the Location Based Services REST APIs. Only one key is needed at a time; two are given to provide seamless key regeneration.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str
    :param account_name: The name of the Location Based Services Account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_list_operations(request: web.Request, api_version) -> web.Response:
    """accounts_list_operations

    List operations available for the Location Based Services Resource Provider

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_move(request: web.Request, api_version, subscription_id, resource_group_name, move_request) -> web.Response:
    """accounts_move

    Moves Location Based Services Accounts from one ResourceGroup (or Subscription) to another

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains Location Based Services Account to move.
    :type resource_group_name: str
    :param move_request: The details of the Location Based Services Account move.
    :type move_request: dict | bytes

    """
    move_request = LocationBasedServicesAccountsMoveRequest.from_dict(move_request)
    return web.Response(status=200)


async def accounts_regenerate_keys(request: web.Request, api_version, subscription_id, resource_group_name, account_name, key_specification) -> web.Response:
    """accounts_regenerate_keys

    Regenerate either the primary or secondary key for use with the Location Based Services APIs. The old key will stop working immediately.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str
    :param account_name: The name of the Location Based Services Account.
    :type account_name: str
    :param key_specification: Which key to regenerate:  primary or secondary.
    :type key_specification: dict | bytes

    """
    key_specification = LocationBasedServicesKeySpecification.from_dict(key_specification)
    return web.Response(status=200)


async def accounts_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, location_based_services_account_update_parameters) -> web.Response:
    """accounts_update

    Updates a Location Based Services Account. Only a subset of the parameters may be updated after creation, such as Sku and Tags.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the Azure Resource Group.
    :type resource_group_name: str
    :param account_name: The name of the Location Based Services Account.
    :type account_name: str
    :param location_based_services_account_update_parameters: The updated parameters for the Location Based Services Account.
    :type location_based_services_account_update_parameters: dict | bytes

    """
    location_based_services_account_update_parameters = LocationBasedServicesAccountUpdateParameters.from_dict(location_based_services_account_update_parameters)
    return web.Response(status=200)
