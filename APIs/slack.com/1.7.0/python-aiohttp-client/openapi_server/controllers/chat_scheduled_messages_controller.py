from typing import List, Dict
from aiohttp import web

from openapi_server.models.chat_scheduled_messages_list_error_schema import ChatScheduledMessagesListErrorSchema
from openapi_server.models.chat_scheduled_messages_list_schema import ChatScheduledMessagesListSchema
from openapi_server import util


async def chat_scheduled_messages_list(request: web.Request, token=None, channel=None, latest=None, oldest=None, limit=None, cursor=None) -> web.Response:
    """chat_scheduled_messages_list

    Returns a list of scheduled messages.

    :param token: Authentication token. Requires scope: &#x60;none&#x60;
    :type token: str
    :param channel: The channel of the scheduled messages
    :type channel: str
    :param latest: A UNIX timestamp of the latest value in the time range
    :type latest: 
    :param oldest: A UNIX timestamp of the oldest value in the time range
    :type oldest: 
    :param limit: Maximum number of original entries to return.
    :type limit: int
    :param cursor: For pagination purposes, this is the &#x60;cursor&#x60; value returned from a previous call to &#x60;chat.scheduledmessages.list&#x60; indicating where you want to start this call from.
    :type cursor: str

    """
    return web.Response(status=200)
