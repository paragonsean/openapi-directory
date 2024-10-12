from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.suggest_result import SuggestResult
from openapi_server import util


async def compute_red_flags(request: web.Request, body, max_results=None) -> web.Response:
    """Query the diagnostic engine for possible red flag symptoms

    Suggests possible red flag symptoms based on provided patient information.

    :param body: 
    :type body: dict | bytes
    :param max_results: maximum number of results
    :type max_results: int

    """
    body = DiagnosisRequest.from_dict(body)
    return web.Response(status=200)
