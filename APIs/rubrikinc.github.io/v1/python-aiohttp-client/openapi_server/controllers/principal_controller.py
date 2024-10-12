from typing import List, Dict
from aiohttp import web

from openapi_server.models.principal_summary_v1_list_response import PrincipalSummaryV1ListResponse
from openapi_server.models.principal_with_role_info import PrincipalWithRoleInfo
from openapi_server.models.role_assignment_request import RoleAssignmentRequest
from openapi_server.models.role_info import RoleInfo
from openapi_server import util


async def assign_roles_to_principals(request: web.Request, body) -> web.Response:
    """Assign roles to principals

    Assign a set of roles to the specified principals.

    :param body: A set of roles and a set of principals to which the roles should be granted. 
    :type body: dict | bytes

    """
    body = RoleAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def get_roles_for_principals(request: web.Request, principals) -> web.Response:
    """Get roles assigned to principals

    Get a list of role information for all roles assigned to the principals. 

    :param principals: IDs of the principals.
    :type principals: List[str]

    """
    return web.Response(status=200)


async def revoke_roles_from_principals(request: web.Request, body) -> web.Response:
    """Revoke roles from principals

    Revoke a set of roles from the specified principals. 

    :param body: A set of roles to revoke from a set of principals.
    :type body: dict | bytes

    """
    body = RoleAssignmentRequest.from_dict(body)
    return web.Response(status=200)


async def search_principals_v1(request: web.Request, limit=None, offset=None, sort_by=None, sort_order=None, auth_domain_id=None, organization_id=None, is_assigned_roles_or_is_local=None, role_id=None, name=None, principal_type=None, is_totp_enabled=None) -> web.Response:
    """Search for principals

    Search for principals based on the specified parameters.

    :param limit: Maximum number of results to return.
    :type limit: int
    :param offset: Starting offset of the results to return.
    :type offset: int
    :param sort_by: Attribute by which to sort. Default is \&quot;name\&quot;.
    :type sort_by: str
    :param sort_order: Sort order. Default order is ascending.
    :type sort_order: str
    :param auth_domain_id: ID of the authentication domain that contains the principal.
    :type auth_domain_id: str
    :param organization_id: ID of the organization of which the principal is a member.
    :type organization_id: str
    :param is_assigned_roles_or_is_local: A Boolean that specifies whether the principal has any roles assigned or is a local user. When a principal is a local user, or when the principal has any roles assigned, this value is &#39;true&#39;. 
    :type is_assigned_roles_or_is_local: bool
    :param role_id: ID of a role assigned to the principal.
    :type role_id: str
    :param name: The name of the principal.
    :type name: str
    :param principal_type: The type of principal.
    :type principal_type: str
    :param is_totp_enabled: Indicates if the principal has TOTP authentication enabled. Returns the users with TOTP authentication enabled when the value is true. 
    :type is_totp_enabled: bool

    """
    return web.Response(status=200)
