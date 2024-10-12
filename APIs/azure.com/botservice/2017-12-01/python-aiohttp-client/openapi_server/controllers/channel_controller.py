from typing import List, Dict
from aiohttp import web

from openapi_server.models.bot_channel import BotChannel
from openapi_server.models.channel_response_list import ChannelResponseList
from openapi_server.models.error import Error
from openapi_server import util


async def channels_create(request: web.Request, resource_group_name, resource_name, channel_name, api_version, subscription_id, parameters) -> web.Response:
    """channels_create

    Creates a Channel registration for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param channel_name: The name of the Channel resource.
    :type channel_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created bot.
    :type parameters: dict | bytes

    """
    parameters = BotChannel.from_dict(parameters)
    return web.Response(status=200)


async def channels_delete(request: web.Request, resource_group_name, resource_name, channel_name, api_version, subscription_id) -> web.Response:
    """channels_delete

    Deletes a Channel registration from a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param channel_name: The name of the Bot resource.
    :type channel_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def channels_get(request: web.Request, resource_group_name, resource_name, channel_name, api_version, subscription_id) -> web.Response:
    """channels_get

    Returns a BotService Channel registration specified by the parameters.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param channel_name: The name of the Bot resource.
    :type channel_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def channels_list_by_resource_group(request: web.Request, resource_group_name, resource_name, subscription_id, api_version) -> web.Response:
    """channels_list_by_resource_group

    Returns all the Channel registrations of a particular BotService resource

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str

    """
    return web.Response(status=200)


async def channels_list_with_keys(request: web.Request, resource_group_name, resource_name, channel_name, api_version, subscription_id) -> web.Response:
    """channels_list_with_keys

    Lists a Channel registration for a Bot Service including secrets

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param channel_name: The name of the Channel resource.
    :type channel_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def channels_update(request: web.Request, resource_group_name, resource_name, channel_name, api_version, subscription_id, parameters) -> web.Response:
    """channels_update

    Updates a Channel registration for a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param channel_name: The name of the Channel resource.
    :type channel_name: str
    :param api_version: Version of the API to be used with the client request. Current version is 2017-12-01
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created bot.
    :type parameters: dict | bytes

    """
    parameters = BotChannel.from_dict(parameters)
    return web.Response(status=200)
