from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_filter import AccountFilter
from openapi_server.models.account_filter_collection import AccountFilterCollection
from openapi_server.models.api_error import ApiError
from openapi_server import util


async def account_filters_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, filter_name, api_version, parameters) -> web.Response:
    """Create or update an Account Filter

    Creates or updates an Account Filter in the Media Services account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param filter_name: The Account Filter name
    :type filter_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = AccountFilter.from_dict(parameters)
    return web.Response(status=200)


async def account_filters_delete(request: web.Request, subscription_id, resource_group_name, account_name, filter_name, api_version) -> web.Response:
    """Delete an Account Filter.

    Deletes an Account Filter in the Media Services account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param filter_name: The Account Filter name
    :type filter_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def account_filters_get(request: web.Request, subscription_id, resource_group_name, account_name, filter_name, api_version) -> web.Response:
    """Get an Account Filter.

    Get the details of an Account Filter in the Media Services account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param filter_name: The Account Filter name
    :type filter_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def account_filters_list(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """List Account Filters

    List Account Filters in the Media Services account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def account_filters_update(request: web.Request, subscription_id, resource_group_name, account_name, filter_name, api_version, parameters) -> web.Response:
    """Update an Account Filter

    Updates an existing Account Filter in the Media Services account.

    :param subscription_id: The unique identifier for a Microsoft Azure subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group within the Azure subscription.
    :type resource_group_name: str
    :param account_name: The Media Services account name.
    :type account_name: str
    :param filter_name: The Account Filter name
    :type filter_name: str
    :param api_version: The Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The request parameters
    :type parameters: dict | bytes

    """
    parameters = AccountFilter.from_dict(parameters)
    return web.Response(status=200)
