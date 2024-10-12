from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hana_instance import HanaInstance
from openapi_server.models.hana_instances_list_result import HanaInstancesListResult
from openapi_server.models.operation_list import OperationList
from openapi_server.models.sap_monitor import SapMonitor
from openapi_server.models.sap_monitor_list_result import SapMonitorListResult
from openapi_server.models.tags import Tags
from openapi_server import util


async def hana_instances_create(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name, hana_instance_parameter) -> web.Response:
    """Creates a SAP HANA instance.

    Creates a SAP HANA instance for the specified subscription, resource group, and instance name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str
    :param hana_instance_parameter: Request body representing a HanaInstance
    :type hana_instance_parameter: dict | bytes

    """
    hana_instance_parameter = HanaInstance.from_dict(hana_instance_parameter)
    return web.Response(status=200)


async def hana_instances_delete(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name) -> web.Response:
    """Deletes a SAP HANA instance.

    Deletes a SAP HANA instance with the specified subscription, resource group, and instance name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str

    """
    return web.Response(status=200)


async def hana_instances_get(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name) -> web.Response:
    """Gets properties of a SAP HANA instance.

    Gets properties of a SAP HANA instance for the specified subscription, resource group, and instance name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str

    """
    return web.Response(status=200)


async def hana_instances_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets a list of SAP HANA instances in the specified subscription.

    Gets a list of SAP HANA instances in the specified subscription. The operations returns various properties of each SAP HANA on Azure instance.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def hana_instances_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """Gets a list of SAP HANA instances in the specified subscription and the resource group.

    Gets a list of SAP HANA instances in the specified subscription and the resource group. The operations returns various properties of each SAP HANA on Azure instance.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def hana_instances_restart(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name) -> web.Response:
    """hana_instances_restart

    The operation to restart a SAP HANA instance.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str

    """
    return web.Response(status=200)


async def hana_instances_shutdown(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name) -> web.Response:
    """hana_instances_shutdown

    The operation to shutdown a SAP HANA instance.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str

    """
    return web.Response(status=200)


async def hana_instances_start(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name) -> web.Response:
    """hana_instances_start

    The operation to start a SAP HANA instance.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str

    """
    return web.Response(status=200)


async def hana_instances_update(request: web.Request, api_version, subscription_id, resource_group_name, hana_instance_name, tags_parameter) -> web.Response:
    """Patches the Tags field of a SAP HANA instance.

    Patches the Tags field of a SAP HANA instance for the specified subscription, resource group, and instance name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param hana_instance_name: Name of the SAP HANA on Azure instance.
    :type hana_instance_name: str
    :param tags_parameter: Request body that only contains the new Tags field
    :type tags_parameter: dict | bytes

    """
    tags_parameter = Tags.from_dict(tags_parameter)
    return web.Response(status=200)


async def operations_list(request: web.Request, api_version) -> web.Response:
    """operations_list

    Gets a list of SAP HANA management operations.

    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def sap_monitors_create(request: web.Request, api_version, subscription_id, resource_group_name, sap_monitor_name, sap_monitor_parameter) -> web.Response:
    """Creates a SAP monitor.

    Creates a SAP monitor for the specified subscription, resource group, and resource name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param sap_monitor_name: Name of the SAP monitor resource.
    :type sap_monitor_name: str
    :param sap_monitor_parameter: Request body representing a SAP Monitor
    :type sap_monitor_parameter: dict | bytes

    """
    sap_monitor_parameter = SapMonitor.from_dict(sap_monitor_parameter)
    return web.Response(status=200)


async def sap_monitors_delete(request: web.Request, api_version, subscription_id, resource_group_name, sap_monitor_name) -> web.Response:
    """Deletes a SAP monitor.

    Deletes a SAP monitor with the specified subscription, resource group, and monitor name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param sap_monitor_name: Name of the SAP monitor resource.
    :type sap_monitor_name: str

    """
    return web.Response(status=200)


async def sap_monitors_get(request: web.Request, api_version, subscription_id, resource_group_name, sap_monitor_name) -> web.Response:
    """Gets properties of a SAP monitor.

    Gets properties of a SAP monitor for the specified subscription, resource group, and resource name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param sap_monitor_name: Name of the SAP monitor resource.
    :type sap_monitor_name: str

    """
    return web.Response(status=200)


async def sap_monitors_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """Gets a list of SAP monitors in the specified subscription.

    Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def sap_monitors_update(request: web.Request, api_version, subscription_id, resource_group_name, sap_monitor_name, tags_parameter) -> web.Response:
    """Patches the Tags field of a SAP monitor.

    Patches the Tags field of a SAP monitor for the specified subscription, resource group, and monitor name.

    :param api_version: Client API version.
    :type api_version: str
    :param subscription_id: Subscription ID which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param sap_monitor_name: Name of the SAP monitor resource.
    :type sap_monitor_name: str
    :param tags_parameter: Request body that only contains the new Tags field
    :type tags_parameter: dict | bytes

    """
    tags_parameter = Tags.from_dict(tags_parameter)
    return web.Response(status=200)
