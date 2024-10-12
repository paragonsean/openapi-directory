from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.sns_message_request import SnsMessageRequest
from openapi_server import util


async def sns_get_sns_get(request: web.Request, message=None, base64_message=None, authorization=None) -> web.Response:
    """Sns Get

    

    :param message: 
    :type message: str
    :param base64_message: 
    :type base64_message: str
    :param authorization: 
    :type authorization: str

    """
    return web.Response(status=200)


async def sns_post_sns_post(request: web.Request, body, authorization=None) -> web.Response:
    """Sns Post

    

    :param body: 
    :type body: dict | bytes
    :param authorization: 
    :type authorization: str

    """
    body = SnsMessageRequest.from_dict(body)
    return web.Response(status=200)
