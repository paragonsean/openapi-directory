from typing import List, Dict
from aiohttp import web

from openapi_server.models.message_status import MessageStatus
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def status_get(request: web.Request, message_id=None) -> web.Response:
    """Get the current status of message

    

    :param message_id: respose of POST request
    :type message_id: str

    """
    return web.Response(status=200)
