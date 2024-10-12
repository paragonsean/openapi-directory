from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.user import User
from openapi_server.models.user_list import UserList
from openapi_server import util


async def users_create_or_update(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version, user) -> web.Response:
    """users_create_or_update

    Creates a new user or updates an existing user&#39;s information on a Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param name: The user name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param user: The user details.
    :type user: dict | bytes

    """
    user = User.from_dict(user)
    return web.Response(status=200)


async def users_delete(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """users_delete

    Deletes the user on a databox edge/gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param name: The user name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def users_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """users_get

    Gets the properties of the specified user.

    :param device_name: The device name.
    :type device_name: str
    :param name: The user name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def users_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version, filter=None) -> web.Response:
    """users_list_by_data_box_edge_device

    Gets all the users registered on a Data Box Edge/Data Box Gateway device.

    :param device_name: The device name.
    :type device_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param filter: Specify $filter&#x3D;&#39;UserType eq &lt;type&gt;&#39; to filter on user type property
    :type filter: str

    """
    return web.Response(status=200)
