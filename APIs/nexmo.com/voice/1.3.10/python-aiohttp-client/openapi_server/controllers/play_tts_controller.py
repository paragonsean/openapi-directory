from typing import List, Dict
from aiohttp import web

from openapi_server.models.start_talk_request import StartTalkRequest
from openapi_server.models.start_talk_response import StartTalkResponse
from openapi_server.models.stop_talk_response import StopTalkResponse
from openapi_server import util


async def start_talk(request: web.Request, uuid, body=None) -> web.Response:
    """Play text to speech into a call

    Play text to speech into a call

    :param uuid: UUID of the Call Leg
    :type uuid: str
    :param body: Action to perform
    :type body: dict | bytes

    """
    body = StartTalkRequest.from_dict(body)
    return web.Response(status=200)


async def stop_talk(request: web.Request, uuid) -> web.Response:
    """Stop text to speech in a call

    Stop text to speech in a call

    :param uuid: UUID of the Call Leg
    :type uuid: str

    """
    return web.Response(status=200)
