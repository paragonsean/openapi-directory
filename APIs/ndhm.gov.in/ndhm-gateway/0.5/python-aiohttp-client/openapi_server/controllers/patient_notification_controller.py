from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest
from openapi_server.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse
from openapi_server import util


async def v05_patients_sms_notify_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """API for HIP to send SMS notifications to patients

    API to send SMS notifications to patient with custom deeplink. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientSMSNotifcationRequest.from_dict(body)
    return web.Response(status=200)


async def v05_patients_sms_on_notify_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Acknowledgment response for SMS notification sent to patient by HIP

    If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientSMSNotifcationResponse.from_dict(body)
    return web.Response(status=200)
