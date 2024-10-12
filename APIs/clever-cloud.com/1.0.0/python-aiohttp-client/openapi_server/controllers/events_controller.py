from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def events_event_socket_get_0(request: web.Request, ) -> web.Response:
    """events_event_socket_get_0

    Retrieve events as they come through a websocket connection. To have authorization, you have to send a &#x60;{ \&quot;message_type\&quot;: \&quot;oauth\&quot;, \&quot;authorization\&quot;: \&quot;oauth authorization string\&quot; }&#x60; message


    """
    return web.Response(status=200)


async def notifications_info_events_get_0(request: web.Request, ) -> web.Response:
    """notifications_info_events_get_0

    list available events


    """
    return web.Response(status=200)
