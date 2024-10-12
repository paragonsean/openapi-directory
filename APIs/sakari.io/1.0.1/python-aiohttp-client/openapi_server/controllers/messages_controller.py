from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_response import MessageResponse
from openapi_server.models.messages_response import MessagesResponse
from openapi_server.models.send_messages_request import SendMessagesRequest
from openapi_server.models.send_messages_response import SendMessagesResponse
from openapi_server import util


async def messages_fetch(request: web.Request, account_id, message_id) -> web.Response:
    """Fetch message by id

    Returns a single messag

    :param account_id: Account to apply operations to
    :type account_id: str
    :param message_id: ID of message to return
    :type message_id: str

    """
    return web.Response(status=200)


async def messages_fetch_all(request: web.Request, account_id, offset=None, limit=None, contact_id=None, conversation_id=None) -> web.Response:
    """Fetch messages

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param offset: Results to skip when paginating through a result set
    :type offset: int
    :param limit: Maximum number of results to return
    :type limit: int
    :param contact_id: ID of contact
    :type contact_id: str
    :param conversation_id: ID of conversation
    :type conversation_id: str

    """
    return web.Response(status=200)


async def messages_send(request: web.Request, account_id, body=None) -> web.Response:
    """Send Messages

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SendMessagesRequest.from_dict(body)
    return web.Response(status=200)
