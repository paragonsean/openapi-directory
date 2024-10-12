from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_list_result import AccountListResult
from openapi_server.models.account_update_parameters import AccountUpdateParameters
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def accounts_create_or_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, parameters) -> web.Response:
    """accounts_create_or_update

    Creates or updates a team account with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param parameters: The parameters for creating or updating a machine learning team account.
    :type parameters: dict | bytes

    """
    parameters = Account.from_dict(parameters)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_delete

    Deletes a machine learning team account.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, api_version, subscription_id, resource_group_name, account_name) -> web.Response:
    """accounts_get

    Gets the properties of the specified machine learning team account.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str

    """
    return web.Response(status=200)


async def accounts_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """accounts_list

    Lists all the available machine learning team accounts under the specified subscription.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """accounts_list_by_resource_group

    Lists all the available machine learning team accounts under the specified resource group.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def accounts_update(request: web.Request, api_version, subscription_id, resource_group_name, account_name, parameters) -> web.Response:
    """accounts_update

    Updates a machine learning team account with the specified parameters.

    :param api_version: The client API version.
    :type api_version: str
    :param subscription_id: The Microsoft Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group to which the machine learning team account belongs.
    :type resource_group_name: str
    :param account_name: The name of the machine learning team account.
    :type account_name: str
    :param parameters: The parameters for updating a machine learning team account.
    :type parameters: dict | bytes

    """
    parameters = AccountUpdateParameters.from_dict(parameters)
    return web.Response(status=200)
