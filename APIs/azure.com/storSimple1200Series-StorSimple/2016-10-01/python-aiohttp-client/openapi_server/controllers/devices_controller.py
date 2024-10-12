from typing import List, Dict
from aiohttp import web

from openapi_server.models.alert_settings import AlertSettings
from openapi_server.models.device import Device
from openapi_server.models.device_list import DeviceList
from openapi_server.models.device_patch import DevicePatch
from openapi_server.models.error import Error
from openapi_server.models.failover_request import FailoverRequest
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.network_settings import NetworkSettings
from openapi_server.models.security_settings import SecuritySettings
from openapi_server.models.time_settings import TimeSettings
from openapi_server.models.updates import Updates
from openapi_server import util


async def devices_create_or_update_alert_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, alert_settings) -> web.Response:
    """devices_create_or_update_alert_settings

    Creates or updates the alert settings

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
    :param alert_settings: The alert settings.
    :type alert_settings: dict | bytes

    """
    alert_settings = AlertSettings.from_dict(alert_settings)
    return web.Response(status=200)


async def devices_create_or_update_security_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, security_settings) -> web.Response:
    """devices_create_or_update_security_settings

    Creates or updates the security settings.

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
    :param security_settings: The security settings.
    :type security_settings: dict | bytes

    """
    security_settings = SecuritySettings.from_dict(security_settings)
    return web.Response(status=200)


async def devices_deactivate(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_deactivate

    Deactivates the device.

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


async def devices_delete(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_delete

    Deletes the device.

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


async def devices_download_updates(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_download_updates

    Downloads updates on the device.

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


async def devices_failover(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, failover_request) -> web.Response:
    """devices_failover

    Fails over the device to another device.

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
    :param failover_request: The failover request.
    :type failover_request: dict | bytes

    """
    failover_request = FailoverRequest.from_dict(failover_request)
    return web.Response(status=200)


async def devices_get(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, expand=None) -> web.Response:
    """devices_get

    Returns the properties of the specified device name.

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
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the device.
    :type expand: str

    """
    return web.Response(status=200)


async def devices_get_alert_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_get_alert_settings

    Returns the alert settings of the specified device name.

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


async def devices_get_network_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_get_network_settings

    Returns the network settings of the specified device name.

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


async def devices_get_time_settings(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_get_time_settings

    Returns the time settings of the specified device name.

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


async def devices_get_update_summary(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_get_update_summary

    Returns the update summary of the specified device name.

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


async def devices_install_updates(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_install_updates

    Installs the updates on the device.

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


async def devices_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, expand=None) -> web.Response:
    """devices_list_by_manager

    Retrieves all the devices in a manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the device.
    :type expand: str

    """
    return web.Response(status=200)


async def devices_list_failover_target(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, expand=None) -> web.Response:
    """devices_list_failover_target

    Retrieves all the devices which can be used as failover targets for the given device.

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
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the device.
    :type expand: str

    """
    return web.Response(status=200)


async def devices_list_metric_definition(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_list_metric_definition

    Retrieves metric definition of all metrics aggregated at device.

    :param device_name: The name of the appliance.
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


async def devices_list_metrics(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, filter=None) -> web.Response:
    """devices_list_metrics

    Retrieves the device metrics.

    :param device_name: The name of the appliance.
    :type device_name: str
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


async def devices_patch(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, device_patch) -> web.Response:
    """devices_patch

    Patches the device.

    :param device_name: The device Name.
    :type device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param device_patch: Patch representation of the device.
    :type device_patch: dict | bytes

    """
    device_patch = DevicePatch.from_dict(device_patch)
    return web.Response(status=200)


async def devices_scan_for_updates(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_scan_for_updates

    Scans for updates on the device.

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
