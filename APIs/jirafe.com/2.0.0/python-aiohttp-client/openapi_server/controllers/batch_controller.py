from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch import Batch
from openapi_server import util


async def post_batch(request: web.Request, site_id, body) -> web.Response:
    """Send a batch for the given site

    

    :param site_id: ID site to send the event
    :type site_id: str
    :param body: batch json of events
    :type body: dict | bytes

    """
    body = Batch.from_dict(body)
    return web.Response(status=200)
