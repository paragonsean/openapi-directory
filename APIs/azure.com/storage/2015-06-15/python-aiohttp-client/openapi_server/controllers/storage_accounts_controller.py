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

    Checks that the storage account name is valid and is not already in use.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: dict | bytes

    """
    account_name = StorageAccountCheckNameAvailabilityParameters.from_dict(account_name)
    return web.Response(status=200)


async def storage_accounts_create(request: web.Request, resource_group_name, account_name, api_version, subscription_id, parameters) -> web.Response:
    """storage_accounts_create

    Asynchronously creates a new storage account with the specified parameters. If an account is already created and a subsequent create request is issued with different properties, the account properties will be updated. If an account is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created account.
    :type parameters: dict | bytes

    """
    parameters = StorageAccountCreateParameters.from_dict(parameters)
    return web.Response(status=200)


async def storage_accounts_delete(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_delete

    Deletes a storage account in Microsoft Azure.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_get_properties(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_get_properties

    Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.  
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """storage_accounts_list

    Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_list_by_resource_group

    Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_list_keys(request: web.Request, resource_group_name, account_name, api_version, subscription_id) -> web.Response:
    """storage_accounts_list_keys

    Lists the access keys for the specified storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def storage_accounts_regenerate_key(request: web.Request, resource_group_name, account_name, api_version, subscription_id, regenerate_key) -> web.Response:
    """storage_accounts_regenerate_key

    Regenerates one of the access keys for the specified storage account.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param regenerate_key: Specifies name of the key which should be regenerated -- key1 or key2.
    :type regenerate_key: dict | bytes

    """
    regenerate_key = StorageAccountRegenerateKeyParameters.from_dict(regenerate_key)
    return web.Response(status=200)


async def storage_accounts_update(request: web.Request, resource_group_name, account_name, api_version, subscription_id, parameters) -> web.Response:
    """storage_accounts_update

    The update operation can be used to update the SKU, encryption, access tier, or tags for a storage account. It can also be used to map the account to a custom domain. Only one custom domain is supported per storage account; the replacement/change of custom domain is not supported. In order to replace an old custom domain, the old value must be cleared/unregistered before a new value can be set. The update of multiple properties is supported. This call does not change the storage keys for the account. If you want to change the storage account keys, use the regenerate keys operation. The location and name of the storage account cannot be changed after creation.

    :param resource_group_name: The name of the resource group within the user&#39;s subscription. The name is case insensitive.
    :type resource_group_name: str
    :param account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :type account_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: The parameters to provide for the updated account.
    :type parameters: dict | bytes

    """
    parameters = StorageAccountUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
