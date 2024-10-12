from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.order import Order
from openapi_server.models.order_list import OrderList
from openapi_server import util


async def orders_create_or_update(request: web.Request, device_name, subscription_id, resource_group_name, api_version, order) -> web.Response:
    """Creates or updates an order.

    

    :param device_name: The order details of a device.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param order: The order to be created or updated.
    :type order: dict | bytes

    """
    order = Order.from_dict(order)
    return web.Response(status=200)


async def orders_delete(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Deletes the order related to the device.

    

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


async def orders_get(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Gets a specific order by name.

    

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


async def orders_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """Lists all the orders related to a Data Box Edge/Data Box Gateway device.

    

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
