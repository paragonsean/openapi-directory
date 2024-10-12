from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_network_peering_policy import ManagedNetworkPeeringPolicy
from openapi_server.models.managed_network_peering_policy_list_result import ManagedNetworkPeeringPolicyListResult
from openapi_server import util


async def managed_network_peering_policies_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network_peering_policy_name, managed_network_policy) -> web.Response:
    """managed_network_peering_policies_create_or_update

    The Put ManagedNetworkPeeringPolicies operation creates/updates a new Managed Network Peering Policy

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
    :type managed_network_peering_policy_name: str
    :param managed_network_policy: Parameters supplied to create/update a Managed Network Peering Policy
    :type managed_network_policy: dict | bytes

    """
    managed_network_policy = ManagedNetworkPeeringPolicy.from_dict(managed_network_policy)
    return web.Response(status=200)


async def managed_network_peering_policies_delete(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network_peering_policy_name) -> web.Response:
    """managed_network_peering_policies_delete

    The Delete ManagedNetworkPeeringPolicies operation deletes a Managed Network Peering Policy, specified by the  resource group, Managed Network name, and peering policy name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
    :type managed_network_peering_policy_name: str

    """
    return web.Response(status=200)


async def managed_network_peering_policies_get(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network_peering_policy_name) -> web.Response:
    """managed_network_peering_policies_get

    The Get ManagedNetworkPeeringPolicies operation gets a Managed Network Peering Policy resource, specified by the  resource group, Managed Network name, and peering policy name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network_peering_policy_name: The name of the Managed Network Peering Policy.
    :type managed_network_peering_policy_name: str

    """
    return web.Response(status=200)


async def managed_network_peering_policies_list_by_managed_network(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, top=None, skiptoken=None) -> web.Response:
    """managed_network_peering_policies_list_by_managed_network

    The ListByManagedNetwork PeeringPolicies operation retrieves all the Managed Network Peering Policies in a specified Managed Network, in a paginated format.

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
