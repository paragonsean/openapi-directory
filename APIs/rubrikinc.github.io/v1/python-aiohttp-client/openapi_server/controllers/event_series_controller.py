from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_series_summary_v1 import EventSeriesSummaryV1
from openapi_server import util


async def query_event_series_by_id_v1(request: web.Request, id) -> web.Response:
    """Get all events and relevant information associated with an event series ID

    Gets all events, event series, SLA Domain, and object information that is associated with a specified event series ID.

    :param id: The ID of the event series.
    :type id: str

    """
    return web.Response(status=200)
