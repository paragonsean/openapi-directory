from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.message import Message
from openapi_server.models.presence_message import PresenceMessage
from openapi_server import util


async def get_messages_by_channel(request: web.Request, channel_id, x_ably_version=None, format=None, start=None, limit=None, end=None, direction=None) -> web.Response:
    """Get message history for a channel

    Get message history for a channel

    :param channel_id: The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels).
    :type channel_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param start: 
    :type start: str
    :param limit: 
    :type limit: int
    :param end: 
    :type end: str
    :param direction: 
    :type direction: str

    """
    return web.Response(status=200)


async def get_presence_history_of_channel(request: web.Request, channel_id, x_ably_version=None, format=None, start=None, limit=None, end=None, direction=None) -> web.Response:
    """Get presence history of a channel

    Get presence on a channel

    :param channel_id: The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels).
    :type channel_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param start: 
    :type start: str
    :param limit: 
    :type limit: int
    :param end: 
    :type end: str
    :param direction: 
    :type direction: str

    """
    return web.Response(status=200)
