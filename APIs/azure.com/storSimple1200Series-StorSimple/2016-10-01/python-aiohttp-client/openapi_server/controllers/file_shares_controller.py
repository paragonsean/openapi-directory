from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.file_share import FileShare
from openapi_server.models.file_share_list import FileShareList
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server import util


async def file_shares_create_or_update(request: web.Request, device_name, file_server_name, share_name, subscription_id, resource_group_name, manager_name, api_version, file_share) -> web.Response:
    """file_shares_create_or_update

    Creates or updates the file share.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param share_name: The file share name.
    :type share_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param file_share: The file share.
    :type file_share: dict | bytes

    """
    file_share = FileShare.from_dict(file_share)
    return web.Response(status=200)


async def file_shares_delete(request: web.Request, device_name, file_server_name, share_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_shares_delete

    Deletes the file share.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param share_name: The file share Name
    :type share_name: str
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


async def file_shares_get(request: web.Request, device_name, file_server_name, share_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_shares_get

    Returns the properties of the specified file share name.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param share_name: The file share name.
    :type share_name: str
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


async def file_shares_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_shares_list_by_device

    Retrieves all the file shares in a device.

    :param device_name: The device name.
    :type device_name: str
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


async def file_shares_list_by_file_server(request: web.Request, device_name, file_server_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_shares_list_by_file_server

    Retrieves all the file shares in a file server.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
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


async def file_shares_list_metric_definition(request: web.Request, device_name, file_server_name, share_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """file_shares_list_metric_definition

    Retrieves metric definitions of all metrics aggregated at the file share.

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param share_name: The file share name.
    :type share_name: str
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


async def file_shares_list_metrics(request: web.Request, device_name, file_server_name, share_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """file_shares_list_metrics

    Gets the file share metrics

    :param device_name: The device name.
    :type device_name: str
    :param file_server_name: The file server name.
    :type file_server_name: str
    :param share_name: The file share name.
    :type share_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)
