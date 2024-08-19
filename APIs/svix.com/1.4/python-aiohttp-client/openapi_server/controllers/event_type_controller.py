from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_type_in import EventTypeIn
from openapi_server.models.event_type_out import EventTypeOut
from openapi_server.models.event_type_update import EventTypeUpdate
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_event_type_out import ListResponseEventTypeOut
from openapi_server import util


async def create_event_type_api_v1_event_type_post(request: web.Request, body, idempotency_key=None) -> web.Response:
    """Create Event Type

    Create new or unarchive existing event type.  Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it. Endpoints filtering on the event type before archival will continue to filter on it. This operation does not preserve the description and schemas.

    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EventTypeIn.from_dict(body)
    return web.Response(status=200)


async def delete_event_type_api_v1_event_type_event_type_name_delete(request: web.Request, event_type_name, expunge=None, idempotency_key=None) -> web.Response:
    """Archive Event Type

    Archive an event type.  Endpoints already configured to filter on an event type will continue to do so after archival. However, new messages can not be sent with it and endpoints can not filter on it. An event type can be unarchived with the [create operation](#operation/create_event_type_api_v1_event_type__post).  If &#x60;expunge&#x3D;true&#x60; is set then the event type is deleted instead of archived. This can only be used in development environments.

    :param event_type_name: 
    :type event_type_name: str
    :param expunge: 
    :type expunge: bool
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_event_type_api_v1_event_type_event_type_name_get(request: web.Request, event_type_name, idempotency_key=None) -> web.Response:
    """Get Event Type

    Get an event type.

    :param event_type_name: 
    :type event_type_name: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_event_types_api_v1_event_type_get(request: web.Request, iterator=None, limit=None, with_content=None, include_archived=None, idempotency_key=None) -> web.Response:
    """List Event Types

    Return the list of event types.

    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param with_content: 
    :type with_content: bool
    :param include_archived: 
    :type include_archived: bool
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def update_event_type_api_v1_event_type_event_type_name_put(request: web.Request, event_type_name, body, idempotency_key=None) -> web.Response:
    """Update Event Type

    Update an event type.

    :param event_type_name: 
    :type event_type_name: str
    :param body: 
    :type body: dict | bytes
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = EventTypeUpdate.from_dict(body)
    return web.Response(status=200)
