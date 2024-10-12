from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.gateway_resource_description import GatewayResourceDescription
from openapi_server.models.gateway_resource_description_list import GatewayResourceDescriptionList
from openapi_server import util


async def gateway_create(request: web.Request, subscription_id, api_version, resource_group_name, gateway_resource_name, gateway_resource_description) -> web.Response:
    """Creates or updates a gateway resource.

    Creates a gateway resource with the specified name, description and properties. If a gateway resource with the same name exists, then it is updated with the specified description and properties. Use gateway resources to create a gateway for public connectivity for services within your application.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param gateway_resource_name: The identity of the gateway.
    :type gateway_resource_name: str
    :param gateway_resource_description: Description for creating a Gateway resource.
    :type gateway_resource_description: dict | bytes

    """
    gateway_resource_description = GatewayResourceDescription.from_dict(gateway_resource_description)
    return web.Response(status=200)


async def gateway_delete(request: web.Request, subscription_id, api_version, resource_group_name, gateway_resource_name) -> web.Response:
    """Deletes the gateway resource.

    Deletes the gateway resource identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param gateway_resource_name: The identity of the gateway.
    :type gateway_resource_name: str

    """
    return web.Response(status=200)


async def gateway_get(request: web.Request, subscription_id, api_version, resource_group_name, gateway_resource_name) -> web.Response:
    """Gets the gateway resource with the given name.

    Gets the information about the gateway resource with the given name. The information include the description and other properties of the gateway.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param gateway_resource_name: The identity of the gateway.
    :type gateway_resource_name: str

    """
    return web.Response(status=200)


async def gateway_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the gateway resources in a given resource group.

    Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the Gateway.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def gateway_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the gateway resources in a given subscription.

    Gets the information about all gateway resources in a given resource group. The information include the description and other properties of the gateway.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
