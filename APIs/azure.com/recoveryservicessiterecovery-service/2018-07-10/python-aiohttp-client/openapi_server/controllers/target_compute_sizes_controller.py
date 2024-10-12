from typing import List, Dict
from aiohttp import web

from openapi_server.models.target_compute_size_collection import TargetComputeSizeCollection
from openapi_server import util


async def target_compute_sizes_list_by_replication_protected_items(request: web.Request, api_version, resource_name, resource_group_name, subscription_id, fabric_name, protection_container_name, replicated_protected_item_name) -> web.Response:
    """Gets the list of target compute sizes for the replication protected item.

    Lists the available target compute sizes for a replication protected item.

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
    :param protection_container_name: protection container name.
    :type protection_container_name: str
    :param replicated_protected_item_name: Replication protected item name.
    :type replicated_protected_item_name: str

    """
    return web.Response(status=200)
