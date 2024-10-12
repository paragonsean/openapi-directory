from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_credentials import AccountCredentials
from openapi_server.models.api_error import ApiError
from openapi_server.models.change_role_request import ChangeRoleRequest
from openapi_server.models.complete_user_registration_request import CompleteUserRegistrationRequest
from openapi_server.models.organization_user_invitation_list_request import OrganizationUserInvitationListRequest
from openapi_server.models.paginated_response_of_organization import PaginatedResponseOfOrganization
from openapi_server.models.paginated_response_of_role import PaginatedResponseOfRole
from openapi_server.models.paginated_response_of_user_presentation import PaginatedResponseOfUserPresentation
from openapi_server.models.paginated_response_of_user_roles import PaginatedResponseOfUserRoles
from openapi_server.models.paginated_response_ofstring import PaginatedResponseOfstring
from openapi_server.models.password_reset_request import PasswordResetRequest
from openapi_server.models.password_reset_verification_request import PasswordResetVerificationRequest
from openapi_server.models.registration_verification_token_presentation import RegistrationVerificationTokenPresentation
from openapi_server.models.simple_message_response import SimpleMessageResponse
from openapi_server.models.user_presentation import UserPresentation
from openapi_server.models.user_registration_request import UserRegistrationRequest
from openapi_server.models.user_registration_response import UserRegistrationResponse
from openapi_server import util


async def add_user_roles(request: web.Request, organization_id, username, body) -> web.Response:
    """Add role(s) to user

    

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param username: username
    :type username: str
    :param body: changeRoleRequest
    :type body: dict | bytes

    """
    body = ChangeRoleRequest.from_dict(body)
    return web.Response(status=200)


async def complete_registration(request: web.Request, body) -> web.Response:
    """Complete registration

    Completing a registration e.g. for invited users. Finish registration with a username and a password.

    :param body: Contains the verification token, the username and the initial password.
    :type body: dict | bytes

    """
    body = CompleteUserRegistrationRequest.from_dict(body)
    return web.Response(status=200)


async def find_user_by_username(request: web.Request, username) -> web.Response:
    """Find by username

    

    :param username: username
    :type username: str

    """
    return web.Response(status=200)


async def find_users(request: web.Request, username_prefix=None, offset=None, limit=None) -> web.Response:
    """Find users

    

    :param username_prefix: 
    :type username_prefix: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_all_organization_roles(request: web.Request, organization_id, offset=None, limit=None) -> web.Response:
    """List users and their roles

    Listing users and their roles in a paginated manner.

    :param organization_id: organizationId
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_organizations_of_user(request: web.Request, role=None, offset=None, limit=None) -> web.Response:
    """Retrieve organizations of user

    

    :param role: role
    :type role: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_user_roles(request: web.Request, organization_id, username, offset=None, limit=None) -> web.Response:
    """Get user roles by username

    

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param username: username
    :type username: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_users_of_organization(request: web.Request, organization_id, offset=None, limit=None) -> web.Response:
    """Find users in organization

    Finding users in the specified organization in a paginated manner.

    :param organization_id: organizationId
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def invite_users(request: web.Request, organization_id, body) -> web.Response:
    """Invite Users

    

    :param organization_id: The namespace of the organization where users should be invited
    :type organization_id: str
    :param body: invitationList
    :type body: dict | bytes

    """
    body = OrganizationUserInvitationListRequest.from_dict(body)
    return web.Response(status=200)


async def list_all_roles(request: web.Request, privilege=None, offset=None, limit=None) -> web.Response:
    """List roles

    Listing of roles.

    :param privilege: If specified the roles will be filtered containing that privilege.
    :type privilege: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def login(request: web.Request, body) -> web.Response:
    """login

    ID4i API Login

    :param body: 
    :type body: dict | bytes

    """
    body = AccountCredentials.from_dict(body)
    return web.Response(status=200)


async def register_user(request: web.Request, body) -> web.Response:
    """Register user

    Registering a new user.

    :param body: The user information about the new created user.
    :type body: dict | bytes

    """
    body = UserRegistrationRequest.from_dict(body)
    return web.Response(status=200)


async def remove_user_roles(request: web.Request, organization_id, username, body) -> web.Response:
    """Remove role(s) from user

    

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param username: username
    :type username: str
    :param body: changeRoleRequest
    :type body: dict | bytes

    """
    body = ChangeRoleRequest.from_dict(body)
    return web.Response(status=200)


async def request_password_reset(request: web.Request, body) -> web.Response:
    """Request password reset

    Requesting a reset for a new password. 

    :param body: Contains the required information to request a new password.
    :type body: dict | bytes

    """
    body = PasswordResetRequest.from_dict(body)
    return web.Response(status=200)


async def verify_password_reset(request: web.Request, body) -> web.Response:
    """Verify password reset

    Setting a new password and verifying the request to set the password.

    :param body: Contains the new password and the verification token to set the new password.
    :type body: dict | bytes

    """
    body = PasswordResetVerificationRequest.from_dict(body)
    return web.Response(status=200)


async def verify_user_registration(request: web.Request, body) -> web.Response:
    """Verify registration

    Verifies a new user registration.

    :param body: The token for user verification.
    :type body: dict | bytes

    """
    body = RegistrationVerificationTokenPresentation.from_dict(body)
    return web.Response(status=200)
