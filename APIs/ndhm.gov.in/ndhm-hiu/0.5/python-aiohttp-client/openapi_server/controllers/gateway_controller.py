from typing import List, Dict
from aiohttp import web

from openapi_server.models.certs import Certs
from openapi_server.models.consent_fetch_request import ConsentFetchRequest
from openapi_server.models.consent_request import ConsentRequest
from openapi_server.models.consent_request_status_request import ConsentRequestStatusRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hi_request import HIRequest
from openapi_server.models.hiu_consent_notification_response import HIUConsentNotificationResponse
from openapi_server.models.hiu_subscription_notification_acknowledgment import HIUSubscriptionNotificationAcknowledgment
from openapi_server.models.hiu_subscription_request_notification_acknowledgement import HIUSubscriptionRequestNotificationAcknowledgement
from openapi_server.models.health_information_notification import HealthInformationNotification
from openapi_server.models.open_id_configuration import OpenIdConfiguration
from openapi_server.models.patient_auth_confirm_request import PatientAuthConfirmRequest
from openapi_server.models.patient_auth_init_request import PatientAuthInitRequest
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from openapi_server.models.patient_identification_request import PatientIdentificationRequest
from openapi_server.models.session_request import SessionRequest
from openapi_server.models.session_response import SessionResponse
from openapi_server.models.subscription_request import SubscriptionRequest
from openapi_server import util


async def v05_certs_get(request: web.Request, ) -> web.Response:
    """Get certs for JWT verification

    


    """
    return web.Response(status=200)


async def v05_consent_requests_init_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Create consent request

    Creates a consent request to get data about a patient by HIU user.

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consent_requests_status_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Get consent request status

    Get status of consent request done previously

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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

    

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentFetchRequest.from_dict(body)
    return web.Response(status=200)


async def v05_consents_hiu_on_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Consent notification

    This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUConsentNotificationResponse.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_cm_request_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Health information data request

    Request for Health information against a consent id. CM would generate a transactionId against each consent and pass it as trnasaction context / correlation id to the HIP and also return the same to HIU via /on-request.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIRequest.from_dict(body)
    return web.Response(status=200)


async def v05_health_information_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Notifications corresponding to events during data flow

    API called by HIU and HIP during data-transfer. 1. HIP on transfer of data would send **sessionStatus** - one of [TRANSFERRED, FAILED] 2. HIP would also send **hiStatus** for each *careContextReference* - on of [DELIVERED, ERRORED] 3. HIU on receipt of data would send **sessionStatus** - one of [TRANSFERRED, FAILED]. For example, FAILED when if data was not sent or if invalid data was sent 4. HIU would also send **hiStatus** for each *careContextReference* - one of [OK, ERRORED] 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HealthInformationNotification.from_dict(body)
    return web.Response(status=200)


async def v05_patients_find_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Identify a patient by her consent-manager user-id

    This API is meant for identify to patient given her consent-manager-user-id 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientIdentificationRequest.from_dict(body)
    return web.Response(status=200)


async def v05_sessions_post(request: web.Request, body) -> web.Response:
    """Get access token

    

    :param body: 
    :type body: dict | bytes

    """
    body = SessionRequest.from_dict(body)
    return web.Response(status=200)


async def v05_subscription_requests_cm_init_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Request for subscription

    creates a request for subscription. The subscription categories can be for care-contexts linkages or availability of data against existing care-contexts. Note that the requester must have HIU role

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SubscriptionRequest.from_dict(body)
    return web.Response(status=200)


async def v05_subscription_requests_hiu_on_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Callback API for /subscription-requests/hiu/notify to acknowledge receipt of notification.

    This API is called by HIU as acknowledgement to subscription request relevant notifications.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionRequestNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)


async def v05_subscriptions_hiu_on_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Callback API for /subscriptions/hiu/notify to acknowledge receipt of notification.

    This API is called by HIU as acknowledgement to consent notifications, specifically for cases when consent is REVOKED or EXPIRED. 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = HIUSubscriptionNotificationAcknowledgment.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_confirm_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

    This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthConfirmRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_fetch_modes_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Get a patient&#39;s authentication modes relevant to specified purpose

    This API is meant for identify supported authentication modes for a patient given a specific purpose 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthModeQueryRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_init_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Initialize authentication from HIP

    This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth.   1. **NOTE**, only **KYC** purpose is applicable for HIU. Hence HIU should only sent KYC in **query.authMode** in the request 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthInitRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """callback API by HIU/HIPs as acknowledgement of auth notification

    This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)


async def v05_well_known_openid_configuration_get(request: web.Request, ) -> web.Response:
    """Get openid configuration

    


    """
    return web.Response(status=200)
