from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_bulk_message_result import CreateBulkMessageResult
from openapi_server.models.create_message import CreateMessage
from openapi_server.models.create_message_result import CreateMessageResult
from openapi_server.models.message import Message
from openapi_server.models.messages_result import MessagesResult
from openapi_server.models.search import Search
from openapi_server import util


async def messages_create(request: web.Request, log_id, body=None) -> web.Response:
    """Create a new message.

    Required permission: &#x60;messages_write&#x60;

    :param log_id: The ID of the log which should contain the new message.
    :type log_id: str
    :param body: The message object to create.
    :type body: dict | bytes

    """
    body = CreateMessage.from_dict(body)
    return web.Response(status=200)


async def messages_create_bulk(request: web.Request, log_id, body=None) -> web.Response:
    """Create one or more new messages.

    Required permission: &#x60;messages_write&#x60;

    :param log_id: The ID of the log which should contain the new messages.
    :type log_id: str
    :param body: The messages to create.
    :type body: list | bytes

    """
    body = [CreateMessage.from_dict(d) for d in body]
    return web.Response(status=200)


async def messages_delete(request: web.Request, id, log_id) -> web.Response:
    """Delete a message by its ID.

    Required permission: &#x60;messages_delete&#x60;

    :param id: The ID of the message to delete.
    :type id: str
    :param log_id: The ID of the log containing the message.
    :type log_id: str

    """
    return web.Response(status=200)


async def messages_delete_all(request: web.Request, log_id, body=None) -> web.Response:
    """Deletes a list of messages by logid and query.

    Required permission: &#x60;messages_delete&#x60;

    :param log_id: The ID of the log containing the message.
    :type log_id: str
    :param body: A search object containing query, time filters etc.
    :type body: dict | bytes

    """
    body = Search.from_dict(body)
    return web.Response(status=200)


async def messages_fix(request: web.Request, id, log_id, mark_all_as_fixed=None) -> web.Response:
    """Fix a message by its ID.

    Required permission: &#x60;messages_write&#x60;

    :param id: The ID of the message to fix.
    :type id: str
    :param log_id: The ID of the log containing the message.
    :type log_id: str
    :param mark_all_as_fixed: If set to true, all instances of the log message are set to fixed.
    :type mark_all_as_fixed: bool

    """
    return web.Response(status=200)


async def messages_fix_all(request: web.Request, log_id, body=None) -> web.Response:
    """Mark a list of messages as fixed by logid and query.

    Required permission: &#x60;messages_write&#x60;

    :param log_id: The ID of the log containing the messages.
    :type log_id: str
    :param body: A search object containing query, time filters etc.
    :type body: dict | bytes

    """
    body = Search.from_dict(body)
    return web.Response(status=200)


async def messages_get(request: web.Request, id, log_id) -> web.Response:
    """Fetch a message by its ID.

    Required permission: &#x60;messages_read&#x60;

    :param id: The ID of the message to fetch.
    :type id: str
    :param log_id: The ID of the log containing the message.
    :type log_id: str

    """
    return web.Response(status=200)


async def messages_get_all(request: web.Request, log_id, page_index=None, page_size=None, query=None, _from=None, to=None, include_headers=None) -> web.Response:
    """Fetch messages from a log.

    Required permission: &#x60;messages_read&#x60;

    :param log_id: The ID of the log containing the messages.
    :type log_id: str
    :param page_index: The page number of the result.
    :type page_index: int
    :param page_size: The number of messages to load (max 100) or 15 if not set.
    :type page_size: int
    :param query: A full-text or Lucene query to limit the messages by.
    :type query: str
    :param _from: A start date and time to search from (not included).
    :type _from: str
    :param to: An end date and time to search to (not included).
    :type to: str
    :param include_headers: Include headers like server variables and cookies in the result (slower).
    :type include_headers: bool

    """
    _from = util.deserialize_datetime(_from)
    to = util.deserialize_datetime(to)
    return web.Response(status=200)


async def messages_hide(request: web.Request, id, log_id) -> web.Response:
    """Hide a message by its ID.

    Required permission: &#x60;messages_write&#x60;

    :param id: The ID of the message to hide.
    :type id: str
    :param log_id: The ID of the log containing the message.
    :type log_id: str

    """
    return web.Response(status=200)
