from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_status import OperationStatus
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server import util


async def operation_status_get(request: web.Request, subscription_id, resource_group_name, api_version, location_name, workflow_id, operation_id) -> web.Response:
    """operation_status_get

    Get Operation status

    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group. The name is case insensitive.
    :type resource_group_name: str
    :param api_version: The API version to use for this operation.
    :type api_version: str
    :param location_name: The desired region to obtain information from.
    :type location_name: str
    :param workflow_id: workflow Id
    :type workflow_id: str
    :param operation_id: operation Id
    :type operation_id: str

    """
    return web.Response(status=200)
