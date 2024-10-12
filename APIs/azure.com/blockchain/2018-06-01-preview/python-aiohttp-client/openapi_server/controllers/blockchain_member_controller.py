from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_collection import ApiKeyCollection
from openapi_server.models.blockchain_member import BlockchainMember
from openapi_server.models.blockchain_member_collection import BlockchainMemberCollection
from openapi_server.models.blockchain_member_update import BlockchainMemberUpdate
from openapi_server.models.consortium_member_collection import ConsortiumMemberCollection
from openapi_server import util


async def blockchain_members_create(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name, blockchain_member=None) -> web.Response:
    """blockchain_members_create

    Create a blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param blockchain_member: Payload to create a blockchain member.
    :type blockchain_member: dict | bytes

    """
    blockchain_member = BlockchainMember.from_dict(blockchain_member)
    return web.Response(status=200)


async def blockchain_members_delete(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """blockchain_members_delete

    Delete a blockchain member.

    :param blockchain_member_name: Blockchain member name
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def blockchain_members_get(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """blockchain_members_get

    Get details about a blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def blockchain_members_list(request: web.Request, api_version, subscription_id, resource_group_name) -> web.Response:
    """blockchain_members_list

    Lists the blockchain members for a resource group.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def blockchain_members_list_all(request: web.Request, api_version, subscription_id) -> web.Response:
    """blockchain_members_list_all

    Lists the blockchain members for a subscription.

    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def blockchain_members_list_api_keys(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """blockchain_members_list_api_keys

    Lists the API keys for a blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def blockchain_members_list_consortium_members(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """blockchain_members_list_consortium_members

    Lists the consortium members for a blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def blockchain_members_list_regenerate_api_keys(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name, api_key=None) -> web.Response:
    """blockchain_members_list_regenerate_api_keys

    Regenerate the API keys for a blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param api_key: api key to be regenerate
    :type api_key: dict | bytes

    """
    api_key = ApiKey.from_dict(api_key)
    return web.Response(status=200)


async def blockchain_members_update(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name, blockchain_member=None) -> web.Response:
    """blockchain_members_update

    Update a blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param blockchain_member: Payload to update the blockchain member.
    :type blockchain_member: dict | bytes

    """
    blockchain_member = BlockchainMemberUpdate.from_dict(blockchain_member)
    return web.Response(status=200)
