from typing import List, Dict
from aiohttp import web

from openapi_server.models.remote_rendering_account import RemoteRenderingAccount
from openapi_server.models.remote_rendering_account_page import RemoteRenderingAccountPage
from openapi_server.models.remote_rendering_accounts_list_by_subscription_default_response import RemoteRenderingAccountsListBySubscriptionDefaultResponse
from openapi_server import util


async def remote_rendering_accounts_create(request: web.Request, subscription_id, resource_group_name, account_name, api_version, remote_rendering_account) -> web.Response:
    """remote_rendering_accounts_create

    Creating or Updating a Remote Rendering Account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param remote_rendering_account: Remote Rendering Account parameter.
    :type remote_rendering_account: dict | bytes

    """
    remote_rendering_account = RemoteRenderingAccount.from_dict(remote_rendering_account)
    return web.Response(status=200)


async def remote_rendering_accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """remote_rendering_accounts_delete

    Delete a Remote Rendering Account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def remote_rendering_accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """remote_rendering_accounts_get

    Retrieve a Remote Rendering Account.

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def remote_rendering_accounts_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """remote_rendering_accounts_list_by_resource_group

    List Resources by Resource Group

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def remote_rendering_accounts_list_by_subscription(request: web.Request, subscription_id, api_version) -> web.Response:
    """remote_rendering_accounts_list_by_subscription

    List Remote Rendering Accounts by Subscription

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def remote_rendering_accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, remote_rendering_account) -> web.Response:
    """remote_rendering_accounts_update

    Updating a Remote Rendering Account

    :param subscription_id: Azure subscription ID.
    :type subscription_id: str
    :param resource_group_name: Name of an Azure resource group.
    :type resource_group_name: str
    :param account_name: Name of an Mixed Reality Account.
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param remote_rendering_account: Remote Rendering Account parameter.
    :type remote_rendering_account: dict | bytes

    """
    remote_rendering_account = RemoteRenderingAccount.from_dict(remote_rendering_account)
    return web.Response(status=200)
