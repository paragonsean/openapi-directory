from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.triage_response import TriageResponse
from openapi_server import util


async def compute_triage(request: web.Request, body) -> web.Response:
    """Query diagnostic engine for triage level

    Estimates triage level based on provided patient information.

    :param body: 
    :type body: dict | bytes

    """
    body = DiagnosisRequest.from_dict(body)
    return web.Response(status=200)
