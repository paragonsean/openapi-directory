from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_heartbeat import CreateHeartbeat
from openapi_server import util


async def heartbeats_create(request: web.Request, id, log_id, body=None) -> web.Response:
    """Create a new heartbeat.

    Required permission: &#x60;heartbeats_write&#x60;

    :param id: The ID of the heartbeat check.
    :type id: str
    :param log_id: The ID of the log containing the heartbeat check.
    :type log_id: str
    :param body: The details of the heartbeat.
    :type body: dict | bytes

    """
    body = CreateHeartbeat.from_dict(body)
    return web.Response(status=200)
