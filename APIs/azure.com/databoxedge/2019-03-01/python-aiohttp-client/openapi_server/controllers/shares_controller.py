from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.share import Share
from openapi_server.models.share_list import ShareList
from openapi_server import util


async def shares_create_or_update(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version, share) -> web.Response:
    """Creates a new share or updates an existing share on the device.

    

    :param device_name: The device name.
    :type device_name: str
    :param name: The share name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param share: The share properties.
    :type share: dict | bytes

    """
    share = Share.from_dict(share)
    return web.Response(status=200)


async def shares_delete(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """shares_delete

    Deletes the share on the data box edge/gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param name: The share name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets a share by name.

    

    :param device_name: The device name.
    :type device_name: str
    :param name: The share name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def shares_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Lists all the shares in a data box edge/gateway device.

    

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


async def shares_refresh(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Refreshes the share metadata with the data from the cloud.

    

    :param device_name: The device name.
    :type device_name: str
    :param name: The share name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
