from typing import List, Dict
from aiohttp import web

from openapi_server.models.events_v1_sink_sink_validate import EventsV1SinkSinkValidate
from openapi_server import util


async def create_sink_validate(request: web.Request, sid, test_id) -> web.Response:
    """create_sink_validate

    Validate that a test event for a Sink was received.

    :param sid: A 34 character string that uniquely identifies the Sink being validated.
    :type sid: str
    :param test_id: A 34 character string that uniquely identifies the test event for a Sink being validated.
    :type test_id: str

    """
    return web.Response(status=200)
