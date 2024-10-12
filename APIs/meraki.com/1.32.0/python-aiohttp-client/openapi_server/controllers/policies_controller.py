from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_adaptive_policy_policy_request import CreateOrganizationAdaptivePolicyPolicyRequest
from openapi_server.models.get_network_policies_by_client200_response_inner import GetNetworkPoliciesByClient200ResponseInner
from openapi_server.models.update_organization_adaptive_policy_policy_request import UpdateOrganizationAdaptivePolicyPolicyRequest
from openapi_server import util


async def create_organization_adaptive_policy_policy_2(request: web.Request, organization_id, body) -> web.Response:
    """Add an Adaptive Policy

    Add an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateOrganizationAdaptivePolicyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_organization_adaptive_policy_policy_2(request: web.Request, organization_id, id) -> web.Response:
    """Delete an Adaptive Policy

    Delete an Adaptive Policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def get_network_policies_by_client_1(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None, t0=None, timespan=None) -> web.Response:
    """Get policies for all clients with policies

    Get policies for all clients with policies

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 50.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    :type t0: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameter t0. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    :type timespan: float

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_policies_2(request: web.Request, organization_id) -> web.Response:
    """List adaptive policies in an organization

    List adaptive policies in an organization

    :param organization_id: 
    :type organization_id: str

    """
    return web.Response(status=200)


async def get_organization_adaptive_policy_policy_2(request: web.Request, organization_id, id) -> web.Response:
    """Return an adaptive policy

    Return an adaptive policy

    :param organization_id: 
    :type organization_id: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def update_organization_adaptive_policy_policy_2(request: web.Request, organization_id, id, body=None) -> web.Response:
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
