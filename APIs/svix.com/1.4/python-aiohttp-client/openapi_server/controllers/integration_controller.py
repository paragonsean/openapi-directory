from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.integration_in import IntegrationIn
from openapi_server.models.integration_key_out import IntegrationKeyOut
from openapi_server.models.integration_out import IntegrationOut
from openapi_server.models.integration_update import IntegrationUpdate
from openapi_server.models.list_response_integration_out import ListResponseIntegrationOut
from openapi_server import util


async def create_integration_api_v1_app_app_id_integration_post(request: web.Request, app_id, body, idempotency_key=None) -> web.Response:
    """Create Integration

    Create an integration.

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = IntegrationIn.from_dict(body)
    return web.Response(status=200)


async def delete_integration_api_v1_app_app_id_integration_integ_id_delete(request: web.Request, integ_id, app_id, idempotency_key=None) -> web.Response:
    """Delete Integration

    Delete an integration and revoke it&#39;s key.

    :param integ_id: 
    :type integ_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_integration_api_v1_app_app_id_integration_integ_id_get(request: web.Request, integ_id, app_id, idempotency_key=None) -> web.Response:
    """Get Integration

    Get an integration.

    :param integ_id: 
    :type integ_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_integration_key_api_v1_app_app_id_integration_integ_id_key_get(request: web.Request, integ_id, app_id, idempotency_key=None) -> web.Response:
    """Get Integration Key

    Get an integration&#39;s key.

    :param integ_id: 
    :type integ_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_integrations_api_v1_app_app_id_integration_get(request: web.Request, app_id, iterator=None, limit=None, idempotency_key=None) -> web.Response:
    """List Integrations

    List the application&#39;s integrations.

    :param app_id: 
    :type app_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def rotate_integration_key_api_v1_app_app_id_integration_integ_id_key_rotate_post(request: web.Request, integ_id, app_id, idempotency_key=None) -> web.Response:
    """Rotate Integration Key

    Rotate the integration&#39;s key. The previous key will be immediately revoked.

    :param integ_id: 
    :type integ_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def update_integration_api_v1_app_app_id_integration_integ_id_put(request: web.Request, integ_id, app_id, body, idempotency_key=None) -> web.Response:
    """Update Integration

    Update an integration.

    :param integ_id: 
    :type integ_id: str
    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = IntegrationUpdate.from_dict(body)
    return web.Response(status=200)
