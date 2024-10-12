from typing import List, Dict
from aiohttp import web

from openapi_server.models.start_stream_request import StartStreamRequest
from openapi_server.models.start_stream_response import StartStreamResponse
from openapi_server.models.stop_stream_response import StopStreamResponse
from openapi_server import util


async def start_stream(request: web.Request, uuid, body) -> web.Response:
    """Play an audio file into a call

    Play an audio file into a call

    :param uuid: UUID of the Call Leg
    :type uuid: str
    :param body: action to perform
    :type body: dict | bytes

    """
    body = StartStreamRequest.from_dict(body)
    return web.Response(status=200)


async def stop_stream(request: web.Request, uuid) -> web.Response:
    """Stop playing an audio file into a call

    Stop playing an audio file into a call

    :param uuid: UUID of the Call Leg
    :type uuid: str

    """
    return web.Response(status=200)
