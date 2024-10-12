from typing import List, Dict
from aiohttp import web

from openapi_server.models.consent_artefact_response import ConsentArtefactResponse
from openapi_server.models.consent_request_init_response import ConsentRequestInitResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification import HIPConsentNotification
from openapi_server.models.hiphi_request import HIPHIRequest
from openapi_server.models.hiu_consent_notification_event import HIUConsentNotificationEvent
from openapi_server.models.hiu_consent_request_status import HIUConsentRequestStatus
from openapi_server.models.hiu_health_information_request_response import HIUHealthInformationRequestResponse
from openapi_server.models.hiu_subscription_notification import HIUSubscriptionNotification
from openapi_server.models.hiu_subscription_request_receipt import HIUSubscriptionRequestReceipt
from openapi_server.models.link_confirmation_request import LinkConfirmationRequest
from openapi_server.models.patient_auth_confirm_response import PatientAuthConfirmResponse
from openapi_server.models.patient_auth_init_response import PatientAuthInitResponse
from openapi_server.models.patient_auth_mode_query_response import PatientAuthModeQueryResponse
from openapi_server.models.patient_auth_notification import PatientAuthNotification
from openapi_server.models.patient_care_context_link_response import PatientCareContextLinkResponse
from openapi_server.models.patient_discovery_request import PatientDiscoveryRequest
from openapi_server.models.patient_discovery_result import PatientDiscoveryResult
from openapi_server.models.patient_identification_response import PatientIdentificationResponse
from openapi_server.models.patient_link_reference_request import PatientLinkReferenceRequest
from openapi_server.models.patient_sms_notifcation_response import PatientSMSNotifcationResponse
from openapi_server.models.share_profile_request import ShareProfileRequest
from openapi_server.models.subscription_approval_notification import SubscriptionApprovalNotification
from openapi_server import util


async def v05_care_contexts_discover_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Discover patient&#39;s accounts

    Request for patient care context discover, made by CM for a specific HIP. It is expected that HIP will subsequently return either zero or one patient record with (potentially masked) associated care contexts   1. **At least one of the verified identifier matches**   2. **Name (fuzzy), gender matches**   3. **If YoB was given, age band(+-2) matches**   4. **If unverified identifiers were given, one of them matches**   5. **If more than one patient records would be found after aforementioned steps, then patient who matches most verified and unverified identifiers would be returned.**   6. **If there would be still more than one patients (after ranking) error would be returned**   7. **Intended HIP should be able to resolve and identify results returned in the subsequent link confirmation request via the specified transactionId**   8. **Intended HIP should store the discovery results with transactionId and care contexts discovered for subsequent link initiation** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientDiscoveryRequest.from_dict(body)
    return web.Response(status=200)


async def v05_care_contexts_on_discover_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Response to patient&#39;s account discovery request

    Result of patient care-context discovery request at HIP end. If a matching patient found with zero or more care contexts associated, it is specified as result attribute. If the prior discovery request, resulted in errors then it is specified in the error attribute. Reasons of errors can be    1. **more than one definitive match for the given request**    2. **no verified identifer was specified** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientDiscoveryResult.from_dict(body)
    return web.Response(status=200)


async def v05_consent_requests_on_init_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
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


async def v05_consent_requests_on_status_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
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


async def v05_consents_hip_notify_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
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


async def v05_consents_hiu_notify_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
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


async def v05_consents_on_fetch_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
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


async def v05_health_information_cm_on_request_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
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


async def v05_health_information_hip_request_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
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


async def v05_links_link_confirm_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Token submission by Consent Manager for link confirmation

    API to submit the token that was sent by HIP during the link request.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = LinkConfirmationRequest.from_dict(body)
    return web.Response(status=200)


