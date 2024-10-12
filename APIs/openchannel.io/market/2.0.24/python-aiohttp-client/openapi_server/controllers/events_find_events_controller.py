from typing import List, Dict
from aiohttp import web

from openapi_server.models.event import Event
from openapi_server import util


async def events_event_id_get(request: web.Request, event_id) -> web.Response:
    """Returns an event

    - Results are returned for the market provided within the basic authentication credentials 

    :param event_id: The id of the event
    :type event_id: str

    """
    return web.Response(status=200)
