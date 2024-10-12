from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.role import Role
from openapi_server.models.role_list import RoleList
from openapi_server import util


async def roles_create_or_update(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version, role) -> web.Response:
    """roles_create_or_update

    Create or update a role.

    :param device_name: The device name.
    :type device_name: str
    :param name: The role name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str
    :param role: The role properties.
    :type role: dict | bytes

    """
    role = Role.from_dict(role)
    return web.Response(status=200)


async def roles_delete(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """roles_delete

    Deletes the role on the data box edge device.

    :param device_name: The device name.
    :type device_name: str
    :param name: The role name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def roles_get(request: web.Request, device_name, name, subscription_id, resource_group_name, api_version) -> web.Response:
    """roles_get

    Gets a specific role by name.

    :param device_name: The device name.
    :type device_name: str
    :param name: The role name.
    :type name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def roles_list_by_data_box_edge_device(request: web.Request, device_name, subscription_id, resource_group_name, api_version) -> web.Response:
    """roles_list_by_data_box_edge_device

    Lists all the roles configured in a data box edge/gateway device.

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
