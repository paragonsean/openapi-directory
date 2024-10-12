from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def feedback_feedback_id_get(request: web.Request, feedback_id) -> web.Response:
    """Feedback details

    Feedback details

    :param feedback_id: 
    :type feedback_id: str

    """
    return web.Response(status=200)
