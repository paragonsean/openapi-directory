from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.content_key_policy import ContentKeyPolicy
from openapi_server.models.content_key_policy_collection import ContentKeyPolicyCollection
from openapi_server.models.content_key_policy_properties import ContentKeyPolicyProperties
from openapi_server import util


async def content_key_policies_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, content_key_policy_name, api_version, parameters) -> web.Response:
    """Create or update an Content Key Policy

    Create or update a Content Key Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param content_key_policy_name: The Content Key Policy name.
    :type content_key_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = ContentKeyPolicy.from_dict(parameters)
    return web.Response(status=200)


async def content_key_policies_delete(request: web.Request, subscription_id, resource_group_name, account_name, content_key_policy_name, api_version) -> web.Response:
    """Delete a Content Key Policy

    Deletes a Content Key Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param content_key_policy_name: The Content Key Policy name.
    :type content_key_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def content_key_policies_get(request: web.Request, subscription_id, resource_group_name, account_name, content_key_policy_name, api_version) -> web.Response:
    """Get a Content Key Policy

    Get the details of a Content Key Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param content_key_policy_name: The Content Key Policy name.
    :type content_key_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def content_key_policies_get_policy_properties_with_secrets(request: web.Request, subscription_id, resource_group_name, account_name, content_key_policy_name, api_version) -> web.Response:
    """Get a Content Key Policy with secrets

    Get a Content Key Policy including secret values

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param content_key_policy_name: The Content Key Policy name.
    :type content_key_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def content_key_policies_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter=None, top=None, orderby=None) -> web.Response:
    """List Content Key Policies

    Lists the Content Key Policies in the account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param filter: Restricts the set of items returned.
    :type filter: str
    :param top: Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
    :type top: int
    :param orderby: Specifies the key by which the result collection should be ordered.
    :type orderby: str

    """
    return web.Response(status=200)


async def content_key_policies_update(request: web.Request, subscription_id, resource_group_name, account_name, content_key_policy_name, api_version, parameters) -> web.Response:
    """Update a Content Key Policy

    Updates an existing Content Key Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param content_key_policy_name: The Content Key Policy name.
    :type content_key_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = ContentKeyPolicy.from_dict(parameters)
    return web.Response(status=200)
