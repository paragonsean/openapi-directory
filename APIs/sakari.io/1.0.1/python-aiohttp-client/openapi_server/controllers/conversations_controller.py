from typing import List, Dict
from aiohttp import web

from openapi_server.models.conversation_response import ConversationResponse
from openapi_server.models.conversations_response import ConversationsResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def conversations_close(request: web.Request, account_id, conversation_id) -> web.Response:
    """Closes a conversation

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param conversation_id: ID of conversation
    :type conversation_id: str

    """
    return web.Response(status=200)


async def conversations_fetch(request: web.Request, account_id, conversation_id) -> web.Response:
    """Fetch conversation by ID

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param conversation_id: ID of template to return
    :type conversation_id: str

    """
    return web.Response(status=200)


async def conversations_fetch_all(request: web.Request, account_id, offset=None, limit=None) -> web.Response:
    """Fetch conversations

    

    :param account_id: Account to apply operations to
    :type account_id: str
    :param offset: Results to skip when paginating through a result set
    :type offset: int
    :param limit: Maximum number of results to return
    :type limit: int

    """
    return web.Response(status=200)
