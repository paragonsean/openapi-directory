from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_events_event_types200_response_inner import GetNetworkEventsEventTypes200ResponseInner
from openapi_server import util


async def get_network_events_event_types_2(request: web.Request, network_id) -> web.Response:
    """List the event type to human-readable description

    List the event type to human-readable description

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)
