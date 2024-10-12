from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_key import ApiKey
from openapi_server.models.api_key_collection import ApiKeyCollection
from openapi_server.models.transaction_node import TransactionNode
from openapi_server.models.transaction_node_collection import TransactionNodeCollection
from openapi_server.models.transaction_node_update import TransactionNodeUpdate
from openapi_server import util


async def transaction_nodes_create(request: web.Request, blockchain_member_name, transaction_node_name, api_version, subscription_id, resource_group_name, transaction_node=None) -> web.Response:
    """transaction_nodes_create

    Create or update the transaction node.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param transaction_node_name: Transaction node name.
    :type transaction_node_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param transaction_node: Payload to create the transaction node.
    :type transaction_node: dict | bytes

    """
    transaction_node = TransactionNode.from_dict(transaction_node)
    return web.Response(status=200)


async def transaction_nodes_delete(request: web.Request, blockchain_member_name, transaction_node_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """transaction_nodes_delete

    Delete the transaction node.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param transaction_node_name: Transaction node name.
    :type transaction_node_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def transaction_nodes_get(request: web.Request, blockchain_member_name, transaction_node_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """transaction_nodes_get

    Get the details of the transaction node.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param transaction_node_name: Transaction node name.
    :type transaction_node_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def transaction_nodes_list(request: web.Request, blockchain_member_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """transaction_nodes_list

    Lists the transaction nodes for a blockchain member.

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


async def transaction_nodes_list_api_keys(request: web.Request, blockchain_member_name, transaction_node_name, api_version, subscription_id, resource_group_name) -> web.Response:
    """transaction_nodes_list_api_keys

    List the API keys for the transaction node.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param transaction_node_name: Transaction node name.
    :type transaction_node_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str

    """
    return web.Response(status=200)


async def transaction_nodes_list_regenerate_api_keys(request: web.Request, blockchain_member_name, transaction_node_name, api_version, subscription_id, resource_group_name, api_key=None) -> web.Response:
    """transaction_nodes_list_regenerate_api_keys

    Regenerate the API keys for the blockchain member.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param transaction_node_name: Transaction node name.
    :type transaction_node_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param api_key: api key to be regenerated
    :type api_key: dict | bytes

    """
    api_key = ApiKey.from_dict(api_key)
    return web.Response(status=200)


async def transaction_nodes_update(request: web.Request, blockchain_member_name, transaction_node_name, api_version, subscription_id, resource_group_name, transaction_node=None) -> web.Response:
    """transaction_nodes_update

    Update the transaction node.

    :param blockchain_member_name: Blockchain member name.
    :type blockchain_member_name: str
    :param transaction_node_name: Transaction node name.
    :type transaction_node_name: str
    :param api_version: Client API Version.
    :type api_version: str
    :param subscription_id: Gets the subscription Id which uniquely identifies the Microsoft Azure subscription. The subscription ID is part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :type resource_group_name: str
    :param transaction_node: Payload to create the transaction node.
    :type transaction_node: dict | bytes

    """
    transaction_node = TransactionNodeUpdate.from_dict(transaction_node)
    return web.Response(status=200)
