from typing import List, Dict
from aiohttp import web

from openapi_server.models.mark_message_as_read_request_body import MarkMessageAsReadRequestBody
from openapi_server.models.message_response import MessageResponse
from openapi_server.models.send_message_request_body import SendMessageRequestBody
from openapi_server import util


async def mark_message_as_read(request: web.Request, message_id, body) -> web.Response:
    """Mark-Message-As-Read

    

    :param message_id: Message ID from Webhook
    :type message_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = MarkMessageAsReadRequestBody.from_dict(body)
    return web.Response(status=200)


async def send_message(request: web.Request, body) -> web.Response:
    """Send-Message

    

    :param body: 
    :type body: dict | bytes

    """
    body = SendMessageRequestBody.from_dict(body)
    return web.Response(status=200)
