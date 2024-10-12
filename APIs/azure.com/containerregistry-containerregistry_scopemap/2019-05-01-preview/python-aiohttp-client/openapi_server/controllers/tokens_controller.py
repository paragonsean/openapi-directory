from typing import List, Dict
from aiohttp import web

from openapi_server.models.token import Token
from openapi_server.models.token_list_result import TokenListResult
from openapi_server.models.token_update_parameters import TokenUpdateParameters
from openapi_server import util


async def tokens_create(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, token_name, token_create_parameters) -> web.Response:
    """tokens_create

    Creates a token for a container registry with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param token_name: The name of the token.
    :type token_name: str
    :param token_create_parameters: The parameters for creating a token.
    :type token_create_parameters: dict | bytes

    """
    token_create_parameters = Token.from_dict(token_create_parameters)
    return web.Response(status=200)


async def tokens_delete(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, token_name) -> web.Response:
    """tokens_delete

    Deletes a token from a container registry.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param token_name: The name of the token.
    :type token_name: str

    """
    return web.Response(status=200)


async def tokens_get(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, token_name) -> web.Response:
    """tokens_get

    Gets the properties of the specified token.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param token_name: The name of the token.
    :type token_name: str

    """
    return web.Response(status=200)


async def tokens_list(request: web.Request, api_version, subscription_id, resource_group_name, registry_name) -> web.Response:
    """tokens_list

    Lists all the tokens for the specified container registry.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str

    """
    return web.Response(status=200)


async def tokens_update(request: web.Request, api_version, subscription_id, resource_group_name, registry_name, token_name, token_update_parameters) -> web.Response:
    """tokens_update

    Updates a token with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the container registry belongs.
    :type resource_group_name: str
    :param registry_name: The name of the container registry.
    :type registry_name: str
    :param token_name: The name of the token.
    :type token_name: str
    :param token_update_parameters: The parameters for updating a token.
    :type token_update_parameters: dict | bytes

    """
    token_update_parameters = TokenUpdateParameters.from_dict(token_update_parameters)
    return web.Response(status=200)
