from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.storage_account import StorageAccount
from openapi_server.models.storage_account_list import StorageAccountList
from openapi_server import util


async def storage_accounts_create_or_update(request: web.Request, device_name, storage_account_name, subscription_id, resource_group_name, api_version, storage_account) -> web.Response:
    """Creates a new StorageAccount or updates an existing StorageAccount on the device.

    

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The StorageAccount name.
    :type storage_account_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param storage_account: The StorageAccount properties.
    :type storage_account: dict | bytes

    """
    storage_account = StorageAccount.from_dict(storage_account)
    return web.Response(status=200)


async def storage_accounts_delete(request: web.Request, device_name, storage_account_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """storage_accounts_delete

    Deletes the StorageAccount on the Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The StorageAccount name.
    :type storage_account_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_accounts_get(request: web.Request, device_name, storage_account_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets a StorageAccount by name.

    

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The storage account name.
    :type storage_account_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def storage_accounts_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Lists all the storage accounts in a Data Box Edge/Data Box Gateway device.

    

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
