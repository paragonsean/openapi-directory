from typing import List, Dict
from aiohttp import web

from openapi_server.models.server_communication_link import ServerCommunicationLink
from openapi_server.models.server_communication_link_list_result import ServerCommunicationLinkListResult
from openapi_server import util


async def server_communication_links_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, communication_link_name, parameters) -> web.Response:
    """server_communication_links_create_or_update

    Creates a server communication link.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param communication_link_name: The name of the server communication link.
    :type communication_link_name: str
    :param parameters: The required parameters for creating a server communication link.
    :type parameters: dict | bytes

    """
    parameters = ServerCommunicationLink.from_dict(parameters)
    return web.Response(status=200)


async def server_communication_links_delete(request: web.Request, api_version, subscription_id, resource_group_name, server_name, communication_link_name) -> web.Response:
    """server_communication_links_delete

    Deletes a server communication link.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param communication_link_name: The name of the server communication link.
    :type communication_link_name: str

    """
    return web.Response(status=200)


async def server_communication_links_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, communication_link_name) -> web.Response:
    """server_communication_links_get

    Returns a server communication link.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param communication_link_name: The name of the server communication link.
    :type communication_link_name: str

    """
    return web.Response(status=200)


async def server_communication_links_list_by_server(request: web.Request, api_version, subscription_id, resource_group_name, server_name) -> web.Response:
    """server_communication_links_list_by_server

    Gets a list of server communication links.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str

    """
    return web.Response(status=200)
