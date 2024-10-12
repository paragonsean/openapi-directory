from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_calendar_event_response_request import CreateCalendarEventResponseRequest
from openapi_server.models.create_or_update_error_response import CreateOrUpdateErrorResponse
from openapi_server import util


async def create_calendar_event_response(request: web.Request, body) -> web.Response:
    """Create calendar event response

    Create a calendar event response for an attendee of a calendar event, the attendee can be a coach or patient.  Calendar event responses cannot be fetched, updated nor deleted.  Use calendar event api to fetch the response status for attendees.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateCalendarEventResponseRequest.from_dict(body)
    return web.Response(status=200)
