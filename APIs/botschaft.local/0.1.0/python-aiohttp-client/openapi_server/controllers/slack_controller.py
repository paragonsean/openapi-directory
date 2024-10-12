from typing import List, Dict
from aiohttp import web

from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.slack_message_request import SlackMessageRequest
from openapi_server import util


async def slack_get_slack_get(request: web.Request, channel, message=None, base64_message=None, authorization=None) -> web.Response:
    """Slack Get

    

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


async def slack_post_slack_post(request: web.Request, body, authorization=None) -> web.Response:
    """Slack Post

    

    :param body: 
    :type body: dict | bytes
    :param authorization: 
    :type authorization: str

    """
    body = SlackMessageRequest.from_dict(body)
    return web.Response(status=200)
