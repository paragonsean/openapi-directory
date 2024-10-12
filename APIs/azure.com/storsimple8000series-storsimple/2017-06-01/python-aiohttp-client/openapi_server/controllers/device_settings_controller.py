from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_settings import AlertSettings
from openapi_server.models.network_settings import NetworkSettings
from openapi_server.models.network_settings_patch import NetworkSettingsPatch
from openapi_server.models.security_settings import SecuritySettings
from openapi_server.models.security_settings_patch import SecuritySettingsPatch
from openapi_server.models.time_settings import TimeSettings
from openapi_server import util


async def device_settings_create_or_update_alert_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """device_settings_create_or_update_alert_settings

    Creates or updates the alert settings of the specified device.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The alert settings to be added or updated.
    :type parameters: dict | bytes

    """
    parameters = AlertSettings.from_dict(parameters)
    return web.Response(status=200)


async def device_settings_create_or_update_time_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """device_settings_create_or_update_time_settings

    Creates or updates the time settings of the specified device.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The time settings to be added or updated.
    :type parameters: dict | bytes

    """
    parameters = TimeSettings.from_dict(parameters)
    return web.Response(status=200)


async def device_settings_get_alert_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """device_settings_get_alert_settings

    Gets the alert settings of the specified device.

    :param device_name: The device name
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


async def device_settings_get_network_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """device_settings_get_network_settings

    Gets the network settings of the specified device.

    :param device_name: The device name
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


async def device_settings_get_security_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """device_settings_get_security_settings

    Returns the Security properties of the specified device name.

    :param device_name: The device name
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


async def device_settings_get_time_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """device_settings_get_time_settings

    Gets the time settings of the specified device.

    :param device_name: The device name
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


async def device_settings_sync_remotemanagement_certificate(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """device_settings_sync_remotemanagement_certificate

    sync Remote management Certificate between appliance and Service

    :param device_name: The device name
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


async def device_settings_update_network_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """device_settings_update_network_settings

    Updates the network settings on the specified device.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The network settings to be updated.
    :type parameters: dict | bytes

    """
    parameters = NetworkSettingsPatch.from_dict(parameters)
    return web.Response(status=200)


async def device_settings_update_security_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """device_settings_update_security_settings

    Patch Security properties of the specified device name.

    :param device_name: The device name
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The security settings properties to be patched.
    :type parameters: dict | bytes

    """
    parameters = SecuritySettingsPatch.from_dict(parameters)
    return web.Response(status=200)
