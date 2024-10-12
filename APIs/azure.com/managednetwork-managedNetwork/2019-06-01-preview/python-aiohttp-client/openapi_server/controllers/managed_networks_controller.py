from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.managed_network import ManagedNetwork
from openapi_server.models.managed_network_list_result import ManagedNetworkListResult
from openapi_server.models.managed_network_update import ManagedNetworkUpdate
from openapi_server import util


async def managed_networks_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, managed_network) -> web.Response:
    """managed_networks_create_or_update

    The Put ManagedNetworks operation creates/updates a Managed Network Resource, specified by resource group and Managed Network name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param managed_network: Parameters supplied to the create/update a Managed Network Resource
    :type managed_network: dict | bytes

    """
    managed_network = ManagedNetwork.from_dict(managed_network)
    return web.Response(status=200)


async def managed_networks_delete(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name) -> web.Response:
    """managed_networks_delete

    The Delete ManagedNetworks operation deletes a Managed Network Resource, specified by the  resource group and Managed Network name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str

    """
    return web.Response(status=200)


async def managed_networks_get(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name) -> web.Response:
    """managed_networks_get

    The Get ManagedNetworks operation gets a Managed Network Resource, specified by the resource group and Managed Network name

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str

    """
    return web.Response(status=200)


async def managed_networks_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name, top=None, skiptoken=None) -> web.Response:
    """managed_networks_list_by_resource_group

    The ListByResourceGroup ManagedNetwork operation retrieves all the Managed Network resources in a resource group in a paginated format.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param top: May be used to limit the number of results in a page for list queries.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def managed_networks_list_by_subscription(request: web.Request, api_version, subscription_id, top=None, skiptoken=None) -> web.Response:
    """managed_networks_list_by_subscription

    The ListBySubscription  ManagedNetwork operation retrieves all the Managed Network Resources in the current subscription in a paginated format.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param top: May be used to limit the number of results in a page for list queries.
    :type top: int
    :param skiptoken: Skiptoken is only used if a previous operation returned a partial result. If a previous response contains a nextLink element, the value of the nextLink element will include a skiptoken parameter that specifies a starting point to use for subsequent calls.
    :type skiptoken: str

    """
    return web.Response(status=200)


async def managed_networks_update(request: web.Request, api_version, subscription_id, resource_group_name, managed_network_name, parameters) -> web.Response:
    """managed_networks_update

    Updates the specified Managed Network resource tags.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param managed_network_name: The name of the Managed Network.
    :type managed_network_name: str
    :param parameters: Parameters supplied to update application gateway tags and/or scope.
    :type parameters: dict | bytes

    """
    parameters = ManagedNetworkUpdate.from_dict(parameters)
    return web.Response(status=200)
