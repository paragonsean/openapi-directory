from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_name_availability_result import CheckNameAvailabilityResult
from openapi_server.models.storage_account import StorageAccount
from openapi_server.models.storage_account_check_name_availability_parameters import StorageAccountCheckNameAvailabilityParameters
from openapi_server.models.storage_account_create_parameters import StorageAccountCreateParameters
from openapi_server.models.storage_account_keys import StorageAccountKeys
from openapi_server.models.storage_account_list_result import StorageAccountListResult
from openapi_server.models.storage_account_regenerate_key_parameters import StorageAccountRegenerateKeyParameters
from openapi_server.models.storage_account_update_parameters import StorageAccountUpdateParameters
from openapi_server import util


async def storage_accounts_check_name_availability(request: web.Request, api_version, subscription_id, account_name) -> web.Response:
    """storage_accounts_check_name_availability

    Checks that account name is valid and is not in use.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: dict | bytes

    """
    account_name = StorageAccountCheckNameAvailabilityParameters.from_dict(account_name)
    return web.Response(status=200)


async def storage_accounts_create(request: web.Request, resource_group_name, account_name, api_version, subscription_id, parameters) -> web.Response:
    """storage_accounts_create

    Asynchronously creates a new storage account with the specified parameters. Existing accounts cannot be updated with this API and should instead use the Update Storage Account API. If an account is already created and subsequent PUT request is issued with exact same set of properties, then HTTP 200 would be returned. 

    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created account.
    :type parameters: dict | bytes

    """
    parameters = StorageAccountCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def storage_accounts_delete(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_delete

    Deletes a storage account in Microsoft Azure.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_get_properties(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_get_properties

    Returns the properties for the specified storage account including but not limited to name, account type, location, and account status. The ListKeys operation should be used to retrieve storage keys.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """storage_accounts_list

    Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_list_by_resource_group

    Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_list_keys(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_list_keys

    Lists the access keys for the specified storage account.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the storage account.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_regenerate_key(request: web.Request, resource_group_name, account_name, api_version, subscription_id, regenerate_key) -> web.Response:
    """storage_accounts_regenerate_key

    Regenerates the access keys for the specified storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param regenerate_key: Specifies name of the key which should be regenerated.
    :type regenerate_key: dict | bytes

    """
    regenerate_key = StorageAccountRegenerateKeyParameters.from_dict(regenerate_key)
    return web.Response(status=200)


async def storage_accounts_update(request: web.Request, resource_group_name, account_name, api_version, subscription_id, parameters) -> web.Response:
    """storage_accounts_update

    Updates the account type or tags for a storage account. It can also be used to add a custom domain (note that custom domains cannot be added via the Create operation). Only one custom domain is supported per storage account. This API can only be used to update one of tags, accountType, or customDomain per call. To update multiple of these properties, call the API multiple times with one change per call. This call does not change the storage keys for the account. If you want to change storage account keys, use the RegenerateKey operation. The location and name of the storage account cannot be changed after creation.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters to update on the account. Note that only one property can be changed at a time using this API. 
    :type parameters: dict | bytes

    """
    parameters = StorageAccountUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
