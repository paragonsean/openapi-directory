from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_switch_access_policy_request import CreateNetworkSwitchAccessPolicyRequest
from openapi_server.models.get_network_switch_access_policies200_response_inner import GetNetworkSwitchAccessPolicies200ResponseInner
from openapi_server.models.update_network_switch_access_policy_request import UpdateNetworkSwitchAccessPolicyRequest
from openapi_server import util


async def create_network_switch_access_policy_1(request: web.Request, network_id, body) -> web.Response:
    """Create an access policy for a switch network

    Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkSwitchAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_switch_access_policy_1(request: web.Request, network_id, access_policy_number) -> web.Response:
    """Delete an access policy for a switch network

    Delete an access policy for a switch network

    :param network_id: 
    :type network_id: str
    :param access_policy_number: 
    :type access_policy_number: str

    """
    return web.Response(status=200)


async def get_network_switch_access_policies_1(request: web.Request, network_id) -> web.Response:
    """List the access policies for a switch network

    List the access policies for a switch network. Only returns access policies with &#39;my RADIUS server&#39; as authentication method

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def get_network_switch_access_policy_1(request: web.Request, network_id, access_policy_number) -> web.Response:
    """Return a specific access policy for a switch network

    Return a specific access policy for a switch network

    :param network_id: 
    :type network_id: str
    :param access_policy_number: 
    :type access_policy_number: str

    """
    return web.Response(status=200)


async def update_network_switch_access_policy_1(request: web.Request, network_id, access_policy_number, body=None) -> web.Response:
    """Update an access policy for a switch network

    Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

    :param network_id: 
    :type network_id: str
    :param access_policy_number: 
    :type access_policy_number: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkSwitchAccessPolicyRequest.from_dict(body)
    return web.Response(status=200)
