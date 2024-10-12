from typing import List, Dict
from aiohttp import web

from openapi_server.models.channels_entity import ChannelsEntity
from openapi_server.models.error401 import Error401
from openapi_server.models.error403 import Error403
from openapi_server.models.error404 import Error404
from openapi_server.models.error422 import Error422
from openapi_server.models.error500 import Error500
from openapi_server.models.events_channels_entity import EventsChannelsEntity
from openapi_server import util


async def fetch_all_channels(request: web.Request, label=None, show_ignored=None, sort=None, page_size=None, accept_language=None) -> web.Response:
    """Find all channels

    

    :param label: Find only the channels whose label contains this value.
    :type label: str
    :param show_ignored: If set to &#x60;false&#x60;, show only the channels which are not ignored. If set to &#x60;true&#x60;, show all channels.
    :type show_ignored: bool
    :param sort: Sort the channels in the corresponding order.
    :type sort: str
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)


async def fetch_all_events_channels(request: web.Request, event_id, show_ignored=None, page_size=None) -> web.Response:
    """Find all channels for one event

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param show_ignored: If set to &#x60;false&#x60;, show only the [event-]channels which are not ignored. If set to &#x60;true&#x60;, show everything.
    :type show_ignored: bool
    :param page_size: Pagination size, i.e. maximum number of items to be displayed in the response.
    :type page_size: int

    """
    return web.Response(status=200)


async def fetch_one_channel(request: web.Request, channel_id, accept_language=None) -> web.Response:
    """Get one channel by ID

    

    :param channel_id: ID of the targeted channel.
    :type channel_id: int
    :param accept_language: Language used for the translatable labels.
    :type accept_language: str

    """
    return web.Response(status=200)


async def fetch_one_event_channel(request: web.Request, event_id, channel_id) -> web.Response:
    """Get one event channel by ID

    

    :param event_id: ID of the targeted event.
    :type event_id: int
    :param channel_id: ID of the targeted event channel.
    :type channel_id: int

    """
    return web.Response(status=200)
