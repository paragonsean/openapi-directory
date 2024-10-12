from typing import List, Dict
from aiohttp import web

from openapi_server.models.discord_message_request import DiscordMessageRequest
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server import util


async def discord_get_discord_get(request: web.Request, channel, message=None, base64_message=None, authorization=None) -> web.Response:
    """Discord Get

    

    :param channel: 
    :type channel: str
    :param message: 
    :type message: str
    :param base64_message: 
    :type base64_message: str
    :param authorization: 
    :type authorization: str

    """
    return web.Response(status=200)


async def discord_post_discord_post(request: web.Request, body, authorization=None) -> web.Response:
    """Discord Post

    

    :param body: 
    :type body: dict | bytes
    :param authorization: 
    :type authorization: str

    """
    body = DiscordMessageRequest.from_dict(body)
    return web.Response(status=200)
