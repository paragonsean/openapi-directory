from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_network_group import ManagedNetworkGroup
from openapi_server.models.managed_network_group_list_result import ManagedNetworkGroupListResult
from openapi_server import util


async def managed_network_groups_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network_group_name, managed_network_group) -> web.Response:
    """managed_network_groups_create_or_update

    The Put ManagedNetworkGroups operation creates or updates a Managed Network Group resource

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network_group_name: The name of the Managed Network Group.
    :type managed_network_group_name: str
    :param managed_network_group: Parameters supplied to the create/update a Managed Network Group resource
    :type managed_network_group: dict | bytes

    """
    managed_network_group = ManagedNetworkGroup.from_dict(managed_network_group)
    return web.Response(status=200)


async def managed_network_groups_delete(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network_group_name) -> web.Response:
    """managed_network_groups_delete

    The Delete ManagedNetworkGroups operation deletes a Managed Network Group specified by the resource group, Managed Network name, and group name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network_group_name: The name of the Managed Network Group.
    :type managed_network_group_name: str

    """
    return web.Response(status=200)


async def managed_network_groups_get(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network_group_name) -> web.Response:
    """managed_network_groups_get

    The Get ManagedNetworkGroups operation gets a Managed Network Group specified by the resource group, Managed Network name, and group name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network_group_name: The name of the Managed Network Group.
    :type managed_network_group_name: str

    """
    return web.Response(status=200)


async def managed_network_groups_list_by_managed_network(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, top=None, skiptoken=None) -> web.Response:
    """managed_network_groups_list_by_managed_network

    The ListByManagedNetwork ManagedNetworkGroup operation retrieves all the Managed Network Groups in a specified Managed Networks in a paginated format.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param top: May be used to limit the number of results in a page for list queries.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)
