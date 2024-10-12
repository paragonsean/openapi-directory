from typing import List, Dict
from aiohttp import web

from openapi_server.models.inline_response400 import InlineResponse400
from openapi_server.models.inline_response401 import InlineResponse401
from openapi_server.models.inline_response403 import InlineResponse403
from openapi_server.models.inline_response404 import InlineResponse404
from openapi_server.models.inline_response409 import InlineResponse409
from openapi_server.models.inline_response412 import InlineResponse412
from openapi_server.models.invite_user_request import InviteUserRequest
from openapi_server.models.paged_user_response import PagedUserResponse
from openapi_server.models.password_request import PasswordRequest
from openapi_server.models.payee_type import PayeeType
from openapi_server.models.payee_user_self_update_request import PayeeUserSelfUpdateRequest
from openapi_server.models.register_sms_request import RegisterSmsRequest
from openapi_server.models.resend_token_request import ResendTokenRequest
from openapi_server.models.role_update_request import RoleUpdateRequest
from openapi_server.models.self_mfa_type_unregister_request import SelfMFATypeUnregisterRequest
from openapi_server.models.self_update_password_request import SelfUpdatePasswordRequest
from openapi_server.models.unregister_mfa_request import UnregisterMFARequest
from openapi_server.models.user_details_update_request import UserDetailsUpdateRequest
from openapi_server.models.user_response import UserResponse
from openapi_server.models.user_status import UserStatus
from openapi_server.models.user_type import UserType
from openapi_server.models.validate_password_response import ValidatePasswordResponse
from openapi_server import util


async def delete_user_by_id_v2(request: web.Request, user_id) -> web.Response:
    """Delete a User

    Delete User by Id. 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def disable_user_v2(request: web.Request, user_id) -> web.Response:
    """Disable a User

    &lt;p&gt;If a user is enabled this endpoint will disable them &lt;/p&gt; &lt;p&gt;The invoker must have the appropriate permission &lt;/p&gt; &lt;p&gt;A user cannot disable themself &lt;/p&gt; &lt;p&gt;When a user is disabled any active access tokens will be revoked and the user will not be able to log in&lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def enable_user_v2(request: web.Request, user_id) -> web.Response:
    """Enable a User

    &lt;p&gt;If a user has been disabled this endpoints will enable them &lt;/p&gt; &lt;p&gt;The invoker must have the appropriate permission &lt;/p&gt; &lt;p&gt;A user cannot enable themself &lt;/p&gt; &lt;p&gt;If the user is a payor user and the payor is disabled this operation is not allowed&lt;/p&gt; &lt;p&gt;If enabling a payor user would breach the limit for master admin payor users the request will be rejected &lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_self(request: web.Request, ) -> web.Response:
    """Get Self

    Get the user&#39;s details 


    """
    return web.Response(status=200)


async def get_user_by_id_v2(request: web.Request, user_id) -> web.Response:
    """Get User

    Get a Single User by Id. 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def invite_user(request: web.Request, body) -> web.Response:
    """Invite a User

    Create a User and invite them to the system 

    :param body: Details of User to invite
    :type body: dict | bytes

    """
    body = InviteUserRequest.from_dict(body)
    return web.Response(status=200)


async def list_users(request: web.Request, type=None, status=None, entity_id=None, payee_type=None, page=None, page_size=None, sort=None) -> web.Response:
    """List Users

    Get a paginated response listing the Users

    :param type: The Type of the User.
    :type type: dict | bytes
    :param status: The status of the User.
    :type status: dict | bytes
    :param entity_id: The entityId of the User.
    :type entity_id: str
    :type entity_id: str
    :param payee_type: The Type of the Payee entity. Either COMPANY or INDIVIDUAL.
    :type payee_type: dict | bytes
    :param page: Page number. Default is 1.
    :type page: int
    :param page_size: The number of results to return in a page
    :type page_size: int
    :param sort: List of sort fields (e.g. ?sort&#x3D;email:asc,lastName:asc) Default is email:asc &#39;name&#39; The supported sort fields are - email, lastNmae. 
    :type sort: str

    """
    type = .from_dict(type)
    status = .from_dict(status)
    payee_type = .from_dict(payee_type)
    return web.Response(status=200)


