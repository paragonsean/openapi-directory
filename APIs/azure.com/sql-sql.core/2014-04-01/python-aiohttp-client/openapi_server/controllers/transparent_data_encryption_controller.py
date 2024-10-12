from typing import List, Dict
from aiohttp import web

from openapi_server.models.transparent_data_encryption import TransparentDataEncryption
from openapi_server.models.transparent_data_encryption_activity_list_result import TransparentDataEncryptionActivityListResult
from openapi_server import util


async def transparent_data_encryption_activities_list_by_configuration(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, transparent_data_encryption_name) -> web.Response:
    """transparent_data_encryption_activities_list_by_configuration

    Returns a database&#39;s transparent data encryption operation result.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database for which the transparent data encryption applies.
    :type database_name: str
    :param transparent_data_encryption_name: The name of the transparent data encryption configuration.
    :type transparent_data_encryption_name: str

    """
    return web.Response(status=200)


async def transparent_data_encryptions_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, transparent_data_encryption_name, parameters) -> web.Response:
    """transparent_data_encryptions_create_or_update

    Creates or updates a database&#39;s transparent data encryption configuration.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database for which setting the transparent data encryption applies.
    :type database_name: str
    :param transparent_data_encryption_name: The name of the transparent data encryption configuration.
    :type transparent_data_encryption_name: str
    :param parameters: The required parameters for creating or updating transparent data encryption.
    :type parameters: dict | bytes

    """
    parameters = TransparentDataEncryption.from_dict(parameters)
    return web.Response(status=200)


async def transparent_data_encryptions_get(request: web.Request, api_version, subscription_id, resource_group_name, server_name, database_name, transparent_data_encryption_name) -> web.Response:
    """transparent_data_encryptions_get

    Gets a database&#39;s transparent data encryption configuration.

    :param api_version: The API version to use for the request.
    :type api_version: str
    :param subscription_id: The subscription ID that identifies an Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param server_name: The name of the server.
    :type server_name: str
    :param database_name: The name of the database for which the transparent data encryption applies.
    :type database_name: str
    :param transparent_data_encryption_name: The name of the transparent data encryption configuration.
    :type transparent_data_encryption_name: str

    """
    return web.Response(status=200)
