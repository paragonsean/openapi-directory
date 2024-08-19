from typing import List, Dict
from aiohttp import web

from openapi_server.models.chap_settings import ChapSettings
from openapi_server.models.chap_settings_list import ChapSettingsList
from openapi_server.models.error import Error
from openapi_server import util


async def chap_settings_create_or_update(request: web.Request, device_name, chap_user_name, subscription_id, resource_group_name, manager_name, api_version, chap_setting) -> web.Response:
    """chap_settings_create_or_update

    Creates or updates the chap setting.

    :param device_name: The device name.
    :type device_name: str
    :param chap_user_name: The chap user name.
    :type chap_user_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param chap_setting: The chap setting to be added or updated.
    :type chap_setting: dict | bytes

    """
    chap_setting = ChapSettings.from_dict(chap_setting)
    return web.Response(status=200)


async def chap_settings_delete(request: web.Request, device_name, chap_user_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """chap_settings_delete

    Deletes the chap setting.

    :param device_name: The device name.
    :type device_name: str
    :param chap_user_name: The chap user name.
    :type chap_user_name: str
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


async def chap_settings_get(request: web.Request, device_name, chap_user_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """chap_settings_get

    Returns the properties of the specified chap setting name.

    :param device_name: The device name.
    :type device_name: str
    :param chap_user_name: The user name of chap to be fetched.
    :type chap_user_name: str
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


async def chap_settings_list_by_device(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """chap_settings_list_by_device

    Retrieves all the chap settings in a device.

    :param device_name: The name of the device.
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
