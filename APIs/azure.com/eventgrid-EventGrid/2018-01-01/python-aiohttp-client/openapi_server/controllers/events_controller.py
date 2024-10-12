from typing import List, Dict
from aiohttp import web

from openapi_server.models.event_grid_event import EventGridEvent
from openapi_server import util


async def publish_events(request: web.Request, api_version, events) -> web.Response:
    """publish_events

    Publishes a batch of events to an Azure Event Grid topic.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param events: An array of events to be published to Event Grid.
    :type events: list | bytes

    """
    events = [EventGridEvent.from_dict(d) for d in events]
    return web.Response(status=200)
