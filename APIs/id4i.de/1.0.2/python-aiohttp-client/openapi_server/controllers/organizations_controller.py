from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_partner_request import AddPartnerRequest
from openapi_server.models.api_error import ApiError
from openapi_server.models.change_role_request import ChangeRoleRequest
from openapi_server.models.organization import Organization
from openapi_server.models.organization_address import OrganizationAddress
from openapi_server.models.organization_update import OrganizationUpdate
from openapi_server.models.organization_user_invitation_list_request import OrganizationUserInvitationListRequest
from openapi_server.models.paginated_response_of_country import PaginatedResponseOfCountry
from openapi_server.models.paginated_response_of_guid_collection import PaginatedResponseOfGuidCollection
from openapi_server.models.paginated_response_of_organization import PaginatedResponseOfOrganization
from openapi_server.models.paginated_response_of_partner_organization import PaginatedResponseOfPartnerOrganization
from openapi_server.models.paginated_response_of_user_presentation import PaginatedResponseOfUserPresentation
from openapi_server.models.paginated_response_of_user_roles import PaginatedResponseOfUserRoles
from openapi_server.models.paginated_response_ofstring import PaginatedResponseOfstring
from openapi_server.models.public_image_presentation import PublicImagePresentation
from openapi_server.models.remove_partner_request import RemovePartnerRequest
from openapi_server import util


async def add_partner_organization(request: web.Request, organization_id, body) -> web.Response:
    """Add partner

    Adding a partner organization. If the given organization is already a partner the result will be state 200 too.

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param body: request
    :type body: dict | bytes

    """
    body = AddPartnerRequest.from_dict(body)
    return web.Response(status=200)


async def add_user_roles_0(request: web.Request, organization_id, username, body) -> web.Response:
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


async def create_organization(request: web.Request, body) -> web.Response:
    """Create organization

    Creating a new organization.

    :param body: Organization to be created
    :type body: dict | bytes

    """
    body = Organization.from_dict(body)
    return web.Response(status=200)


async def delete_organization(request: web.Request, organization_id) -> web.Response:
    """Delete organization

    

    :param organization_id: The namespace of the organization to be deleted.
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_organization_billing_address(request: web.Request, organization_id) -> web.Response:
    """Remove billing address

    

    :param organization_id: organizationId
    :type organization_id: str

    """
    return web.Response(status=200)


async def delete_organization_logo(request: web.Request, organization_id) -> web.Response:
    """Delete organization logo

    

    :param organization_id: The namespace of the organization where the logo should be deleted.
    :type organization_id: str

    """
    return web.Response(status=200)


async def find_organization(request: web.Request, organization_id) -> web.Response:
    """Find organization by id/namespace

    Returns a single organization.

    :param organization_id: The namespace of the organization to be retrieved.
    :type organization_id: str

    """
    return web.Response(status=200)


async def find_organization_address(request: web.Request, organization_id) -> web.Response:
    """Retrieve address

    

    :param organization_id: organizationId
    :type organization_id: str

    """
    return web.Response(status=200)


async def find_organization_billing_address(request: web.Request, organization_id) -> web.Response:
    """Retrieve billing address

    

    :param organization_id: organizationId
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_all_collections_of_organization_0(request: web.Request, organization_id, offset=None, limit=None, type=None, label=None, label_prefix=None, _property=None) -> web.Response:
    """Get collections of organization

    Retrieving all collections of an organization in a paginated manner. You may filter the results by specifying id4n properties with filter operations (eq, in, ne) in the query parameters. e.g. &#x60;com.yourcompany.orderId.eq&#x3D;1234&#x60;  

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int
    :param type: Filter by this type
    :type type: str
    :param label: Filter by this label
    :type label: str
    :param label_prefix: Filter by this label prefix
    :type label_prefix: str
    :param _property: List of i4dn property filter. e.g. \&quot;com.myorga.state:IN:waiting|processing\&quot; or \&quot;com.myorga.orderId:EQ:SAP001\&quot;
    :type _property: List[str]

    """
    return web.Response(status=200)


async def get_all_organization_roles_0(request: web.Request, organization_id, offset=None, limit=None) -> web.Response:
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


async def get_organization_privileges(request: web.Request, organization_id) -> web.Response:
    """List my privileges

    Listing all privileges of the current user/APIKey of the specified organization.

    :param organization_id: The namespace of the organization
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organizations_of_user_0(request: web.Request, role=None, offset=None, limit=None) -> web.Response:
    """Retrieve organizations of user

    

    :param role: role
    :type role: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_partner_organizations(request: web.Request, organization_id, offset=None, limit=None) -> web.Response:
    """Get partners of an organization

    Listing partners in a paginated manner.

    :param organization_id: The namespace of the organization to query partner organizations
    :type organization_id: str
    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def get_user_roles_0(request: web.Request, organization_id, username, offset=None, limit=None) -> web.Response:
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


async def get_users_of_organization_0(request: web.Request, organization_id, offset=None, limit=None) -> web.Response:
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


async def invite_users_0(request: web.Request, organization_id, body) -> web.Response:
    """Invite Users

    

    :param organization_id: The namespace of the organization where users should be invited
    :type organization_id: str
    :param body: invitationList
    :type body: dict | bytes

    """
    body = OrganizationUserInvitationListRequest.from_dict(body)
    return web.Response(status=200)


async def list_countries(request: web.Request, offset=None, limit=None) -> web.Response:
    """List countries

    

    :param offset: Start with the n-th element
    :type offset: int
    :param limit: The maximum count of returned elements
    :type limit: int

    """
    return web.Response(status=200)


async def remove_partner_organization(request: web.Request, organization_id, body) -> web.Response:
    """Remove partner

    Removing a partner organization

    :param organization_id: The namespace of the organization
    :type organization_id: str
    :param body: request
    :type body: dict | bytes

    """
    body = RemovePartnerRequest.from_dict(body)
    return web.Response(status=200)


async def remove_user_roles_0(request: web.Request, organization_id, username, body) -> web.Response:
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


async def set_organization_logo(request: web.Request, organization_id, file) -> web.Response:
    """Update organization logo

    Updating an organization logo using a multipart file upload.

    :param organization_id: The namespace of the organization where the logo should be updated.
    :type organization_id: str
    :param file: An image containing the new logo.
    :type file: str

    """
    return web.Response(status=200)


async def update_organization(request: web.Request, organization_id, body) -> web.Response:
    """Update organization

    

    :param organization_id: The namespace of the organization to be updated.
    :type organization_id: str
    :param body: Updated organization object
    :type body: dict | bytes

    """
    body = OrganizationUpdate.from_dict(body)
    return web.Response(status=200)


async def update_organization_address(request: web.Request, organization_id, body) -> web.Response:
    """Store address

    

    :param organization_id: organizationId
    :type organization_id: str
    :param body: addressResource
    :type body: dict | bytes

    """
    body = OrganizationAddress.from_dict(body)
    return web.Response(status=200)


async def update_organization_billing_address(request: web.Request, organization_id, body) -> web.Response:
    """Store billing address

    

    :param organization_id: organizationId
    :type organization_id: str
    :param body: addressResource
    :type body: dict | bytes

    """
    body = OrganizationAddress.from_dict(body)
    return web.Response(status=200)
