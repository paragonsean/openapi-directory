from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation_entity_list_result import OperationEntityListResult
from openapi_server.models.storage_sync_error import StorageSyncError
from openapi_server import util


async def operations_list_0(request: web.Request, api_version) -> web.Response:
    """operations_list_0

    Lists all of the available Storage Sync Rest API operations.

    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
