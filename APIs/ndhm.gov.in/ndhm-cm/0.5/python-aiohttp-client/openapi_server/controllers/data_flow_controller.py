from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
from openapi_server.models.hi_request import HIRequest
from openapi_server.models.health_information_notification import HealthInformationNotification
from openapi_server import util


async def v05_health_information_notify_post(request: web.Request, authorization, body) -> web.Response:
    """Notifications corresponding to events during data flow

    API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HealthInformationNotification.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_on_request_post(request: web.Request, authorization, body) -> web.Response:
    """Health information data request acknowledgement from HIP

    This API is called by HIP to acknowledge Health information request receipt. When HIU requests health information, CM generates a transactionId and makes a health information request to the HIP(s). HIPs acknowledgement to the health-information request is coveyed by this API. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPHealthInformationRequestAcknowledgement.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_request_post(request: web.Request, authorization, body) -> web.Response:
    """Health information data request from HIU

    HIU request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via Gateway API - ***/v0.5/health-information/cm/on-request***.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIRequest.from_dict(body)
    return web.Response(status=200)
