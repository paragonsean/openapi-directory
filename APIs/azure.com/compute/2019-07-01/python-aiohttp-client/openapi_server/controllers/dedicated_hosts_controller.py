from typing import List, Dict
from aiohttp import web

from openapi_server.models.dedicated_host import DedicatedHost
from openapi_server.models.dedicated_host_update import DedicatedHostUpdate
from openapi_server import util


async def dedicated_hosts_create_or_update(request: web.Request, resource_group_name, host_group_name, host_name, api_version, subscription_id, parameters) -> web.Response:
    """dedicated_hosts_create_or_update

    Create or update a dedicated host .

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param host_name: The name of the dedicated host .
    :type host_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Dedicated Host.
    :type parameters: dict | bytes

    """
    parameters = DedicatedHost.from_dict(parameters)
    return web.Response(status=200)


async def dedicated_hosts_delete(request: web.Request, resource_group_name, host_group_name, host_name, api_version, subscription_id) -> web.Response:
    """dedicated_hosts_delete

    Delete a dedicated host.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param host_name: The name of the dedicated host.
    :type host_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def dedicated_hosts_get(request: web.Request, resource_group_name, host_group_name, host_name, api_version, subscription_id, expand=None) -> web.Response:
    """dedicated_hosts_get

    Retrieves information about a dedicated host.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param host_name: The name of the dedicated host.
    :type host_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def dedicated_hosts_update(request: web.Request, resource_group_name, host_group_name, host_name, api_version, subscription_id, parameters) -> web.Response:
    """dedicated_hosts_update

    Update an dedicated host .

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param host_group_name: The name of the dedicated host group.
    :type host_group_name: str
    :param host_name: The name of the dedicated host .
    :type host_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Dedicated Host operation.
    :type parameters: dict | bytes

    """
    parameters = DedicatedHostUpdate.from_dict(parameters)
    return web.Response(status=200)
