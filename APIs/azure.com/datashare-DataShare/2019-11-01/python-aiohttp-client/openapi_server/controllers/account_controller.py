from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_list import AccountList
from openapi_server.models.account_update_parameters import AccountUpdateParameters
from openapi_server.models.data_share_error import DataShareError
from openapi_server.models.operation_response import OperationResponse
from openapi_server import util


async def accounts_create(request: web.Request, subscription_id, resource_group_name, account_name, api_version, account) -> web.Response:
    """Create an account in the given resource group

    Create an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param account: The account payload.
    :type account: dict | bytes

    """
    account = Account.from_dict(account)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Delete an account

    DeleteAccount

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """Get an account under a resource group

    Get an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param api_version: The api version to use.
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version, skip_token=None) -> web.Response:
    """List Accounts in a resource group

    List Accounts in ResourceGroup

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: Continuation token
    :type skip_token: str

    """
    return web.Response(status=200)


async def accounts_list_by_subscription(request: web.Request, subscription_id, api_version, skip_token=None) -> web.Response:
    """List Accounts in a subscription

    List Accounts in Subscription

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param api_version: The api version to use.
    :type api_version: str
    :param skip_token: Continuation token
    :type skip_token: str

    """
    return web.Response(status=200)


async def accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, account_update_parameters) -> web.Response:
    """Patch a given account

    Patch an account

    :param subscription_id: The subscription identifier
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param account_name: The name of the share account.
    :type account_name: str
    :param api_version: The api version to use.
    :type api_version: str
    :param account_update_parameters: The account update parameters.
    :type account_update_parameters: dict | bytes

    """
    account_update_parameters = AccountUpdateParameters.from_dict(account_update_parameters)
    return web.Response(status=200)
