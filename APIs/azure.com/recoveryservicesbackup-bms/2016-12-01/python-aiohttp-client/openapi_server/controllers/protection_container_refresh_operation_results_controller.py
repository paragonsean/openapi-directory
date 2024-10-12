from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def protection_container_refresh_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, operation_id) -> web.Response:
    """protection_container_refresh_operation_results_get

    Provides the result of the refresh operation triggered by the BeginRefresh operation.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the container.
    :type fabric_name: str
    :param operation_id: Operation ID associated with the operation whose result needs to be fetched.
    :type operation_id: str

    """
    return web.Response(status=200)
