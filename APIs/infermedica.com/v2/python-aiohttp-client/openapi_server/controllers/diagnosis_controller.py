from typing import List, Dict
from aiohttp import web

from openapi_server.models.diagnosis_request import DiagnosisRequest
from openapi_server.models.diagnosis_response_public import DiagnosisResponsePublic
from openapi_server import util


async def compute_diagnosis(request: web.Request, body) -> web.Response:
    """Query diagnostic engine

    Suggests possible diagnoses and relevant observations based on provided patient information.

    :param body: 
    :type body: dict | bytes

    """
    body = DiagnosisRequest.from_dict(body)
    return web.Response(status=200)
