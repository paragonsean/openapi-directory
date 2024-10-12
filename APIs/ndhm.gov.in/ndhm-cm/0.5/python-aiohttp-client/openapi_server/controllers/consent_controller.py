from typing import List, Dict
from aiohttp import web

from openapi_server.models.consent_fetch_request import ConsentFetchRequest
from openapi_server.models.consent_request import ConsentRequest
from openapi_server.models.consent_request_status_request import ConsentRequestStatusRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification_response import HIPConsentNotificationResponse
from openapi_server.models.hiu_consent_notification_response import HIUConsentNotificationResponse
from openapi_server import util


async def v05_consent_requests_init_post(request: web.Request, authorization, body) -> web.Response:
    """Create consent request

    Creates a consent request to get data about a patient by HIU user. CM should call Gateway - ***/v0.5/consent-requests/on-init*** API with the consent-request-id

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consent_requests_status_post(request: web.Request, authorization, body) -> web.Response:
    """Get consent request status

    Get status of consent request done previously. CM responds by calling Gateway API - ***/v0.5/consent-requests/on-status***

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentRequestStatusRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consents_fetch_post(request: web.Request, authorization, body) -> web.Response:
    """Get consent artefact

    This API is called when a HIU makes a request to get a consent artefact. For response please refer to the Gateway ***/v0.5/consents/on-fetch***

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentFetchRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hip_on_notify_post(request: web.Request, authorization, body) -> web.Response:
    """Consent notification

    This API is called by HIP as acknowledgement to notification of consents, in cases of consent revocation and expiration, notified by CM earlier via Gateway API - ***/v0.5/consents/hip/notify***.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPConsentNotificationResponse.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hiu_on_notify_post(request: web.Request, authorization, body) -> web.Response:
    """Consent notification

    This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED, notified by CM earlier via Gateway API - ***/v0.5/consents/hiu/notify***. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentNotificationResponse.from_dict(body)
    return web.Response(status=200)
