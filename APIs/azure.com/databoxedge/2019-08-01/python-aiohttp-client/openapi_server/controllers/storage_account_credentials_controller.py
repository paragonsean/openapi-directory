from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_account_credential import StorageAccountCredential
from openapi_server.models.storage_account_credential_list import StorageAccountCredentialList
from openapi_server import util


async def storage_account_credentials_create_or_update(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version, storage_account_credential) -> web.Response:
    """storage_account_credentials_create_or_update

    Creates or updates the storage account credential.

    :param device_name: The device name.
    :type device_name: str
    :param name: The storage account credential name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param storage_account_credential: The storage account credential.
    :type storage_account_credential: dict | bytes

    """
    storage_account_credential = StorageAccountCredential.from_dict(storage_account_credential)
    return web.Response(status=200)


async def storage_account_credentials_delete(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """storage_account_credentials_delete

    Deletes the storage account credential.

    :param device_name: The device name.
    :type device_name: str
    :param name: The storage account credential name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_account_credentials_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """storage_account_credentials_get

    Gets the properties of the specified storage account credential.

    :param device_name: The device name.
    :type device_name: str
    :param name: The storage account credential name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_account_credentials_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets all the storage account credentials in a Data Box Edge/Data Box Gateway device.

    

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
