from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def status(request: web.Request, msg_id) -> web.Response:
    """status

    

    :param msg_id: The ID from the SMS.
    :type msg_id: str

    """
    return web.Response(status=200)
