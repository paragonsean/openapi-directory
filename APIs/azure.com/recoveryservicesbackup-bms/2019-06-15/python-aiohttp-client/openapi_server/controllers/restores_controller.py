from typing import List, Dict
from aiohttp import web

from openapi_server.models.restore_request_resource import RestoreRequestResource
from openapi_server import util


async def restores_trigger(request: web.Request, api_version, vault_name, resource_group_name, subscription_id, fabric_name, container_name, protected_item_name, recovery_point_id, parameters) -> web.Response:
    """restores_trigger

    Restores the specified backed up data. This is an asynchronous operation. To know the status of this API call, use  GetProtectedItemOperationResult API.

    :param api_version: Client Api Version.
    :type api_version: str
    :param vault_name: The name of the recovery services vault.
    :type vault_name: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param fabric_name: Fabric name associated with the backed up items.
    :type fabric_name: str
    :param container_name: Container name associated with the backed up items.
    :type container_name: str
    :param protected_item_name: Backed up item to be restored.
    :type protected_item_name: str
    :param recovery_point_id: Recovery point ID which represents the backed up data to be restored.
    :type recovery_point_id: str
    :param parameters: resource restore request
    :type parameters: dict | bytes

    """
    parameters = RestoreRequestResource.from_dict(parameters)
    return web.Response(status=200)
