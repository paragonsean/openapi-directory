from typing import List, Dict
from aiohttp import web

from openapi_server.models.background_task_out import BackgroundTaskOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_background_task_out import ListResponseBackgroundTaskOut
from openapi_server.models.ordering import Ordering
from openapi_server import util


async def get_background_task_api_v1_background_task_task_id_get(request: web.Request, task_id, idempotency_key=None) -> web.Response:
    """Get Background Task

    Get a background task by ID.

    :param task_id: 
    :type task_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_background_tasks_api_v1_background_task_get(request: web.Request, iterator=None, limit=None, order=None, idempotency_key=None) -> web.Response:
    """List Background Tasks

    List background tasks executed in the past 90 days.

    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param order: 
    :type order: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    order = .from_dict(order)
    return web.Response(status=200)
