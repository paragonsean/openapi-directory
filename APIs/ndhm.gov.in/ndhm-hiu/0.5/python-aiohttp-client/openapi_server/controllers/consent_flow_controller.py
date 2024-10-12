from typing import List, Dict
from aiohttp import web

from openapi_server.models.consent_artefact_response import ConsentArtefactResponse
from openapi_server.models.consent_request_init_response import ConsentRequestInitResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hiu_consent_notification_event import HIUConsentNotificationEvent
from openapi_server.models.hiu_consent_request_status import HIUConsentRequestStatus
from openapi_server import util


async def v05_consent_requests_on_init_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Response to consent request

    Result of consent request creation for a patient. **id** represents the consentrequest id created by CM. The result must contain either **id** or the **error** caused. &lt;br/&gt;   Reasons for error may be   * Invalid references (e.g patient id, hiu id), purpose, hiTypes, ranges, persmission 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentRequestStatus.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hiu_notify_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Consent notification

    Health information user will get notified about the consent request granted or denied, consent revoked, consent expired.  1. For consent request grant, status&#x3D;GRANTED, consentRequestId&#x3D;&lt;consent-request-id&gt;, and consentArtefacts is an array of generated consent artefact Ids. 2. For consent request expiry, status&#x3D;EXPIRED, consentRequestId&#x3D;&lt;consent-request-id&gt; 3. For consent request denied, status&#x3D;DENIED, consentRequestId&#x3D;&lt;consent-request-id&gt; 4. For consent revocation, status&#x3D;REVOKED, consentArtefacts is an array of revoked consent artefact ids 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentNotificationEvent.from_dict(body)
    return web.Response(status=200)


async def v05_consents_on_fetch_post(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Result of fetch request for a consent artefact

    Must contain either consent or error. Possible reason of errors are  1. consentId passed through /fetch is invalid 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentArtefactResponse.from_dict(body)
    return web.Response(status=200)
