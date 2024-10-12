from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.track_event_request import TrackEventRequest
from openapi_server import util


async def track_event(request: web.Request, body) -> web.Response:
    """Track event

    Endpoint used to track an event for a user or an account.

    :param body: 
    :type body: dict | bytes

    """
    body = TrackEventRequest.from_dict(body)
    return web.Response(status=200)
