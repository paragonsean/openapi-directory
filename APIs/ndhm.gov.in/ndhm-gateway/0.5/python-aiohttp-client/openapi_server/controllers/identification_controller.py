from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_identification_request import PatientIdentificationRequest
from openapi_server.models.patient_identification_response import PatientIdentificationResponse
from openapi_server import util


async def v05_patients_find_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Identify a patient by her consent-manager user-id

    This API is meant for identify to patient given her consent-manager-user-id 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientIdentificationRequest.from_dict(body)
    return web.Response(status=200)


async def v05_patients_on_find_post(request: web.Request, authorization, body) -> web.Response:
    """Identification result for a consent-manager user-id

    If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientIdentificationResponse.from_dict(body)
    return web.Response(status=200)
