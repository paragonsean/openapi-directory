from typing import List, Dict
from aiohttp import web

from openapi_server.models.behavioral_event_http_completion_request import BehavioralEventHttpCompletionRequest
from openapi_server.models.error import Error
from openapi_server import util


async def post_events_v3_send_send(request: web.Request, body) -> web.Response:
    """Send custom event completion

    Endpoint to send an instance of a custom event.

    :param body: 
    :type body: dict | bytes

    """
    body = BehavioralEventHttpCompletionRequest.from_dict(body)
    return web.Response(status=200)
