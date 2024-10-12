from typing import List, Dict
from aiohttp import web

from openapi_server.models.connection_setting import ConnectionSetting
from openapi_server.models.connection_setting_response_list import ConnectionSettingResponseList
from openapi_server.models.error import Error
from openapi_server import util


async def bot_connection_create(request: web.Request, resource_group_name, resource_name, connection_name, api_version, subscription_id, parameters) -> web.Response:
    """bot_connection_create

    Register a new Auth Connection for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param connection_name: The name of the Bot Service Connection Setting resource
    :type connection_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for creating the Connection Setting.
    :type parameters: dict | bytes

    """
    parameters = ConnectionSetting.from_dict(parameters)
    return web.Response(status=200)


async def bot_connection_delete(request: web.Request, resource_group_name, resource_name, connection_name, api_version, subscription_id) -> web.Response:
    """bot_connection_delete

    Deletes a Connection Setting registration for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param connection_name: The name of the Bot Service Connection Setting resource
    :type connection_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bot_connection_get(request: web.Request, resource_group_name, resource_name, connection_name, api_version, subscription_id) -> web.Response:
    """bot_connection_get

    Get a Connection Setting registration for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param connection_name: The name of the Bot Service Connection Setting resource
    :type connection_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bot_connection_list_by_bot_service(request: web.Request, resource_group_name, resource_name, subscription_id, api_version) -> web.Response:
    """bot_connection_list_by_bot_service

    Returns all the Connection Settings registered to a particular BotService resource

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def bot_connection_list_with_secrets(request: web.Request, resource_group_name, resource_name, connection_name, api_version, subscription_id) -> web.Response:
    """bot_connection_list_with_secrets

    Get a Connection Setting registration for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param connection_name: The name of the Bot Service Connection Setting resource
    :type connection_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bot_connection_update(request: web.Request, resource_group_name, resource_name, connection_name, api_version, subscription_id, parameters) -> web.Response:
    """bot_connection_update

    Updates a Connection Setting registration for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param connection_name: The name of the Bot Service Connection Setting resource
    :type connection_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for updating the Connection Setting.
    :type parameters: dict | bytes

    """
    parameters = ConnectionSetting.from_dict(parameters)
    return web.Response(status=200)
