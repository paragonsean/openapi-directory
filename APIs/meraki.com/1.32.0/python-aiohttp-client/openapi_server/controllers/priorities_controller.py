from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_branding_policies_priorities200_response import GetOrganizationBrandingPoliciesPriorities200Response
from openapi_server.models.update_organization_branding_policies_priorities_request import UpdateOrganizationBrandingPoliciesPrioritiesRequest
from openapi_server import util


async def get_organization_branding_policies_priorities_2(request: web.Request, organization_id) -> web.Response:
    """Return the branding policy IDs of an organization in priority order

    Return the branding policy IDs of an organization in priority order. IDs are ordered in ascending order of priority (IDs later in the array have higher priority).

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def update_organization_branding_policies_priorities_2(request: web.Request, organization_id, body=None) -> web.Response:
    """Update the priority ordering of an organization&#39;s branding policies.

    Update the priority ordering of an organization&#39;s branding policies.

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateOrganizationBrandingPoliciesPrioritiesRequest.from_dict(body)
    return web.Response(status=200)
