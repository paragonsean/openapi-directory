from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_content_keys_response import ListContentKeysResponse
from openapi_server.models.list_paths_response import ListPathsResponse
from openapi_server.models.streaming_locator import StreamingLocator
from openapi_server.models.streaming_locator_collection import StreamingLocatorCollection
from openapi_server.models.streaming_locators_list_default_response import StreamingLocatorsListDefaultResponse
from openapi_server.models.streaming_policy import StreamingPolicy
from openapi_server.models.streaming_policy_collection import StreamingPolicyCollection
from openapi_server import util


async def streaming_locators_create(request: web.Request, subscription_id, resource_group_name, account_name, streaming_locator_name, api_version, parameters) -> web.Response:
    """Create a Streaming Locator

    Create a Streaming Locator in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_locator_name: The Streaming Locator name.
    :type streaming_locator_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = StreamingLocator.from_dict(parameters)
    return web.Response(status=200)


async def streaming_locators_delete(request: web.Request, subscription_id, resource_group_name, account_name, streaming_locator_name, api_version) -> web.Response:
    """Delete a Streaming Locator

    Deletes a Streaming Locator in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_locator_name: The Streaming Locator name.
    :type streaming_locator_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_locators_get(request: web.Request, subscription_id, resource_group_name, account_name, streaming_locator_name, api_version) -> web.Response:
    """Get a Streaming Locator

    Get the details of a Streaming Locator in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_locator_name: The Streaming Locator name.
    :type streaming_locator_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_locators_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter=None, top=None, orderby=None) -> web.Response:
    """List Streaming Locators

    Lists the Streaming Locators in the account

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


async def streaming_locators_list_content_keys(request: web.Request, subscription_id, resource_group_name, account_name, streaming_locator_name, api_version) -> web.Response:
    """List Content Keys

    List Content Keys used by this Streaming Locator

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_locator_name: The Streaming Locator name.
    :type streaming_locator_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_locators_list_paths(request: web.Request, subscription_id, resource_group_name, account_name, streaming_locator_name, api_version) -> web.Response:
    """List Paths

    List Paths supported by this Streaming Locator

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_locator_name: The Streaming Locator name.
    :type streaming_locator_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_policies_create(request: web.Request, subscription_id, resource_group_name, account_name, streaming_policy_name, api_version, parameters) -> web.Response:
    """Create a Streaming Policy

    Create a Streaming Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_policy_name: The Streaming Policy name.
    :type streaming_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = StreamingPolicy.from_dict(parameters)
    return web.Response(status=200)


async def streaming_policies_delete(request: web.Request, subscription_id, resource_group_name, account_name, streaming_policy_name, api_version) -> web.Response:
    """Delete a Streaming Policy

    Deletes a Streaming Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_policy_name: The Streaming Policy name.
    :type streaming_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_policies_get(request: web.Request, subscription_id, resource_group_name, account_name, streaming_policy_name, api_version) -> web.Response:
    """Get a Streaming Policy

    Get the details of a Streaming Policy in the Media Services account

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param streaming_policy_name: The Streaming Policy name.
    :type streaming_policy_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def streaming_policies_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version, filter=None, top=None, orderby=None) -> web.Response:
    """List Streaming Policies

    Lists the Streaming Policies in the account

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
