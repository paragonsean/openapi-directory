from typing import List, Dict
from aiohttp import web

from openapi_server.models.protection_container_resource import ProtectionContainerResource
from openapi_server import util


async def protection_container_operation_results_get(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, operation_id) -> web.Response:
    """protection_container_operation_results_get

    Gets the result of any operation on the container.

    :param api_version: Client API version.
    :type api_version: str
    :param vault_name: The name of the Recovery Services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group associated with the Recovery Services vault.
    :type resource_group_name: str
    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param fabric_name: The fabric name associated with the container.
    :type fabric_name: str
    :param container_name: The container name used for this GET operation.
    :type container_name: str
    :param operation_id: The operation ID used for this GET operation.
    :type operation_id: str

    """
    return web.Response(status=200)
