from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.message import Message
from openapi_server.models.publish_messages_to_channel2_xx_response import PublishMessagesToChannel2XXResponse
from openapi_server import util


async def publish_messages_to_channel(request: web.Request, channel_id, x_ably_version=None, format=None, body=None) -> web.Response:
    """Publish a message to a channel

    Publish a message to the specified channel

    :param channel_id: The [Channel&#39;s ID](https://www.ably.io/documentation/rest/channels).
    :type channel_id: str
    :param x_ably_version: The version of the API you wish to use.
    :type x_ably_version: str
    :param format: The response format you would like
    :type format: str
    :param body: 
    :type body: dict | bytes

    """
    body = Message.from_dict(body)
    return web.Response(status=200)
