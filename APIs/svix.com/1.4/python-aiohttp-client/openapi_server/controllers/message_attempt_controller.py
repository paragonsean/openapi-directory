from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_endpoint_message_out import ListResponseEndpointMessageOut
from openapi_server.models.list_response_message_attempt_endpoint_out import ListResponseMessageAttemptEndpointOut
from openapi_server.models.list_response_message_attempt_out import ListResponseMessageAttemptOut
from openapi_server.models.list_response_message_endpoint_out import ListResponseMessageEndpointOut
from openapi_server.models.message_attempt_out import MessageAttemptOut
from openapi_server.models.message_status import MessageStatus
from openapi_server.models.status_code_class import StatusCodeClass
from openapi_server import util


async def expunge_attempt_content_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_content_delete(request: web.Request, attempt_id, msg_id, app_id, idempotency_key=None) -> web.Response:
    """Delete attempt response body

    Deletes the given attempt&#39;s response body. Useful when an endpoint accidentally returned sensitive content.

    :param attempt_id: 
    :type attempt_id: str
    :param msg_id: 
    :type msg_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_attempt_api_v1_app_app_id_msg_msg_id_attempt_attempt_id_get(request: web.Request, attempt_id, msg_id, app_id, idempotency_key=None) -> web.Response:
    """Get Attempt

    &#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

    :param attempt_id: 
    :type attempt_id: str
    :param msg_id: 
    :type msg_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_attempted_destinations_api_v1_app_app_id_msg_msg_id_endpoint_get(request: web.Request, msg_id, app_id, iterator=None, limit=None, idempotency_key=None) -> web.Response:
    """List Attempted Destinations

    &#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

    :param msg_id: 
    :type msg_id: str
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


async def list_attempted_messages_api_v1_app_app_id_endpoint_endpoint_id_msg_get(request: web.Request, endpoint_id, app_id, iterator=None, limit=None, channel=None, status=None, before=None, after=None, idempotency_key=None) -> web.Response:
    """List Attempted Messages

    List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

    :param endpoint_id: 
    :type endpoint_id: str
    :param app_id: 
    :type app_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param channel: 
    :type channel: str
    :param status: 
    :type status: dict | bytes
    :param before: 
    :type before: str
    :param after: 
    :type after: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    status = .from_dict(status)
    before = util.deserialize_datetime(before)
    after = util.deserialize_datetime(after)
    return web.Response(status=200)


async def list_attempts_api_v1_app_app_id_msg_msg_id_attempt_get(request: web.Request, app_id, msg_id, iterator=None, limit=None, endpoint_id=None, event_types=None, channel=None, status=None, before=None, after=None, idempotency_key=None) -> web.Response:
    """List Attempts

    Deprecated: Please use \&quot;List Attempts by Endpoint\&quot; and \&quot;List Attempts by Msg\&quot; instead.  &#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

    :param app_id: 
    :type app_id: str
    :param msg_id: 
    :type msg_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param endpoint_id: 
    :type endpoint_id: str
    :param event_types: 
    :type event_types: List[str]
    :param channel: 
    :type channel: str
    :param status: 
    :type status: dict | bytes
    :param before: 
    :type before: str
    :param after: 
    :type after: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    status = .from_dict(status)
    before = util.deserialize_datetime(before)
    after = util.deserialize_datetime(after)
    return web.Response(status=200)


async def list_attempts_by_endpoint_api_v1_app_app_id_attempt_endpoint_endpoint_id_get(request: web.Request, app_id, endpoint_id, iterator=None, limit=None, status=None, status_code_class=None, event_types=None, channel=None, before=None, after=None, idempotency_key=None) -> web.Response:
    """List Attempts By Endpoint

    List attempts by endpoint id

    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param status: 
    :type status: dict | bytes
    :param status_code_class: 
    :type status_code_class: dict | bytes
    :param event_types: 
    :type event_types: List[str]
    :param channel: 
    :type channel: str
    :param before: 
    :type before: str
    :param after: 
    :type after: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    status = .from_dict(status)
    status_code_class = .from_dict(status_code_class)
    before = util.deserialize_datetime(before)
    after = util.deserialize_datetime(after)
    return web.Response(status=200)


async def list_attempts_by_msg_api_v1_app_app_id_attempt_msg_msg_id_get(request: web.Request, app_id, msg_id, endpoint_id=None, iterator=None, limit=None, status=None, status_code_class=None, event_types=None, channel=None, before=None, after=None, idempotency_key=None) -> web.Response:
    """List Attempts By Msg

    List attempts by message id

    :param app_id: 
    :type app_id: str
    :param msg_id: 
    :type msg_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param status: 
    :type status: dict | bytes
    :param status_code_class: 
    :type status_code_class: dict | bytes
    :param event_types: 
    :type event_types: List[str]
    :param channel: 
    :type channel: str
    :param before: 
    :type before: str
    :param after: 
    :type after: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    status = .from_dict(status)
    status_code_class = .from_dict(status_code_class)
    before = util.deserialize_datetime(before)
    after = util.deserialize_datetime(after)
    return web.Response(status=200)


async def list_attempts_for_endpoint_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_attempt_get(request: web.Request, msg_id, app_id, endpoint_id, iterator=None, limit=None, event_types=None, channel=None, status=None, before=None, after=None, idempotency_key=None) -> web.Response:
    """List Attempts For Endpoint

    DEPRECATED: please use list_attempts with endpoint_id as a query parameter instead.  List the message attempts for a particular endpoint.  Returning the endpoint.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

    :param msg_id: 
    :type msg_id: str
    :param app_id: 
    :type app_id: str
    :param endpoint_id: 
    :type endpoint_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
    :param event_types: 
    :type event_types: List[str]
    :param channel: 
    :type channel: str
    :param status: 
    :type status: dict | bytes
    :param before: 
    :type before: str
    :param after: 
    :type after: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    status = .from_dict(status)
    before = util.deserialize_datetime(before)
    after = util.deserialize_datetime(after)
    return web.Response(status=200)


async def resend_webhook_api_v1_app_app_id_msg_msg_id_endpoint_endpoint_id_resend_post(request: web.Request, endpoint_id, msg_id, app_id, idempotency_key=None) -> web.Response:
    """Resend Webhook

    Resend a message to the specified endpoint.

    :param endpoint_id: 
    :type endpoint_id: str
    :param msg_id: 
    :type msg_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)
