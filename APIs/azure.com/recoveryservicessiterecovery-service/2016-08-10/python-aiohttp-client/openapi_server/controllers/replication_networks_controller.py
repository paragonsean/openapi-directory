from typing import List, Dict
from aiohttp import web

from openapi_server.models.network import Network
from openapi_server.models.network_collection import NetworkCollection
from openapi_server import util


async def replication_networks_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, network_name) -> web.Response:
    """Gets a network with specified server id and network name.

    Gets the details of a network.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Server Id.
    :type fabric_name: str
    :param network_name: Primary network name.
    :type network_name: str

    """
    return web.Response(status=200)


async def replication_networks_list(request: web.Request, api_version, resource_name, resource_group_name, subscription_id) -> web.Response:
    """Gets the list of networks. View-only API.

    Lists the networks available in a vault

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def replication_networks_list_by_replication_fabrics(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the list of networks under a fabric.

    Lists the networks available for a fabric.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name
    :type fabric_name: str

    """
    return web.Response(status=200)
