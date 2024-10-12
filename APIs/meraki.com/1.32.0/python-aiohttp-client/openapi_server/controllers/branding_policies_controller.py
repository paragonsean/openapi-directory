from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_branding_policy201_response import CreateOrganizationBrandingPolicy201Response
from openapi_server.models.create_organization_branding_policy_request import CreateOrganizationBrandingPolicyRequest
from openapi_server.models.get_organization_branding_policies200_response_inner import GetOrganizationBrandingPolicies200ResponseInner
from openapi_server.models.get_organization_branding_policies_priorities200_response import GetOrganizationBrandingPoliciesPriorities200Response
from openapi_server.models.update_organization_branding_policies_priorities_request import UpdateOrganizationBrandingPoliciesPrioritiesRequest
from openapi_server.models.update_organization_branding_policy_request import UpdateOrganizationBrandingPolicyRequest
from openapi_server import util


async def create_organization_branding_policy_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Add a new branding policy to an organization

    Add a new branding policy to an organization

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationBrandingPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_branding_policy_1(request: web.Request, organization_id, branding_policy_id) -> web.Response:
    """Delete a branding policy

    Delete a branding policy

    :param organization_id: 
    :type organization_id: str
    :param branding_policy_id: 
    :type branding_policy_id: str

    """
    return web.Response(status=200)


async def get_organization_branding_policies_1(request: web.Request, organization_id) -> web.Response:
    """List the branding policies of an organization

    List the branding policies of an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_branding_policies_priorities_1(request: web.Request, organization_id) -> web.Response:
    """Return the branding policy IDs of an organization in priority order

    Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_branding_policy_1(request: web.Request, organization_id, branding_policy_id) -> web.Response:
    """Return a branding policy

    Return a branding policy

    :param organization_id: 
    :type organization_id: str
    :param branding_policy_id: 
    :type branding_policy_id: str

    """
    return web.Response(status=200)


async def update_organization_branding_policies_priorities_1(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the priority ordering of an organization&#39;s branding policies.

    Update the priority ordering of an organization&#39;s branding policies.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationBrandingPoliciesPrioritiesRequest.from_dict(body)
    return web.Response(status=200)


async def update_organization_branding_policy_1(request: web.Request, organization_id, branding_policy_id, body=None) -> web.Response:
    """Update a branding policy

    Update a branding policy

    :param organization_id: 
    :type organization_id: str
    :param branding_policy_id: 
    :type branding_policy_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationBrandingPolicyRequest.from_dict(body)
    return web.Response(status=200)
