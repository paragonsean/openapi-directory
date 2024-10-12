from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert import Alert
from openapi_server.models.alert_list import AlertList
from openapi_server.models.cloud_error import CloudError
from openapi_server import util


async def alerts_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets an alert by name.

    

    :param device_name: The device name.
    :type device_name: str
    :param name: The alert name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def alerts_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """alerts_list_by_data_box_edge_device

    Gets all the alerts for a data box edge/gateway device.

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