async def v05_links_link_init_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Link patient&#39;s care contexts

    Request from CM to links care contexts associated with only one patient   1. **Validate account reference number and care context reference number**   2. **Validate transactionId in the request with discovery request entry to check whether there was a discovery       and were these care contexts discovered or not for a given patient**   3. **Before eventual link confirmation, HIP needs to authenticate the request with the patient(eg: OTP verification)**   4. **HIP should communicate the mode of authentication of a successful request to Consent Manager** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientLinkReferenceRequest.from_dict(body)
    return web.Response(status=200)


async def v05_links_link_on_add_contexts_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """callback API for HIP initiated patient linking /link/add-context

    If the accessToken is valid for purpose of linking, and specified details provided, CM will send \&quot;acknoweldgement.status\&quot; as SUCCESS. If any error occcurred, for example invalid token, or other required patient or care-context information not provided, then \&quot;error\&quot; attribute conveys so.    1. **accessToken must be valid and must be for the purpose of linking** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientCareContextLinkResponse.from_dict(body)
    return web.Response(status=200)


async def v05_patients_on_find_post_0(request: web.Request, authorization, body) -> web.Response:
    """Identification result for a consent-manager user-id

    If a patient is found then patient.name contains the patients name.  Otherwise, patient is not provided, and possibly error is raised for invalid requests Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. specify **X-HIU-ID** if the requester is HIU (identified from /find requester.id) 2. specify **X-HIP-ID** if the requester is HIP (identified from /find requester.id) 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientIdentificationResponse.from_dict(body)
    return web.Response(status=200)


async def v05_patients_profile_share_post_0(request: web.Request, authorization, x_hip_id, body) -> web.Response:
    """Share patient profile details

    Request for sharing patient&#39;s profile details to HIP 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ShareProfileRequest.from_dict(body)
    return web.Response(status=200)


async def v05_patients_sms_on_notify_post(request: web.Request, authorization, x_hip_id, body) -> web.Response:
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


async def v05_subscription_requests_cm_on_init_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """callback API for the /subscription-requests/cm/init to notify a HIU on acceptance/acknowledgement of the request for subscription.

    This callback API acknowledges the request for subscription from a HIU, and sends back a \&quot;id\&quot; that will be used when the patient/user approves or denies the subscription.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionRequestReceipt.from_dict(body)
    return web.Response(status=200)


async def v05_subscription_requests_hiu_notify_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Notification for subscription grant/deny/revoke

    This API is used by CM to notify a HIU to grant or deny a request for subscription, and also to notify that in case an existing subscription is revoked or expired. For notifying that a particular subscription request was GRANTED or DENIED, the **subscriptionRequestId** is passed.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionApprovalNotification.from_dict(body)
    return web.Response(status=200)


async def v05_subscriptions_hiu_notify_post_0(request: web.Request, authorization, x_hiu_id, body) -> web.Response:
    """Notification to HIU on basis of a granted subscription

    This API is used by CM to notify a HIU for notification relevant to subscription. Notifications are sent to subscribed HIUs whenever a new care-context is linked or new data is available on an existing linked care-context.  1. if event.category &#x3D; LINK, then only care-contexts are passed when new care-contexts are linked for patient.  2. If event.category &#x3D; DATA, then hiTypes are passed. Care-context is passed only if the subscribed HIU has any valid consent for that care-context 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionNotification.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_notify_post_0(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """notification API in case of DIRECT mode of authentication by the CM

    This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \&quot;auth.status\&quot; conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthNotification.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_confirm_post_0(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not

    This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.      

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthConfirmResponse.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_fetch_modes_post_0(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """Identification result for a consent-manager user-id

    If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthModeQueryResponse.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_init_post_0(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """Response to user authentication initialization from HIP

    If the patient&#39;s id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then &#39;auth.mode&#39; will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.                         The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_hip_id: Identifier of the health information provider to which the request was intended.
    :type x_hip_id: str
    :param x_hiu_id: Identifier of the health information user to which the request was intended.
    :type x_hiu_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthInitResponse.from_dict(body)
    return web.Response(status=200)
