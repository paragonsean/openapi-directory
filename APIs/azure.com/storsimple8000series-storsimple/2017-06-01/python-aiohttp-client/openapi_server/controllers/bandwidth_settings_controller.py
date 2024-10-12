from typing import List, Dict
from aiohttp import web

from openapi_server.models.bandwidth_setting import BandwidthSetting
from openapi_server.models.bandwidth_setting_list import BandwidthSettingList
from openapi_server import util


async def bandwidth_settings_create_or_update(request: web.Request, bandwidth_setting_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """bandwidth_settings_create_or_update

    Creates or updates the bandwidth setting

    :param bandwidth_setting_name: The bandwidth setting name.
    :type bandwidth_setting_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The bandwidth setting to be added or updated.
    :type parameters: dict | bytes

    """
    parameters = BandwidthSetting.from_dict(parameters)
    return web.Response(status=200)


async def bandwidth_settings_delete(request: web.Request, bandwidth_setting_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """bandwidth_settings_delete

    Deletes the bandwidth setting

    :param bandwidth_setting_name: The name of the bandwidth setting.
    :type bandwidth_setting_name: str
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


async def bandwidth_settings_get(request: web.Request, bandwidth_setting_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """bandwidth_settings_get

    Returns the properties of the specified bandwidth setting name.

    :param bandwidth_setting_name: The name of bandwidth setting to be fetched.
    :type bandwidth_setting_name: str
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


async def bandwidth_settings_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """bandwidth_settings_list_by_manager

    Retrieves all the bandwidth setting in a manager.

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
