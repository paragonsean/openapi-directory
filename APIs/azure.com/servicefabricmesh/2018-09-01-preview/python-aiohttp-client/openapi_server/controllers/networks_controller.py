from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.network_resource_description import NetworkResourceDescription
from openapi_server.models.network_resource_description_list import NetworkResourceDescriptionList
from openapi_server import util


async def network_create(request: web.Request, subscription_id, api_version, resource_group_name, network_resource_name, network_resource_description) -> web.Response:
    """Creates or updates a network resource.

    Creates a network resource with the specified name, description and properties. If a network resource with the same name exists, then it is updated with the specified description and properties.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param network_resource_name: The identity of the network.
    :type network_resource_name: str
    :param network_resource_description: Description for creating a Network resource.
    :type network_resource_description: dict | bytes

    """
    network_resource_description = NetworkResourceDescription.from_dict(network_resource_description)
    return web.Response(status=200)


async def network_delete(request: web.Request, subscription_id, api_version, resource_group_name, network_resource_name) -> web.Response:
    """Deletes the network resource.

    Deletes the network resource identified by the name.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param network_resource_name: The identity of the network.
    :type network_resource_name: str

    """
    return web.Response(status=200)


async def network_get(request: web.Request, subscription_id, api_version, resource_group_name, network_resource_name) -> web.Response:
    """Gets the network resource with the given name.

    Gets the information about the network resource with the given name. The information include the description and other properties of the network.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str
    :param network_resource_name: The identity of the network.
    :type network_resource_name: str

    """
    return web.Response(status=200)


async def network_list_by_resource_group(request: web.Request, subscription_id, api_version, resource_group_name) -> web.Response:
    """Gets all the network resources in a given resource group.

    Gets the information about all network resources in a given resource group. The information include the description and other properties of the Network.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str
    :param resource_group_name: Azure resource group name
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def network_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """Gets all the network resources in a given subscription.

    Gets the information about all network resources in a given resource group. The information include the description and other properties of the network.

    :param subscription_id: The customer subscription identifier
    :type subscription_id: str
    :param api_version: The version of the API. This parameter is required and its value must be &#x60;2018-09-01-preview&#x60;.
    :type api_version: str

    """
    return web.Response(status=200)
