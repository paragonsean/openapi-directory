from typing import List, Dict
from aiohttp import web

from openapi_server.models.fabric_error import FabricError
from openapi_server.models.gateway_resource_description import GatewayResourceDescription
from openapi_server.models.paged_gateway_resource_description_list import PagedGatewayResourceDescriptionList
from openapi_server import util


async def mesh_gateway_create_or_update(request: web.Request, api_version, gateway_resource_name, gateway_resource_description) -> web.Response:
    """Creates or updates a Gateway resource.

    Creates a Gateway resource with the specified name, description and properties. If Gateway resource with the same name exists, then it is updated with the specified description and properties. Use Gateway resource to provide public connectivity to application services.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param gateway_resource_name: The identity of the gateway.
    :type gateway_resource_name: str
    :param gateway_resource_description: Description for creating a Gateway resource.
    :type gateway_resource_description: dict | bytes

    """
    gateway_resource_description = GatewayResourceDescription.from_dict(gateway_resource_description)
    return web.Response(status=200)


async def mesh_gateway_delete(request: web.Request, api_version, gateway_resource_name) -> web.Response:
    """Deletes the Gateway resource.

    Deletes the Gateway resource identified by the name.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param gateway_resource_name: The identity of the gateway.
    :type gateway_resource_name: str

    """
    return web.Response(status=200)


async def mesh_gateway_get(request: web.Request, api_version, gateway_resource_name) -> web.Response:
    """Gets the Gateway resource with the given name.

    Gets the information about the Gateway resource with the given name. The information include the description and other properties of the Gateway.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str
    :param gateway_resource_name: The identity of the gateway.
    :type gateway_resource_name: str

    """
    return web.Response(status=200)


async def mesh_gateway_list(request: web.Request, api_version) -> web.Response:
    """Lists all the gateway resources.

    Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.

    :param api_version: The version of the API. This parameter is required and its value must be &#39;6.4-preview&#39;.
    :type api_version: str

    """
    return web.Response(status=200)
