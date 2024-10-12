from typing import List, Dict
from aiohttp import web

from openapi_server.models.bot import Bot
from openapi_server.models.bot_response_list import BotResponseList
from openapi_server.models.check_name_availability_request_body import CheckNameAvailabilityRequestBody
from openapi_server.models.check_name_availability_response_body import CheckNameAvailabilityResponseBody
from openapi_server.models.error import Error
from openapi_server import util


async def bots_create(request: web.Request, resource_group_name, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """bots_create

    Creates a Bot Service. Bot Service is a resource group wide resource type.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created bot.
    :type parameters: dict | bytes

    """
    parameters = Bot.from_dict(parameters)
    return web.Response(status=200)


async def bots_delete(request: web.Request, resource_group_name, resource_name, api_version, subscription_id) -> web.Response:
    """bots_delete

    Deletes a Bot Service from the resource group. 

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bots_get(request: web.Request, resource_group_name, resource_name, api_version, subscription_id) -> web.Response:
    """bots_get

    Returns a BotService specified by the parameters.

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bots_get_check_name_availability(request: web.Request, api_version, parameters) -> web.Response:
    """bots_get_check_name_availability

    Check whether a bot name is available.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request body parameters to provide for the check name availability request
    :type parameters: dict | bytes

    """
    parameters = CheckNameAvailabilityRequestBody.from_dict(parameters)
    return web.Response(status=200)


async def bots_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """bots_list

    Returns all the resources of a particular type belonging to a subscription.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def bots_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """bots_list_by_resource_group

    Returns all the resources of a particular type belonging to a resource group

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def bots_update(request: web.Request, resource_group_name, resource_name, api_version, subscription_id, parameters) -> web.Response:
    """bots_update

    Updates a Bot Service

    :param resource_group_name: The name of the Bot resource group in the user subscription.
    :type resource_group_name: str
    :param resource_name: The name of the Bot resource.
    :type resource_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Azure Subscription ID.
    :type subscription_id: str
    :param parameters: The parameters to provide for the created bot.
    :type parameters: dict | bytes

    """
    parameters = Bot.from_dict(parameters)
    return web.Response(status=200)
