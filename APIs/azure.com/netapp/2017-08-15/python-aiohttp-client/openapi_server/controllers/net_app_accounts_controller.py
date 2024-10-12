from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.net_app_account import NetAppAccount
from openapi_server.models.net_app_account_list import NetAppAccountList
from openapi_server.models.net_app_account_patch import NetAppAccountPatch
from openapi_server import util


async def accounts_create_or_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, body) -> web.Response:
    """accounts_create_or_update

    Create or update a NetApp account

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: NetApp Account object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = NetAppAccount.from_dict(body)
    return web.Response(status=200)


async def accounts_delete(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """accounts_delete

    Delete a NetApp account

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_get(request: web.Request, subscription_id, resource_group_name, account_name, api_version) -> web.Response:
    """accounts_get

    Get the NetApp account

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_list(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """accounts_list

    Lists all NetApp accounts in the resource group

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def accounts_update(request: web.Request, subscription_id, resource_group_name, account_name, api_version, body) -> web.Response:
    """accounts_update

    Patch a NetApp account

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param account_name: The name of the NetApp account
    :type account_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param body: NetApp Account object supplied in the body of the operation.
    :type body: dict | bytes

    """
    body = NetAppAccountPatch.from_dict(body)
    return web.Response(status=200)
