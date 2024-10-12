from typing import List, Dict
from aiohttp import web

from openapi_server.models.dtmf_request import DTMFRequest
from openapi_server.models.dtmf_response import DTMFResponse
from openapi_server import util


async def start_dtmf(request: web.Request, uuid, body) -> web.Response:
    """Play DTMF tones into a call

    Play DTMF tones into a call

    :param uuid: UUID of the Call Leg
    :type uuid: str
    :param body: action to perform
    :type body: dict | bytes

    """
    body = DTMFRequest.from_dict(body)
    return web.Response(status=200)
