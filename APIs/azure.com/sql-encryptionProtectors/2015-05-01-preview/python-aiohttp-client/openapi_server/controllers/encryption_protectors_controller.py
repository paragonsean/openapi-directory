from typing import List, Dict
from aiohttp import web

from openapi_server.models.encryption_protector import EncryptionProtector
from openapi_server.models.encryption_protector_list_result import EncryptionProtectorListResult
from openapi_server import util


async def encryption_protectors_create_or_update(request: web.Request, resource_group_name, server_name, encryption_protector_name, subscription_id, api_version, parameters) -> web.Response:
    """encryption_protectors_create_or_update

    Updates an existing encryption protector.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param encryption_protector_name: The name of the encryption protector to be updated.
    :type encryption_protector_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str
    :param parameters: The requested encryption protector resource state.
    :type parameters: dict | bytes

    """
    parameters = EncryptionProtector.from_dict(parameters)
    return web.Response(status=200)


async def encryption_protectors_get(request: web.Request, resource_group_name, server_name, encryption_protector_name, subscription_id, api_version) -> web.Response:
    """encryption_protectors_get

    Gets a server encryption protector.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param encryption_protector_name: The name of the encryption protector to be retrieved.
    :type encryption_protector_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def encryption_protectors_list_by_server(request: web.Request, resource_group_name, server_name, subscription_id, api_version) -> web.Response:
    """encryption_protectors_list_by_server

    Gets a list of server encryption protectors

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)


async def encryption_protectors_revalidate(request: web.Request, resource_group_name, server_name, encryption_protector_name, subscription_id, api_version) -> web.Response:
    """encryption_protectors_revalidate

    Revalidates an existing encryption protector.

    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param encryption_protector_name: The name of the encryption protector to be updated.
    :type encryption_protector_name: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param api_version: The API version to use for the request.
    :type api_version: str

    """
    return web.Response(status=200)
