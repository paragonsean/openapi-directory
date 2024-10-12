from typing import List, Dict
from aiohttp import web

from openapi_server.models.asynchronous_operations_data_bulk_operations_status_interface import AsynchronousOperationsDataBulkOperationsStatusInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def asynchronous_operations_bulk_status_v1_get_bulk_short_status_get(request: web.Request, bulk_uuid) -> web.Response:
    """bulk/{bulkUuid}/status

    Get Bulk summary data with list of operations items short data.

    :param bulk_uuid: 
    :type bulk_uuid: str

    """
    return web.Response(status=200)
