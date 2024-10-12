from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.patient_auth_confirm_response import PatientAuthConfirmResponse
from openapi_server.models.patient_auth_init_response import PatientAuthInitResponse
from openapi_server.models.patient_auth_mode_query_response import PatientAuthModeQueryResponse
from openapi_server.models.patient_auth_notification import PatientAuthNotification
from openapi_server import util


async def v05_users_auth_notify_post(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """notification API in case of DIRECT mode of authentication by the CM

    This API is called by CM to confirm authentication of users. The transactionId returned is same as that passed in /auth/on-init. The \&quot;auth.status\&quot; conveys whether the request was GRANTED or DENIED.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.   3. The payload is conditional to the purpose of auth. If purpose specified in /auth/init is KYC or KYC_AND_LINK, then patient details are passed. **auth.accessToken** is passed only if the purpose is LINK or KYC_AND_LINK. 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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


async def v05_users_auth_on_confirm_post(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """callback API for /auth/confirm (in case of MEDIATED auth) to confirm user authentication or not

    This API is called by CM to confirm authentication of users.    1. **auth.accessToken** - is specific to the purpose mentioned in the /auth/init. This token needs to be used for initiating the intended action. For example for HIP initiated linking of care-contexts   2. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.      

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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


async def v05_users_auth_on_fetch_modes_post(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """Identification result for a consent-manager user-id

    If a patient is found then **auth** attribute contains the supported modes for the specified purpose.  Otherwise, error is raised for invalid requests or for non-existent id. Note in addition to the \&quot;Authorization\&quot; header, one of the following headers must be specified 1. **X-HIU-ID** if the requester is HIU (identified from /auth/fetch-modes requester.id) 2. **X-HIP-ID** if the requester is HIP (identified from /auth/fetch-modes requester.id) 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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


async def v05_users_auth_on_init_post(request: web.Request, authorization, x_hip_id, x_hiu_id, body) -> web.Response:
    """Response to user authentication initialization from HIP

    If the patient&#39;s id is valid, CM will return a transactionId as initialization of user auth. If the request is valid, then &#39;auth.mode&#39; will convey how the authentication should be done. The authentication can be *mediated* or *direct*. For mediated authentication modes, HIP or HIU is epected to send over relevant code (OTP/token) or demographic info via subsequent API call to /auth/confirm. for direct authentication case, CM will notify requester through/users/auth/notify API.     1. **auth.mode** conveys whats the mode of authentication is, and what is expected from HIP/HIU in the subsequent /auth/confirm API call. Possible values        1. MOBILE_OTP - auth via OTP to registered mobile. Mediated.        2. AADHAAR_OTP - auth initiated with Aadhaar with OTP. Mediated.        3. DEMOGRAPHICS - auth initiated with demographic verification       4. DIRECT - for authentication directly with the patient. e.g. Mobile App, SMS. In this case, the HIP/HIU is not expected to call subsequent /auth/confirm call. CM will do direct authentication with the User (e.g. Mobile App, SMS etc) and will notify requester   2. **meta.expiry** conveys the expiry time of the token and the authentication session   3. **NOTE**, only one of **X-HIP-ID** or **X-HIU-ID** will be sent as part of header, not both.                         The error section in the body, represents the potential errors that may have occurred. Possible reasons:   1. Patient id is invalid 

    :param authorization: Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
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
