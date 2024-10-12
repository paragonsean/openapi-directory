from typing import List, Dict
from aiohttp import web

from openapi_server.models.infra_role_instance import InfraRoleInstance
from openapi_server.models.infra_role_instance_list import InfraRoleInstanceList
from openapi_server import util


async def infra_role_instances_get(request: web.Request, subscription_id, resource_group_name, location, infra_role_instance, api_version) -> web.Response:
    """infra_role_instances_get

    Return the requested infrastructure role instance.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param infra_role_instance: Name of an infrastructure role instance.
    :type infra_role_instance: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def infra_role_instances_list(request: web.Request, subscription_id, resource_group_name, location, api_version, filter=None) -> web.Response:
    """infra_role_instances_list

    Returns a list of all infrastructure role instances at a location.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str
    :param filter: OData filter parameter.
    :type filter: str

    """
    return web.Response(status=200)


async def infra_role_instances_power_off(request: web.Request, subscription_id, resource_group_name, location, infra_role_instance, api_version) -> web.Response:
    """infra_role_instances_power_off

    Power off an infrastructure role instance.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param infra_role_instance: Name of an infrastructure role instance.
    :type infra_role_instance: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def infra_role_instances_power_on(request: web.Request, subscription_id, resource_group_name, location, infra_role_instance, api_version) -> web.Response:
    """infra_role_instances_power_on

    Power on an infrastructure role instance.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param infra_role_instance: Name of an infrastructure role instance.
    :type infra_role_instance: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def infra_role_instances_reboot(request: web.Request, subscription_id, resource_group_name, location, infra_role_instance, api_version) -> web.Response:
    """infra_role_instances_reboot

    Reboot an infrastructure role instance.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param infra_role_instance: Name of an infrastructure role instance.
    :type infra_role_instance: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def infra_role_instances_shutdown(request: web.Request, subscription_id, resource_group_name, location, infra_role_instance, api_version) -> web.Response:
    """infra_role_instances_shutdown

    Shut down an infrastructure role instance.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: Name of the resource group.
    :type resource_group_name: str
    :param location: Location of the resource.
    :type location: str
    :param infra_role_instance: Name of an infrastructure role instance.
    :type infra_role_instance: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
