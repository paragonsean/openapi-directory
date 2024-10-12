from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.event_filter import EventFilter
from openapi_server.models.event_parameter_info import EventParameterInfo
from openapi_server.models.overview_event import OverviewEvent
from openapi_server.models.overview_event_paged_results_public import OverviewEventPagedResultsPublic
from openapi_server import util


async def events_event_id_overview_get(request: web.Request, event_id) -> web.Response:
    """Get overview event

    Get overview event by id.

    :param event_id: Id of event to get.
    :type event_id: str

    """
    return web.Response(status=200)


async def events_event_id_parameters_get(request: web.Request, event_id) -> web.Response:
    """Get event parameters

    Get parameters of an event by id.

    :param event_id: Event Id of the requested Alert.
    :type event_id: str

    """
    return web.Response(status=200)


async def events_paged_post(request: web.Request, max_results=None, body=None) -> web.Response:
    """Get overview event paged.

    Get overview event paged. If there are more results, you also get a continuation token which you can add to the event filter.

    :param max_results: Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                   Number of alerts could be less if filtered but at least 1.
    :type max_results: int
    :param body: The filter defines which alerts are supposed to be retrieved.
    :type body: dict | bytes

    """
    body = EventFilter.from_dict(body)
    return web.Response(status=200)
