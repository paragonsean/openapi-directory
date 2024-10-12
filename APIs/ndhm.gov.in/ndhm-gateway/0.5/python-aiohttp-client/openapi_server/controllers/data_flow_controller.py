from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiphi_request import HIPHIRequest
from openapi_server.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
from openapi_server.models.hi_request import HIRequest
from openapi_server.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
from openapi_server.models.health_information_notification import HealthInformationNotification
from openapi_server import util


async def v05_health_information_cm_on_request_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Health information data request

    Callback API for acknowledgement of Health information request of HIU. CM calls this API when it has validated the Health Information request given the consent id. Either the **hiRequest** or **error** would need to be specified. If the health info request was valid, then the ***hiRequest.transactionId*** specifies the transaction context against which HIP would send over the data.  Possible cases of errors are   1. **Invalid consent artefact id**   2. **Consent has expired**   3. **Date ranges are invalid** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUHealthInformationRequestResponse.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_cm_request_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Health information data request

    Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIRequest.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_hip_on_request_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Health information data request

    API called by HIP to acknowledge Health information request receipt. Either the **hiRequest** or **error** must be specified. **hiRequest** element returns the same transactionId as before with a status indicating that the request is acknowledged.   

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPHealthInformationRequestAcknowledgement.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_hip_request_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Health information data request

    API called by CM to request Health information from HIP against a validated consent artefact. The transactionId is the correlation id that HIP should use use when pushing data to the **dataPushUrl**.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPHIRequest.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Notifications corresponding to events during data flow

    API called by HIU and HIP during data-transfer.  1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED]  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HealthInformationNotification.from_dict(body)
    return web.Response(status=200)
