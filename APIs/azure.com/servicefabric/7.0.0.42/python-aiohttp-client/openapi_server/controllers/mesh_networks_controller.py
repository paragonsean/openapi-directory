from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.network_resource_description import NetworkResourceDescription
from openapi_server.models.paged_network_resource_description_list import PagedNetworkResourceDescriptionList
from openapi_server import util


async def mesh_network_create_or_update(request: web.Request, api_version, network_resource_name, network_resource_description) -> web.Response:
    """Creates or updates a Network resource.

    Creates a Network resource with the specified name, description and properties. If Network resource with the same name exists, then it is updated with the specified description and properties. Network resource provides connectivity between application services.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param network_resource_name: The identity of the network.
    :type network_resource_name: str
    :param network_resource_description: Description for creating a Network resource.
    :type network_resource_description: dict | bytes

    """
    network_resource_description = NetworkResourceDescription.from_dict(network_resource_description)
    return web.Response(status=200)


async def mesh_network_delete(request: web.Request, api_version, network_resource_name) -> web.Response:
    """Deletes the Network resource.

    Deletes the Network resource identified by the name.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param network_resource_name: The identity of the network.
    :type network_resource_name: str

    """
    return web.Response(status=200)


async def mesh_network_get(request: web.Request, api_version, network_resource_name) -> web.Response:
    """Gets the Network resource with the given name.

    Gets the information about the Network resource with the given name. The information include the description and other properties of the Network.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param network_resource_name: The identity of the network.
    :type network_resource_name: str

    """
    return web.Response(status=200)


async def mesh_network_list(request: web.Request, api_version) -> web.Response:
    """Lists all the network resources.

    Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str

    """
    return web.Response(status=200)
