from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_resource_member_request_body import AddResourceMemberRequestBody
from openapi_server.models.error import Error
from openapi_server.models.organization import Organization
from openapi_server.models.organizations import Organizations
from openapi_server.models.patch_organization_request import PatchOrganizationRequest
from openapi_server.models.post_organization_request import PostOrganizationRequest
from openapi_server.models.resource_member import ResourceMember
from openapi_server.models.resource_members import ResourceMembers
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server.models.resource_owners import ResourceOwners
from openapi_server.models.secret_keys import SecretKeys
from openapi_server.models.secret_keys_response import SecretKeysResponse
from openapi_server import util


async def delete_orgs_id(request: web.Request, org_id, zap_trace_span=None) -> web.Response:
    """Delete an organization

    

    :param org_id: The ID of the organization to delete.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_orgs_id_members_id(request: web.Request, user_id, org_id, zap_trace_span=None) -> web.Response:
    """Remove a member from an organization

    

    :param user_id: The ID of the member to remove.
    :type user_id: str
    :param org_id: The organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def delete_orgs_id_owners_id(request: web.Request, user_id, org_id, zap_trace_span=None) -> web.Response:
    """Remove an owner from an organization

    

    :param user_id: The ID of the owner to remove.
    :type user_id: str
    :param org_id: The organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_orgs(request: web.Request, zap_trace_span=None, offset=None, limit=None, descending=None, org=None, org_id=None, user_id=None) -> web.Response:
    """List all organizations

    

    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str
    :param offset: 
    :type offset: int
    :param limit: 
    :type limit: int
    :param descending: 
    :type descending: bool
    :param org: Filter organizations to a specific organization name.
    :type org: str
    :param org_id: Filter organizations to a specific organization ID.
    :type org_id: str
    :param user_id: Filter organizations to a specific user ID.
    :type user_id: str

    """
    return web.Response(status=200)


async def get_orgs_id(request: web.Request, org_id, zap_trace_span=None) -> web.Response:
    """Retrieve an organization

    

    :param org_id: The ID of the organization to get.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_orgs_id_members(request: web.Request, org_id, zap_trace_span=None) -> web.Response:
    """List all members of an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_orgs_id_owners(request: web.Request, org_id, zap_trace_span=None) -> web.Response:
    """List all owners of an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def get_orgs_id_secrets_0(request: web.Request, org_id, zap_trace_span=None) -> web.Response:
    """List all secret keys for an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def patch_orgs_id(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Update an organization

    

    :param org_id: The ID of the organization to get.
    :type org_id: str
    :param body: Organization update to apply
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PatchOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def patch_orgs_id_secrets_0(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Update secrets in an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param body: Secret key value pairs to update/add
    :type body: Dict[str, str]
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    return web.Response(status=200)


async def post_orgs(request: web.Request, body, zap_trace_span=None) -> web.Response:
    """Create an organization

    

    :param body: Organization to create
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = PostOrganizationRequest.from_dict(body)
    return web.Response(status=200)


async def post_orgs_id_members(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Add a member to an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param body: User to add as member
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_orgs_id_owners(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Add an owner to an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param body: User to add as owner
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = AddResourceMemberRequestBody.from_dict(body)
    return web.Response(status=200)


async def post_orgs_id_secrets_0(request: web.Request, org_id, body, zap_trace_span=None) -> web.Response:
    """Delete secrets from an organization

    

    :param org_id: The organization ID.
    :type org_id: str
    :param body: Secret key to delete
    :type body: dict | bytes
    :param zap_trace_span: OpenTracing span context
    :type zap_trace_span: str

    """
    body = SecretKeys.from_dict(body)
    return web.Response(status=200)
