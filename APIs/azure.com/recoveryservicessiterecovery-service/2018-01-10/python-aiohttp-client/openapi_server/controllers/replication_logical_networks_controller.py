from typing import List, Dict
from aiohttp import web

from openapi_server.models.logical_network import LogicalNetwork
from openapi_server.models.logical_network_collection import LogicalNetworkCollection
from openapi_server import util


async def replication_logical_networks_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, logical_network_name) -> web.Response:
    """Gets a logical network with specified server id and logical network name.

    Gets the details of a logical network.

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
    :param logical_network_name: Logical network name.
    :type logical_network_name: str

    """
    return web.Response(status=200)


async def replication_logical_networks_list_by_replication_fabrics(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name) -> web.Response:
    """Gets the list of logical networks under a fabric.

    Lists all the logical networks of the Azure Site Recovery fabric

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

    """
    return web.Response(status=200)
