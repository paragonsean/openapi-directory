from typing import List, Dict
from aiohttp import web

from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_entity import EventsEntity
from openapi_server import util


async def fetch_all_events(request: web.Request, label=None, from_datetime=None, to_datetime=None, city=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all events

    

    :param label: Find only the events whose label contains this value.
    :type label: str
    :param from_datetime: Find only the events starting after this date.
    :type from_datetime: str
    :param to_datetime: Find only the events starting before this date.
    :type to_datetime: str
    :param city: Find only the events whose venue city (or metropolitan area) contains this value.
    :type city: str
    :param sort: Sort the events in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_datetime = util.deserialize_date(from_datetime)
    to_datetime = util.deserialize_date(to_datetime)
    return web.Response(status=200)


async def fetch_all_series_events(request: web.Request, series_id, from_datetime=None, to_datetime=None, city=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all events for one series

    

    :param series_id: ID of the targeted series.
    :type series_id: int
    :param from_datetime: Find only the events starting after this date.
    :type from_datetime: str
    :param to_datetime: Find only the events starting before this date.
    :type to_datetime: str
    :param city: Find only the events whose venue city (or metropolitan area) contains this value.
    :type city: str
    :param sort: Sort the events in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_datetime = util.deserialize_date(from_datetime)
    to_datetime = util.deserialize_date(to_datetime)
    return web.Response(status=200)


async def fetch_all_venues_events(request: web.Request, venue_id, from_datetime=None, to_datetime=None, city=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all events for one venue

    

    :param venue_id: ID of the targeted venue.
    :type venue_id: int
    :param from_datetime: Find only the events starting after this date.
    :type from_datetime: str
    :param to_datetime: Find only the events starting before this date.
    :type to_datetime: str
    :param city: Find only the events whose venue city (or metropolitan area) contains this value.
    :type city: str
    :param sort: Sort the events in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    from_datetime = util.deserialize_date(from_datetime)
    to_datetime = util.deserialize_date(to_datetime)
    return web.Response(status=200)


async def fetch_one_event(request: web.Request, event_id, accept_language=None) -> web.Response:
    """Get one event by ID

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)
