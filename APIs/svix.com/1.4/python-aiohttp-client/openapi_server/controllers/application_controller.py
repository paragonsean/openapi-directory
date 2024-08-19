from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_in import ApplicationIn
from openapi_server.models.application_out import ApplicationOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_application_out import ListResponseApplicationOut
from openapi_server.models.ordering import Ordering
from openapi_server import util


async def create_application_api_v1_app_post(request: web.Request, body, get_if_exists=None, idempotency_key=None) -> web.Response:
    """Create Application

    Create a new application.

    :param body: 
    :type body: dict | bytes
    :param get_if_exists: Get an existing application, or create a new one if doesn&#39;t exist. It&#39;s two separate functions in the libs.
    :type get_if_exists: bool
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = ApplicationIn.from_dict(body)
    return web.Response(status=200)


async def delete_application_api_v1_app_app_id_delete(request: web.Request, app_id, idempotency_key=None) -> web.Response:
    """Delete Application

    Delete an application.

    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_application_api_v1_app_app_id_get(request: web.Request, app_id, idempotency_key=None) -> web.Response:
    """Get Application

    Get an application.

    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_applications_api_v1_app_get(request: web.Request, iterator=None, limit=None, order=None, idempotency_key=None) -> web.Response:
    """List Applications

    List of all the organization&#39;s applications.

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


async def update_application_api_v1_app_app_id_put(request: web.Request, app_id, body, idempotency_key=None) -> web.Response:
    """Update Application

    Update an application.

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = ApplicationIn.from_dict(body)
    return web.Response(status=200)
