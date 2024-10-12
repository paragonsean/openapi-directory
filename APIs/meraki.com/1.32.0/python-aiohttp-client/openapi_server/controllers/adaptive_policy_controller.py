from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_adaptive_policy_acl_request import CreateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.create_organization_adaptive_policy_group_request import CreateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.create_organization_adaptive_policy_policy_request import CreateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.get_organization_adaptive_policy_overview200_response import GetOrganizationAdaptivePolicyOverview200Response
from openapi_server.models.update_organization_adaptive_policy_acl_request import UpdateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.update_organization_adaptive_policy_group_request import UpdateOrganizationAdaptivePolicyGroupRequest
from openapi_server.models.update_organization_adaptive_policy_policy_request import UpdateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.update_organization_adaptive_policy_settings_request import UpdateOrganizationAdaptivePolicySettingsRequest
from openapi_server import util


async def create_organization_adaptive_policy_acl_1(request: web.Request, organization_id, body) -> web.Response:
    """Creates new adaptive policy ACL

    Creates new adaptive policy ACL

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyAclRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_adaptive_policy_group_1(request: web.Request, organization_id, body) -> web.Response:
    """Creates a new adaptive policy group

    Creates a new adaptive policy group

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def create_organization_adaptive_policy_policy_1(request: web.Request, organization_id, body) -> web.Response:
    """Add an Adaptive Policy

    Add an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_adaptive_policy_acl_1(request: web.Request, organization_id, acl_id) -> web.Response:
    """Deletes the specified adaptive policy ACL

    Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str

    """
    return web.Response(status=200)


async def delete_organization_adaptive_policy_group_1(request: web.Request, organization_id, id) -> web.Response:
    """Deletes the specified adaptive policy group and any associated policies and references

    Deletes the specified adaptive policy group and any associated policies and references

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def delete_organization_adaptive_policy_policy_1(request: web.Request, organization_id, id) -> web.Response:
    """Delete an Adaptive Policy

    Delete an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_acl_1(request: web.Request, organization_id, acl_id) -> web.Response:
    """Returns the adaptive policy ACL information

    Returns the adaptive policy ACL information

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_acls_1(request: web.Request, organization_id) -> web.Response:
    """List adaptive policy ACLs in a organization

    List adaptive policy ACLs in a organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_group_1(request: web.Request, organization_id, id) -> web.Response:
    """Returns an adaptive policy group

    Returns an adaptive policy group

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_groups_1(request: web.Request, organization_id) -> web.Response:
    """List adaptive policy groups in a organization

    List adaptive policy groups in a organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_overview_1(request: web.Request, organization_id) -> web.Response:
    """Returns adaptive policy aggregate statistics for an organization

    Returns adaptive policy aggregate statistics for an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_policies_1(request: web.Request, organization_id) -> web.Response:
    """List adaptive policies in an organization

    List adaptive policies in an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_policy_1(request: web.Request, organization_id, id) -> web.Response:
    """Return an adaptive policy

    Return an adaptive policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_settings_1(request: web.Request, organization_id) -> web.Response:
    """Returns global adaptive policy settings in an organization

    Returns global adaptive policy settings in an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_adaptive_policy_acl_1(request: web.Request, organization_id, acl_id, body=None) -> web.Response:
    """Updates an adaptive policy ACL

    Updates an adaptive policy ACL

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyAclRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_group_1(request: web.Request, organization_id, id, body=None) -> web.Response:
    """Updates an adaptive policy group

    Updates an adaptive policy group. If updating \&quot;Infrastructure\&quot;, only the SGT is allowed. Cannot update \&quot;Unknown\&quot;.

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyGroupRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_policy_1(request: web.Request, organization_id, id, body=None) -> web.Response:
    """Update an Adaptive Policy

    Update an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_adaptive_policy_settings_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Update global adaptive policy settings

    Update global adaptive policy settings

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationAdaptivePolicySettingsRequest.from_dict(body)
    return web.Response(status=200)
