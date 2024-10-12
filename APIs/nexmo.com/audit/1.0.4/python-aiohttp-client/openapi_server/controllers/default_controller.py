from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit_event import AuditEvent
from openapi_server.models.audit_event_types_resp import AuditEventTypesResp
from openapi_server.models.audit_resp import AuditResp
from openapi_server.models.error_forbidden import ErrorForbidden
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_unauthorized import ErrorUnauthorized
from openapi_server.models.event_types import EventTypes
from openapi_server.models.no_content import NoContent
from openapi_server import util


async def get_event(request: web.Request, id) -> web.Response:
    """Retrieve individual audit event

    Get the specified audit event. 

    :param id: The UUID of the audit event to retrieve
    :type id: str

    """
    return web.Response(status=200)


async def get_events(request: web.Request, event_type=None, date_from=None, date_to=None, search_text=None, page=None, size=None) -> web.Response:
    """Retrieve audit events

    Get a series of audit events describing changes made to your Vonage API account over time. 

    :param event_type: Filter results by this event type.
    :type event_type: dict | bytes
    :param date_from: Start of time range for audit events. DateTime in ISO-8601 format.
    :type date_from: str
    :param date_to: End of time range for audit events. DateTime in ISO-8601 format.
    :type date_to: str
    :param search_text: Return only audit events where the JSON object contains this search text. Must be legal text for a JSON attribute value, that is quotes and braces must be escaped.
    :type search_text: str
    :param page: Page number starting with page 1.
    :type page: str
    :param size: Number of elements per page.
    :type size: int

    """
    event_type = .from_dict(event_type)
    return web.Response(status=200)


async def get_events_options(request: web.Request, ) -> web.Response:
    """Retrieve audit event types

    Get audit event types. 


    """
    return web.Response(status=200)
