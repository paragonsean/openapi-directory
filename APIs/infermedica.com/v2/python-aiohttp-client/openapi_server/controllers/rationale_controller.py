from typing import List, Dict
from aiohttp import web

from openapi_server.models.rationale_request import RationaleRequest
from openapi_server.models.rationale_response import RationaleResponse
from openapi_server import util


async def compute_rationale(request: web.Request, body) -> web.Response:
    """Query diagnostic engine for question rationale

    Returns rationale behind the question asked by the system.

    :param body: 
    :type body: dict | bytes

    """
    body = RationaleRequest.from_dict(body)
    return web.Response(status=200)
