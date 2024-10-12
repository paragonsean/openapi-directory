from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.virtual_network import VirtualNetwork
from openapi_server.models.virtual_network_fragment import VirtualNetworkFragment
from openapi_server.models.virtual_network_list import VirtualNetworkList
from openapi_server import util


async def virtual_networks_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, virtual_network) -> web.Response:
    """virtual_networks_create_or_update

    Create or replace an existing virtual network. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual network.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param virtual_network: A virtual network.
    :type virtual_network: dict | bytes

    """
    virtual_network = VirtualNetwork.from_dict(virtual_network)
    return web.Response(status=200)


async def virtual_networks_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """virtual_networks_delete

    Delete virtual network. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual network.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def virtual_networks_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """virtual_networks_get

    Get virtual network.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual network.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;externalSubnets)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def virtual_networks_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """virtual_networks_list

    List virtual networks in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($expand&#x3D;externalSubnets)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation. Example: &#39;$filter&#x3D;contains(name,&#39;myName&#39;)
    :type filter: str
    :param top: The maximum number of resources to return from the operation. Example: &#39;$top&#x3D;10&#39;
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation. Example: &#39;$orderby&#x3D;name desc&#39;
    :type orderby: str

    """
    return web.Response(status=200)


async def virtual_networks_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, virtual_network) -> web.Response:
    """virtual_networks_update

    Allows modifying tags of virtual networks. All other properties will be ignored.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the virtual network.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param virtual_network: A virtual network.
    :type virtual_network: dict | bytes

    """
    virtual_network = VirtualNetworkFragment.from_dict(virtual_network)
    return web.Response(status=200)
