from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_adaptive_policy_acl_request import CreateOrganizationAdaptivePolicyAclRequest
from openapi_server.models.update_organization_adaptive_policy_acl_request import UpdateOrganizationAdaptivePolicyAclRequest
from openapi_server import util


async def create_organization_adaptive_policy_acl_2(request: web.Request, organization_id, body) -> web.Response:
    """Creates new adaptive policy ACL

    Creates new adaptive policy ACL

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyAclRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_adaptive_policy_acl_2(request: web.Request, organization_id, acl_id) -> web.Response:
    """Deletes the specified adaptive policy ACL

    Deletes the specified adaptive policy ACL. Note this adaptive policy ACL will also be removed from policies using it.

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_acl_2(request: web.Request, organization_id, acl_id) -> web.Response:
    """Returns the adaptive policy ACL information

    Returns the adaptive policy ACL information

    :param organization_id: 
    :type organization_id: str
    :param acl_id: 
    :type acl_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_acls_2(request: web.Request, organization_id) -> web.Response:
    """List adaptive policy ACLs in a organization

    List adaptive policy ACLs in a organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_adaptive_policy_acl_2(request: web.Request, organization_id, acl_id, body=None) -> web.Response:
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
