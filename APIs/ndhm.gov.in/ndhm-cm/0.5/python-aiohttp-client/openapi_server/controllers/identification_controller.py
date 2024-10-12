from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_identification_request import PatientIdentificationRequest
from openapi_server import util


async def v05_patients_find_post(request: web.Request, authorization, body) -> web.Response:
    """Identify a patient by her consent-manager user-id

    This API is meant for identify to patient given her consent-manager-user-id. CM subsequently makes the /on-find Gateway API call with results.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientIdentificationRequest.from_dict(body)
    return web.Response(status=200)
