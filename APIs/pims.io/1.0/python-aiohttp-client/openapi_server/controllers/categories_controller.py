from typing import List, Dict
from aiohttp import web

from openapi_server.models.categories_entity import CategoriesEntity
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_categories_entity import EventsCategoriesEntity
from openapi_server import util


async def fetch_all_categories(request: web.Request, label=None, show_ignored=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all categories

    

    :param label: Find only the categories whose label/short label contains this value.
    :type label: str
    :param show_ignored: If set to &#x60;false&#x60;, show only the categories which are not ignored. If set to &#x60;true&#x60;, show all categories.
    :type show_ignored: bool
    :param sort: Sort the categories in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)


async def fetch_all_events_categories(request: web.Request, event_id, show_ignored=None, page_size=None) -> web.Response:
    """Find all categories for one event

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int

    """
    return web.Response(status=200)


async def fetch_one_category(request: web.Request, category_id, accept_language=None) -> web.Response:
    """Get one category by ID

    

    :param category_id: ID of the targeted category.
    :type category_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)


async def fetch_one_event_category(request: web.Request, event_id, category_id, show_ignored=None) -> web.Response:
    """Get one event category by ID

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param category_id: ID of the targeted event category.
    :type category_id: 
    :param show_ignored: If set to &#x60;false&#x60;, show only the embedded [event-]price ranges which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool

    """
    return web.Response(status=200)
