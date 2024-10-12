from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.hip_consent_notification_response import HIPConsentNotificationResponse
from openapi_server.models.hip_health_information_request_acknowledgement import HIPHealthInformationRequestAcknowledgement
from openapi_server.models.health_information_notification import HealthInformationNotification
from openapi_server.models.patient_auth_confirm_request import PatientAuthConfirmRequest
from openapi_server.models.patient_auth_init_request import PatientAuthInitRequest
from openapi_server.models.patient_auth_mode_query_request import PatientAuthModeQueryRequest
from openapi_server.models.patient_auth_notification_acknowledgement import PatientAuthNotificationAcknowledgement
from openapi_server.models.patient_care_context_link_request import PatientCareContextLinkRequest
from openapi_server.models.patient_link_reference_result import PatientLinkReferenceResult
from openapi_server.models.patient_link_result import PatientLinkResult
from openapi_server.models.patient_sms_notifcation_request import PatientSMSNotifcationRequest
from openapi_server import util


async def v05_consents_hip_on_notify_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
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


async def v05_health_information_hip_on_request_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
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


async def v05_health_information_notify_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
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


async def v05_links_link_add_contexts_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """API for HIP initiated care-context linking for patient

    API to submit care-context to CM for HIP initiated linking. The API must accompany the \&quot;accessToken\&quot; fetched in the users/auth process.     1. subsequent usage for accessToken may be invalid if it was meant for one-time usage or if it expired 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientCareContextLinkRequest.from_dict(body)
    return web.Response(status=200)


async def v05_links_link_on_confirm_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Token authenticated by HIP, indicating completion of linkage of care-contexts

    Returns a list of linked care contexts with patient reference number.   1. **Validated and linked account reference number**   2. **Validated that the token sent from Consent Manager is same as the one generated by HIP**   3. **Verified that same Consent Manager which made the link request is sending the token**   4. **Results of unmasked linked care contexts with patient reference number** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientLinkResult.from_dict(body)
    return web.Response(status=200)


async def v05_links_link_on_init_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Response to patient&#39;s care context link request

    Result of patient care-context link request from HIP end. This happens in context of previous discovery of patient found at HIP end, therefore the link requests ought to be in reference to the patient reference and care-context references previously returned by the HIP. The correlation of discovery and link request is maintained through the transactionId. HIP should have   1. **Validated transactionId in the request to check whether there was a discovery done previously, and the link request corresponds to returned patient care care context references**   2. **Before returning the response, HIP should have sent an authentication request to the patient(eg: OTP verification)**   3. **HIP should communicate the mode of authentication of a successful request**   4. **HIP subsequently should expect the token passed via /link/confirm against the link.referenceNumber passed in this call**                        The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. **Patient reference number is invalid**   2. **Care context reference numbers are invalid** 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientLinkReferenceResult.from_dict(body)
    return web.Response(status=200)


async def v05_patients_sms_notify_post(request: web.Request, authorization, x_cm_id, body) -> web.Response:
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


async def v05_users_auth_confirm_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Confirmation request sending token, otp or other authentication details from HIP/HIU for confirmation

    This API is called by HIP/HIUs to confirm authentication of users. The transactionId returned by the previous callback API /users/auth/on-init must be sent. If Authentication is successful the callback API will send an \&quot;access token\&quot; for subsequent purpose specific API calls. Note only **credential.authCode** or **credential.demographic** should be sent   1. demographic details are only required for  demographic auth as of now.    2. demographic details are required only in MEDIATED cases and if the **auth.mode** so demands. e.g. if **auth.mode** is DEMOGRAPHICS. Usually for demographic authentication, the name, gender and DOB must be exactly as specified in User Account.   3. demographic.identifier is optional, however maybe required if authentication so mandates.    4. credential.authCode is required for other MEDIATED authentication like MOBILE_OTP, AADHAAR_OTP.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthConfirmRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_fetch_modes_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Get a patient&#39;s authentication modes relevant to specified purpose

    This API is meant for identify supported authentication modes for a patient given a specific purpose 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthModeQueryRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_init_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """Initialize authentication from HIP

    This API is called by HIPs to initiate authentication of users. A transactionId is retuned by the corresponding callback API for confirmation of user auth. 

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthInitRequest.from_dict(body)
    return web.Response(status=200)


async def v05_users_auth_on_notify_post_0(request: web.Request, authorization, x_cm_id, body) -> web.Response:
    """callback API by HIU/HIPs as acknowledgement of auth notification

    This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  

    :param authorization: Access token which was issued after successful login with gateway auth server.
    :type authorization: str
    :param x_cm_id: Suffix of the consent manager to which the request was intended.
    :type x_cm_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatientAuthNotificationAcknowledgement.from_dict(body)
    return web.Response(status=200)
