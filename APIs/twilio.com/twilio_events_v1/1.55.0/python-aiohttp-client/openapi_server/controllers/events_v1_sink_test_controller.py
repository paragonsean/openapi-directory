from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_sink_sink_test import EventsV1SinkSinkTest
from openapi_server import util


async def create_sink_test(request: web.Request, sid) -> web.Response:
    """create_sink_test

    Create a new Sink Test Event for the given Sink.

    :param sid: A 34 character string that uniquely identifies the Sink to be Tested.
    :type sid: str

    """
    return web.Response(status=200)
