from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse
from openapi_server import util


async def v05_patients_sms_on_notify_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Acknowledgment response for SMS notification sent to patient by HIP

    If the SMS notification is successfully sent to patient then \&quot;status\&quot; will be \&quot;ACKNOWLEDGED\&quot; with no error. If the SMS notification is failed then \&quot;status\&quot; will be \&quot;ERRORED\&quot; with error. 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientSMSNotifcationResponse.from_dict(body)
    return web.Response(status=200)
