from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def asynchronous_operations_bulk_status_v1_get_operations_count_by_bulk_id_and_status_get(request: web.Request, bulk_uuid, status) -> web.Response:
    """bulk/{bulkUuid}/operation-status/{status}

    Get operations count by bulk uuid and status.

    :param bulk_uuid: 
    :type bulk_uuid: str
    :param status: 
    :type status: int

    """
    return web.Response(status=200)
