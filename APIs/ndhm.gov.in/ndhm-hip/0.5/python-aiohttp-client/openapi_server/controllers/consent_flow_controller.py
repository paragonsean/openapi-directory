from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification import HIPConsentNotification
from openapi_server import util


async def v05_consents_hip_notify_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Consent notification

    Notification of consents to health information providers consent request granted, consent revoked, consent expired. Only the GRANTED and REVOKED status notifications will be sent to HIP.   1. If consent is granted, status&#x3D;GRANTED, then consentDetail contains the consent artefact details and signature is available.    2. If consent is revoked, then status&#x3D;REVOKED, and consentId specifes which consent artefact is revoked.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPConsentNotification.from_dict(body)
    return web.Response(status=200)
