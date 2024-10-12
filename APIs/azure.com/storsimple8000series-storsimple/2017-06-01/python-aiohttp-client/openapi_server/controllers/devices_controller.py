from typing import List, Dict
from aiohttp import web

from openapi_server.models.configure_device_request import ConfigureDeviceRequest
from openapi_server.models.device import Device
from openapi_server.models.device_list import DeviceList
from openapi_server.models.device_patch import DevicePatch
from openapi_server.models.failover_request import FailoverRequest
from openapi_server.models.failover_sets_list import FailoverSetsList
from openapi_server.models.failover_targets_list import FailoverTargetsList
from openapi_server.models.list_failover_targets_request import ListFailoverTargetsRequest
from openapi_server.models.metric_definition_list import MetricDefinitionList
from openapi_server.models.metric_list import MetricList
from openapi_server.models.updates import Updates
from openapi_server import util


async def devices_authorize_for_service_encryption_key_rollover(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_authorize_for_service_encryption_key_rollover

    Authorizes the specified device for service data encryption key rollover.

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


async def devices_configure(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """devices_configure

    Complete minimal setup before using the device.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: The minimal properties to configure a device.
    :type parameters: dict | bytes

    """
    parameters = ConfigureDeviceRequest.from_dict(parameters)
    return web.Response(status=200)


async def devices_deactivate(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_deactivate

    Deactivates the device.

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


async def devices_delete(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_delete

    Deletes the device.

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


async def devices_failover(request: web.Request, source_device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """devices_failover

    Failovers a set of volume containers from a specified source device to a target device.

    :param source_device_name: The source device name on which failover is performed.
    :type source_device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: FailoverRequest containing the source device and the list of volume containers to be failed over.
    :type parameters: dict | bytes

    """
    parameters = FailoverRequest.from_dict(parameters)
    return web.Response(status=200)


async def devices_get(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, expand=None) -> web.Response:
    """devices_get

    Returns the properties of the specified device.

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
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the device or $expand&#x3D;rolloverdetails to populate additional fields related to the service data encryption key rollover on device
    :type expand: str

    """
    return web.Response(status=200)


async def devices_get_update_summary(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_get_update_summary

    Returns the update summary of the specified device name.

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


async def devices_install_updates(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_install_updates

    Downloads and installs the updates on the device.

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


async def devices_list_by_manager(request: web.Request, subscription_id, resource_group_name, manager_name, api_version, expand=None) -> web.Response:
    """devices_list_by_manager

    Returns the list of devices for the specified manager.

    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param expand: Specify $expand&#x3D;details to populate additional fields related to the device or $expand&#x3D;rolloverdetails to populate additional fields related to the service data encryption key rollover on device
    :type expand: str

    """
    return web.Response(status=200)


async def devices_list_failover_sets(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_list_failover_sets

    Returns all failover sets for a given device and their eligibility for participating in a failover. A failover set refers to a set of volume containers that need to be failed-over as a single unit to maintain data integrity.

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


async def devices_list_failover_targets(request: web.Request, source_device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """devices_list_failover_targets

    Given a list of volume containers to be failed over from a source device, this method returns the eligibility result, as a failover target, for all devices under that resource.

    :param source_device_name: The source device name on which failover is performed.
    :type source_device_name: str
    :param subscription_id: The subscription id
    :type subscription_id: str
    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param manager_name: The manager name
    :type manager_name: str
    :param api_version: The api version
    :type api_version: str
    :param parameters: ListFailoverTargetsRequest containing the list of volume containers to be failed over.
    :type parameters: dict | bytes

    """
    parameters = ListFailoverTargetsRequest.from_dict(parameters)
    return web.Response(status=200)


async def devices_list_metric_definition(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_list_metric_definition

    Gets the metric definitions for the specified device.

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


async def devices_list_metrics(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, filter) -> web.Response:
    """devices_list_metrics

    Gets the metrics for the specified device.

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
    :param filter: OData Filter options
    :type filter: str

    """
    return web.Response(status=200)


async def devices_scan_for_updates(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version) -> web.Response:
    """devices_scan_for_updates

    Scans for updates on the device.

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


async def devices_update(request: web.Request, device_name, subscription_id, resource_group_name, manager_name, api_version, parameters) -> web.Response:
    """devices_update

    Patches the device.

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
    :param parameters: Patch representation of the device.
    :type parameters: dict | bytes

    """
    parameters = DevicePatch.from_dict(parameters)
    return web.Response(status=200)
