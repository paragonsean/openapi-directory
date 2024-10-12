from typing import List, Dict
from aiohttp import web

from openapi_server.models.protected_item_resource import ProtectedItemResource
from openapi_server import util


async def protected_items_create_or_update(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, parameters) -> web.Response:
    """protected_items_create_or_update

    Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an  asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backup item.
    :type fabric_name: str
    :param container_name: Container name associated with the backup item.
    :type container_name: str
    :param protected_item_name: Item name to be backed up.
    :type protected_item_name: str
    :param parameters: resource backed up item
    :type parameters: dict | bytes

    """
    parameters = ProtectedItemResource.from_dict(parameters)
    return web.Response(status=200)


async def protected_items_delete(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name) -> web.Response:
    """protected_items_delete

    Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the  request, call the GetItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up item.
    :type fabric_name: str
    :param container_name: Container name associated with the backed up item.
    :type container_name: str
    :param protected_item_name: Backed up item to be deleted.
    :type protected_item_name: str

    """
    return web.Response(status=200)


async def protected_items_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, filter=None) -> web.Response:
    """protected_items_get

    Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,  call the GetItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up item.
    :type fabric_name: str
    :param container_name: Container name associated with the backed up item.
    :type container_name: str
    :param protected_item_name: Backed up item name whose details are to be fetched.
    :type protected_item_name: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)
