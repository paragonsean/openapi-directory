from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.http_error_out import HttpErrorOut
from openapi_server.models.list_response_message_out import ListResponseMessageOut
from openapi_server.models.message_in import MessageIn
from openapi_server.models.message_out import MessageOut
from openapi_server import util


async def create_message_api_v1_app_app_id_msg_post(request: web.Request, app_id, body, with_content=None, idempotency_key=None) -> web.Response:
    """Create Message

    Creates a new message and dispatches it to all of the application&#39;s endpoints.  The &#x60;eventId&#x60; is an optional custom unique ID. It&#39;s verified to be unique only up to a day, after that no verification will be made. If a message with the same &#x60;eventId&#x60; already exists for any application in your environment, a 409 conflict error will be returned.  The &#x60;eventType&#x60; indicates the type and schema of the event. All messages of a certain &#x60;eventType&#x60; are expected to have the same schema. Endpoints can choose to only listen to specific event types. Messages can also have &#x60;channels&#x60;, which similar to event types let endpoints filter by them. Unlike event types, messages can have multiple channels, and channels don&#39;t imply a specific message content or schema.  The &#x60;payload&#x60; property is the webhook&#39;s body (the actual webhook message). Svix supports payload sizes of up to ~350kb, though it&#39;s generally a good idea to keep webhook payloads small, probably no larger than 40kb.  The optional &#x60;application&#x60; property will be used to create an application if the application referenced in the path does not exist. If it does then this property is ignored.

    :param app_id: 
    :type app_id: str
    :param body: 
    :type body: dict | bytes
    :param with_content: 
    :type with_content: bool
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    body = MessageIn.from_dict(body)
    return web.Response(status=200)


async def expunge_message_payload_api_v1_app_app_id_msg_msg_id_content_delete(request: web.Request, msg_id, app_id, idempotency_key=None) -> web.Response:
    """Delete message payload

    Delete the given message&#39;s payload. Useful in cases when a message was accidentally sent with sensitive content.  The message can&#39;t be replayed or resent once its payload has been deleted or expired.

    :param msg_id: 
    :type msg_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def get_message_api_v1_app_app_id_msg_msg_id_get(request: web.Request, msg_id, app_id, idempotency_key=None) -> web.Response:
    """Get Message

    Get a message by its ID or eventID.

    :param msg_id: 
    :type msg_id: str
    :param app_id: 
    :type app_id: str
    :param idempotency_key: The request&#39;s idempotency key
    :type idempotency_key: str

    """
    return web.Response(status=200)


async def list_messages_api_v1_app_app_id_msg_get(request: web.Request, app_id, iterator=None, limit=None, event_types=None, channel=None, before=None, after=None, idempotency_key=None) -> web.Response:
    """List Messages

    List all of the application&#39;s messages.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed. The &#x60;after&#x60; parameter lets you filter all items created after a certain date and is ignored if an iterator is passed. &#x60;before&#x60; and &#x60;after&#x60; cannot be used simultaneously.

    :param app_id: 
    :type app_id: str
    :param iterator: 
    :type iterator: str
    :param limit: 
    :type limit: int
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
    before = util.deserialize_datetime(before)
    after = util.deserialize_datetime(after)
    return web.Response(status=200)
