from typing import List, Dict
from aiohttp import web

from openapi_server.models.protected_item_resource import ProtectedItemResource
from openapi_server import util


async def protected_item_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, operation_id) -> web.Response:
    """protected_item_operation_results_get

    Fetches the result of any operation on the backup item.

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
    :param protected_item_name: Backup item name whose details are to be fetched.
    :type protected_item_name: str
    :param operation_id: OperationID which represents the operation whose result needs to be fetched.
    :type operation_id: str

    """
    return web.Response(status=200)
