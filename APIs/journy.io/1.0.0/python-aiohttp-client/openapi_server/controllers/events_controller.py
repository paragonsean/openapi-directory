from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_account202_response import DeleteAccount202Response
from openapi_server.models.delete_account400_response import DeleteAccount400Response
from openapi_server.models.get_events200_response import GetEvents200Response
from openapi_server.models.track_journey_event_request import TrackJourneyEventRequest
from openapi_server import util


async def get_events(request: web.Request, ) -> web.Response:
    """Get events

    Endpoint to list events.


    """
    return web.Response(status=200)


async def track_journey_event(request: web.Request, body) -> web.Response:
    """Track event

    Endpoint used to track an event for a user or an account.  This endpoint is moved to [Track](#operation/trackEvent).

    :param body: 
    :type body: dict | bytes

    """
    body = TrackJourneyEventRequest.from_dict(body)
    return web.Response(status=200)