async def register_sms(request: web.Request, body) -> web.Response:
    """Register SMS Number

    &lt;p&gt;Register an Sms number and send an OTP to it &lt;/p&gt; &lt;p&gt;Used for manual verification of a user &lt;/p&gt; &lt;p&gt;The backoffice user initiates the request to send the OTP to the user&#39;s sms &lt;/p&gt; &lt;p&gt;The user then reads back the OTP which the backoffice user enters in the verifactionCode property for requests that require it&lt;/p&gt; 

    :param body: a SMS Number to send an OTP to
    :type body: dict | bytes

    """
    body = RegisterSmsRequest.from_dict(body)
    return web.Response(status=200)


async def resend_token_0(request: web.Request, user_id, body) -> web.Response:
    """Resend a token

    &lt;p&gt;Resend the specified token &lt;/p&gt; &lt;p&gt;The token to resend must already exist for the user &lt;/p&gt; &lt;p&gt;It will be revoked and a new one issued&lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str
    :param body: The type of token to resend
    :type body: dict | bytes

    """
    body = ResendTokenRequest.from_dict(body)
    return web.Response(status=200)


async def role_update(request: web.Request, user_id, body) -> web.Response:
    """Update User Role

    &lt;p&gt;Update the user&#39;s Role&lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str
    :param body: The Role to change to
    :type body: dict | bytes

    """
    body = RoleUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def unlock_user_v2(request: web.Request, user_id) -> web.Response:
    """Unlock a User

    If a user is locked this endpoint will unlock them 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def unregister_mfa(request: web.Request, user_id, body) -> web.Response:
    """Unregister MFA for the user

    &lt;p&gt;Unregister the MFA device for the user &lt;/p&gt; &lt;p&gt;If the user does not require further verification then a register new MFA device token will be sent to them via their email address&lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str
    :param body: The MFA Type to unregister
    :type body: dict | bytes

    """
    body = UnregisterMFARequest.from_dict(body)
    return web.Response(status=200)


async def unregister_mfa_for_self(request: web.Request, body, authorization=None) -> web.Response:
    """Unregister MFA for Self

    &lt;p&gt;Unregister the MFA device for the user &lt;/p&gt; &lt;p&gt;If the user does not require further verification then a register new MFA device token will be sent to them via their email address&lt;/p&gt; 

    :param body: The MFA Type to unregister
    :type body: dict | bytes
    :param authorization: Bearer token authorization leg of validate
    :type authorization: str

    """
    body = SelfMFATypeUnregisterRequest.from_dict(body)
    return web.Response(status=200)


async def update_password_self(request: web.Request, body) -> web.Response:
    """Update Password for self

    Update password for self 

    :param body: The password
    :type body: dict | bytes

    """
    body = SelfUpdatePasswordRequest.from_dict(body)
    return web.Response(status=200)


async def user_details_update(request: web.Request, user_id, body) -> web.Response:
    """Update User Details

    &lt;p&gt;Update the profile details for the given user&lt;/p&gt; &lt;p&gt;When updating Payor users with the role of payor.master_admin a verificationCode is required&lt;/p&gt; 

    :param user_id: The UUID of the User.
    :type user_id: str
    :type user_id: str
    :param body: The details of the user to update
    :type body: dict | bytes

    """
    body = UserDetailsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def user_details_update_for_self(request: web.Request, body) -> web.Response:
    """Update User Details for self

    &lt;p&gt;Update the profile details for the given user&lt;/p&gt; &lt;p&gt;Only Payee user types are supported&lt;/p&gt; 

    :param body: The details of the user to update
    :type body: dict | bytes

    """
    body = PayeeUserSelfUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def validate_password_self(request: web.Request, body) -> web.Response:
    """Validate the proposed password

    validate the password and return a score 

    :param body: The password
    :type body: dict | bytes

    """
    body = PasswordRequest.from_dict(body)
    return web.Response(status=200)
