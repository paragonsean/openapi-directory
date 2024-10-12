from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.storage_account_credential import StorageAccountCredential
from openapi_server.models.storage_account_credential_list import StorageAccountCredentialList
from openapi_server import util


async def storage_account_credentials_create_or_update(request: web.Request, credential_name, subscription_id, resource_group_name, manager_name, api_version, storage_account) -> web.Response:
    """storage_account_credentials_create_or_update

    Creates or updates the storage account credential

    :param credential_name: The credential name.
    :type credential_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param storage_account: The storage account credential to be added or updated.
    :type storage_account: dict | bytes

    """
    storage_account = StorageAccountCredential.from_dict(storage_account)
    return web.Response(status=200)


async def storage_account_credentials_delete(request: web.Request, credential_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """storage_account_credentials_delete

    Deletes the storage account credential

    :param credential_name: The name of the storage account credential.
    :type credential_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_account_credentials_get(request: web.Request, credential_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """storage_account_credentials_get

    Returns the properties of the specified storage account credential name.

    :param credential_name: The name of storage account credential to be fetched.
    :type credential_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_account_credentials_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """storage_account_credentials_list_by_manager

    Retrieves all the storage account credentials in a manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str

    """
    return web.Response(status=200)
