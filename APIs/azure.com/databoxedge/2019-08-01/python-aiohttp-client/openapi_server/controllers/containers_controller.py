from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.container import Container
from openapi_server.models.container_list import ContainerList
from openapi_server import util


async def containers_create_or_update(request: web.Request, device_name, storage_account_name, container_name, subscription_id, resource_group_name, api_version, container) -> web.Response:
    """Creates a new container or updates an existing container on the device.

    

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The Storage Account Name
    :type storage_account_name: str
    :param container_name: The container name.
    :type container_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param container: The container properties.
    :type container: dict | bytes

    """
    container = Container.from_dict(container)
    return web.Response(status=200)


async def containers_delete(request: web.Request, device_name, storage_account_name, container_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """containers_delete

    Deletes the container on the Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The Storage Account Name
    :type storage_account_name: str
    :param container_name: The container name.
    :type container_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def containers_get(request: web.Request, device_name, storage_account_name, container_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets a container by name.

    

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The Storage Account Name
    :type storage_account_name: str
    :param container_name: The container Name
    :type container_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def containers_list_by_storage_account(request: web.Request, device_name, storage_account_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Lists all the containers of a storage Account in a Data Box Edge/Data Box Gateway device.

    

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The storage Account name.
    :type storage_account_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def containers_refresh(request: web.Request, device_name, storage_account_name, container_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Refreshes the container metadata with the data from the cloud.

    

    :param device_name: The device name.
    :type device_name: str
    :param storage_account_name: The Storage Account Name
    :type storage_account_name: str
    :param container_name: The container name.
    :type container_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
