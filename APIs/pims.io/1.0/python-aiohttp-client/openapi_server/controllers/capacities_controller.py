from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_capacities_entity import EventsCapacitiesEntity
from openapi_server import util


async def fetch_all_events_capacities(request: web.Request, event_id, show_ignored=None, sort=None, page_size=None) -> web.Response:
    """Find all capacities for one event

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool
    :param sort: Sort the capacities in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int

    """
    return web.Response(status=200)


async def fetch_one_event_capacity(request: web.Request, event_id, capacity_id, show_ignored=None) -> web.Response:
    """Get one capacity by ID

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param capacity_id: ID of the targeted capacity.
    :type capacity_id: int
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool

    """
    return web.Response(status=200)
