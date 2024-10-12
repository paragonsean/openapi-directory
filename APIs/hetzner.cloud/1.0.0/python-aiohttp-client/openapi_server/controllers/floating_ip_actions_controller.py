from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.assign_floating_ip_request import AssignFloatingIPRequest
from openapi_server.models.change_dnsptr_request import ChangeDNSPTRRequest
from openapi_server.models.change_protection_request import ChangeProtectionRequest
from openapi_server.models.floating_ips_id_actions_get200_response import FloatingIpsIdActionsGet200Response
from openapi_server import util


async def floating_ips_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Floating IP

    Returns a specific Action object for a Floating IP.

    :param id: ID of the Floating IP
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def floating_ips_id_actions_assign_post(request: web.Request, id, body=None) -> web.Response:
    """Assign a Floating IP to a Server

    Assigns a Floating IP to a Server.

    :param id: ID of the Floating IP
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AssignFloatingIPRequest.from_dict(body)
    return web.Response(status=200)


async def floating_ips_id_actions_change_dns_ptr_post(request: web.Request, id, body=None) -> web.Response:
    """Change reverse DNS entry for a Floating IP

    Changes the hostname that will appear when getting the hostname belonging to this Floating IP.

    :param id: ID of the Floating IP
    :type id: int
    :param body: Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. For a Floating IP of type &#x60;ipv4&#x60; this must exactly match the IP address of the Floating IP. For a Floating IP of type &#x60;ipv6&#x60; this must be a single IP within the IPv6 /64 range that belongs to this Floating IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing &#x60;dns_ptr&#x60;. 
    :type body: dict | bytes

    """
    body = ChangeDNSPTRRequest.from_dict(body)
    return web.Response(status=200)


async def floating_ips_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Floating IP Protection

    Changes the protection configuration of the Floating IP.

    :param id: ID of the Floating IP
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeProtectionRequest.from_dict(body)
    return web.Response(status=200)


async def floating_ips_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Floating IP

    Returns all Action objects for a Floating IP. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Floating IP
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)


async def floating_ips_id_actions_unassign_post(request: web.Request, id) -> web.Response:
    """Unassign a Floating IP

    Unassigns a Floating IP, resulting in it being unreachable. You may assign it to a Server again at a later time.

    :param id: ID of the Floating IP
    :type id: int

    """
    return web.Response(status=200)
