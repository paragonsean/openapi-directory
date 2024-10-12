from typing import List, Dict
from aiohttp import web

from openapi_server.models.consent_artefact_response import ConsentArtefactResponse
from openapi_server.models.consent_fetch_request import ConsentFetchRequest
from openapi_server.models.consent_request import ConsentRequest
from openapi_server.models.consent_request_init_response import ConsentRequestInitResponse
from openapi_server.models.consent_request_status_request import ConsentRequestStatusRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification import HIPConsentNotification
from openapi_server.models.hip_consent_notification_response import HIPConsentNotificationResponse
from openapi_server.models.hiu_consent_notification_event import HIUConsentNotificationEvent
from openapi_server.models.hiu_consent_notification_response import HIUConsentNotificationResponse
from openapi_server.models.hiu_consent_request_status import HIUConsentRequestStatus
from openapi_server import util


async def v05_consent_requests_init_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Create consent request

    Creates a consent request to get data about a patient by HIU user.

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consent_requests_on_init_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Response to consent request

    Result of consent request creation for a patient. **consentRequest.id** represents the consentrequest id created by CM. The result must contain either **consentRequest** or the **error** caused. &lt;br/&gt;   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentRequestInitResponse.from_dict(body)
    return web.Response(status=200)


async def v05_consent_requests_on_status_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Result of consent request status

    Result of consent request done previously. Status of request can be GRANTED,  DENIED, EXPIRED. If the request was GRANTED, then  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentRequestStatus.from_dict(body)
    return web.Response(status=200)


async def v05_consent_requests_status_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Get consent request status

    Get status of consent request done previously

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentRequestStatusRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consents_fetch_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Get consent artefact

    

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentFetchRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hip_notify_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Consent notification

    Notification of consents to health information providers consent request granted, consent revoked, consent expired. Only the GRANTED, REVOKED and EXPIRED status notifications will be sent to HIP.   1. If consent is granted, status&#x3D;GRANTED, then consentDetail contains the consent artefact details and signature is available.    2. If consent is revoked, then status&#x3D;REVOKED, and consentId specifes which consent artefact is revoked.    3. If the consent has expired, then status&#x3D;EXPIRED, and consentId specifies which consent artefact has expired. Note, this is also responsibility of the HIP to keep track of consent expiry. Any data request on expired consent artefact must not be done.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPConsentNotification.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hip_on_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Consent notification

    This API is called by HIP as acknowledgement to notification of consents, in cases of consent revocation and expiration.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIPConsentNotificationResponse.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hiu_notify_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Consent notification

    Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status&#x3D;GRANTED, consentRequestId&#x3D;&lt;consent-request-id&gt;, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status&#x3D;EXPIRED, consentRequestId&#x3D;&lt;consent-request-id&gt; 3. For consent request denied, status&#x3D;DENIED, consentRequestId&#x3D;&lt;consent-request-id&gt; 4. For consent revocation, status&#x3D;REVOKED, consentArtefacts is an array of revoked consent artefact ids 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentNotificationEvent.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hiu_on_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Consent notification

    This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentNotificationResponse.from_dict(body)
    return web.Response(status=200)


async def v05_consents_on_fetch_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Result of fetch request for a consent artefact

    Must contain either consentDetail or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentArtefactResponse.from_dict(body)
    return web.Response(status=200)
