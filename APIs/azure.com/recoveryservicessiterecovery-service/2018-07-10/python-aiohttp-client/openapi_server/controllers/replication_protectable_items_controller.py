from typing import List, Dict
from aiohttp import web

from openapi_server.models.protectable_item import ProtectableItem
from openapi_server.models.protectable_item_collection import ProtectableItemCollection
from openapi_server import util


async def replication_protectable_items_get(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, protectable_item_name) -> web.Response:
    """Gets the details of a protectable item.

    The operation to get the details of a protectable item.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param protectable_item_name: Protectable item name.
    :type protectable_item_name: str

    """
    return web.Response(status=200)


async def replication_protectable_items_list_by_replication_protection_containers(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, filter=None) -> web.Response:
    """Gets the list of protectable items.

    Lists the protectable items in a protection container.

    :param api_version: Client Api Version.
    :type api_version: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name.
    :type fabric_name: str
    :param protection_container_name: Protection container name.
    :type protection_container_name: str
    :param filter: OData filter options.
    :type filter: str

    """
    return web.Response(status=200)
