from typing import List, Dict
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.lti_credentials import LtiCredentials
from openapi_server.models.lti_credentials_creation import LtiCredentialsCreation
from openapi_server.models.organization_invitation import OrganizationInvitation
from openapi_server.models.organization_invitation_creation import OrganizationInvitationCreation
from openapi_server.models.user_admin_update import UserAdminUpdate
from openapi_server.models.user_creation import UserCreation
from openapi_server.models.user_details_admin import UserDetailsAdmin
from openapi_server import util


async def count_orga_users(request: web.Request, role=None, q=None, group=None, no_active_license=None) -> web.Response:
    """Count the organization users using the provided filters

    

    :param role: Filter users by role
    :type role: List[str]
    :param q: The query to search
    :type q: str
    :param group: Filter users by group
    :type group: List[str]
    :param no_active_license: Filter users who don&#39;t have an active license
    :type no_active_license: bool

    """
    return web.Response(status=200)


async def create_lti_credentials(request: web.Request, body) -> web.Response:
    """Create a new couple of LTI 1.x credentials

    Flat for Education is a Certified LTI Provider. You can use these API methods to automate the creation of LTI credentials. You can read more about our LTI implementation, supported components and LTI Endpoints in our [Developer Documentation](https://flat.io/developers/docs/lti/). 

    :param body: 
    :type body: dict | bytes

    """
    body = LtiCredentialsCreation.from_dict(body)
    return web.Response(status=200)


async def create_organization_invitation(request: web.Request, body=None) -> web.Response:
    """Create a new invitation to join the organization

    This method creates and sends invitation for teachers and admins.  Invitations can only be used by new Flat users or users who are not part of the organization yet.  If the email of the user is already associated to a user of your organization, the API will simply update the role of the existing user and won&#39;t send an invitation. In this case, the property &#x60;usedBy&#x60; will be directly filled with the uniquer identifier of the corresponding user. 

    :param body: 
    :type body: dict | bytes

    """
    body = OrganizationInvitationCreation.from_dict(body)
    return web.Response(status=200)


async def create_organization_user(request: web.Request, body=None) -> web.Response:
    """Create a new user account

    

    :param body: 
    :type body: dict | bytes

    """
    body = UserCreation.from_dict(body)
    return web.Response(status=200)


async def list_lti_credentials(request: web.Request, ) -> web.Response:
    """List LTI 1.x credentials

    


    """
    return web.Response(status=200)


async def list_organization_invitations(request: web.Request, role=None, limit=None, next=None, previous=None) -> web.Response:
    """List the organization invitations

    

    :param role: Filter users by role
    :type role: str
    :param limit: This is the maximum number of objects that may be returned
    :type limit: int
    :param next: An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type next: str
    :param previous: An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type previous: str

    """
    return web.Response(status=200)


async def list_organization_users(request: web.Request, sort=None, direction=None, next=None, previous=None, role=None, q=None, group=None, no_active_license=None, license_expiration_date=None, only_ids=None, limit=None) -> web.Response:
    """List the organization users

    

    :param sort: The order to sort the user list
    :type sort: List[str]
    :param direction: Sort direction
    :type direction: str
    :param next: An opaque string cursor to fetch the next page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type next: str
    :param previous: An opaque string cursor to fetch the previous page of data. The paginated API URLs are returned in the &#x60;Link&#x60; header when requesting the API. These URLs will contain a &#x60;next&#x60; and &#x60;previous&#x60; cursor based on the available data. 
    :type previous: str
    :param role: Filter users by role
    :type role: List[str]
    :param q: The query to search
    :type q: str
    :param group: Filter users by group
    :type group: List[str]
    :param no_active_license: Filter users who don&#39;t have an active license
    :type no_active_license: bool
    :param license_expiration_date: Filter users by license expiration date or &#x60;active&#x60; / &#x60;notActive&#x60;
    :type license_expiration_date: List[str]
    :param only_ids: Return only user ids
    :type only_ids: bool
    :param limit: This is the maximum number of objects that may be returned
    :type limit: int

    """
    return web.Response(status=200)


async def remove_organization_invitation(request: web.Request, invitation) -> web.Response:
    """Remove an organization invitation

    

    :param invitation: Unique identifier of the invitation
    :type invitation: str

    """
    return web.Response(status=200)


async def remove_organization_user(request: web.Request, user, convert_to_individual=None) -> web.Response:
    """Remove an account from Flat

    This operation removes an account from Flat and its data, including: * The music scores created by this user (documents, history, comments, collaboration information) * Education related data (assignments and classroom information) 

    :param user: Unique identifier of the Flat account 
    :type user: str
    :param convert_to_individual: If &#x60;true&#x60;, the account will be only removed from the organization and converted into an individual account on our public website, https://flat.io. This operation will remove the education-related data from the account. Before realizing this operation, you need to be sure that the user is at least 13 years old and that this one has read and agreed to the Individual Terms of Services of Flat available on https://flat.io/legal. 
    :type convert_to_individual: bool

    """
    return web.Response(status=200)


async def revoke_lti_credentials(request: web.Request, credentials) -> web.Response:
    """Revoke LTI 1.x credentials

    

    :param credentials: Credentials unique identifier 
    :type credentials: str

    """
    return web.Response(status=200)


async def update_organization_user(request: web.Request, user, body) -> web.Response:
    """Update account information

    

    :param user: Unique identifier of the Flat account 
    :type user: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserAdminUpdate.from_dict(body)
    return web.Response(status=200)
