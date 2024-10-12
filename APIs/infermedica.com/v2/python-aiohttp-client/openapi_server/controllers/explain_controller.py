from typing import List, Dict
from aiohttp import web

from openapi_server.models.explanation_request import ExplanationRequest
from openapi_server.models.explanation_response import ExplanationResponse
from openapi_server import util


async def compute_explanation(request: web.Request, body) -> web.Response:
    """Query diagnostic engine for explanation

    Explains which evidence impact probability of selected condition.

    :param body: 
    :type body: dict | bytes

    """
    body = ExplanationRequest.from_dict(body)
    return web.Response(status=200)
