from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.ticket_counts_detailed_entity import TicketCountsDetailedEntity
from openapi_server.models.ticket_counts_entity import TicketCountsEntity
from openapi_server import util


async def fetch_all_detailed_ticket_counts(request: web.Request, event_id, from_date=None, to_date=None, show_ignored=None, show_not_approved=None, sort=None, page_size=None) -> web.Response:
    """Find all detailed ticket counts for one event

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param from_date: Find only the ticket counts after this date.
    :type from_date: str
    :param to_date: Find only the ticket counts before this date.
    :type to_date: str
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool
    :param show_not_approved: If set to &#x60;false&#x60;, show only the approved ticket counts. If set to &#x60;true&#x60;, show all the ticket counts.
    :type show_not_approved: bool
    :param sort: Sort the ticket counts in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def fetch_all_ticket_counts(request: web.Request, event_id, from_date=None, to_date=None, show_ignored=None, show_not_approved=None, sort=None, page_size=None) -> web.Response:
    """Find all ticket counts for one event

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param from_date: Find only the ticket counts after this date.
    :type from_date: str
    :param to_date: Find only the ticket counts before this date.
    :type to_date: str
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool
    :param show_not_approved: If set to &#x60;false&#x60;, show only the approved ticket counts. If set to &#x60;true&#x60;, show all the ticket counts.
    :type show_not_approved: bool
    :param sort: Sort the ticket counts in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int

    """
    from_date = util.deserialize_date(from_date)
    to_date = util.deserialize_date(to_date)
    return web.Response(status=200)


async def fetch_one_detailed_ticket_count(request: web.Request, event_id, ticket_count_id, show_ignored=None) -> web.Response:
    """Get one detailed ticket count by ID

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param ticket_count_id: ID of the targeted ticket count.
    :type ticket_count_id: int
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool

    """
    return web.Response(status=200)


async def fetch_one_ticket_count(request: web.Request, event_id, ticket_count_id, show_ignored=None) -> web.Response:
    """Get one ticket count by ID

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param ticket_count_id: ID of the targeted ticket count.
    :type ticket_count_id: int
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool

    """
    return web.Response(status=200)
