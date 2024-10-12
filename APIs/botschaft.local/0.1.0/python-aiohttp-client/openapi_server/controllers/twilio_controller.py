from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.twilio_message_request import TwilioMessageRequest
from openapi_server import util


async def twilio_message_get_twilio_get(request: web.Request, to, message=None, base64_message=None, authorization=None) -> web.Response:
    """Twilio Message Get

    

    :param to: 
    :type to: str
    :param message: 
    :type message: str
    :param base64_message: 
    :type base64_message: str
    :param authorization: 
    :type authorization: str

    """
    return web.Response(status=200)


async def twilio_message_post_twilio_post(request: web.Request, body, authorization=None) -> web.Response:
    """Twilio Message Post

    

    :param body: 
    :type body: dict | bytes
    :param authorization: 
    :type authorization: str

    """
    body = TwilioMessageRequest.from_dict(body)
    return web.Response(status=200)
