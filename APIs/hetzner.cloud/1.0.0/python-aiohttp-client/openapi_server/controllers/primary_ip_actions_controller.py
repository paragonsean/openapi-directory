from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.assign_primary_ip_request import AssignPrimaryIPRequest
from openapi_server.models.change_dnsptr_request import ChangeDNSPTRRequest
from openapi_server.models.change_protection_request2 import ChangeProtectionRequest2
from openapi_server import util


async def primary_ips_id_actions_assign_post(request: web.Request, id, body=None) -> web.Response:
    """Assign a Primary IP to a resource

    Assigns a Primary IP to a Server.  A Server can only have one Primary IP of type &#x60;ipv4&#x60; and one of type &#x60;ipv6&#x60; assigned. If you need more IPs use Floating IPs.  The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed.  #### Call specific error codes  | Code                          | Description                                                   | |------------------------------ |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;          | The server is running, but needs to be powered off            | | &#x60;primary_ip_already_assigned&#x60; | Primary ip is already assigned to a different server          | | &#x60;server_has_ipv4&#x60;             | The server already has an ipv4 address                        | | &#x60;server_has_ipv6&#x60;             | The server already has an ipv6 address                        | 

    :param id: ID of the Primary IP
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AssignPrimaryIPRequest.from_dict(body)
    return web.Response(status=200)


async def primary_ips_id_actions_change_dns_ptr_post(request: web.Request, id, body=None) -> web.Response:
    """Change reverse DNS entry for a Primary IP

    Changes the hostname that will appear when getting the hostname belonging to this Primary IP.

    :param id: ID of the Primary IP
    :type id: int
    :param body: Select the IP address for which to change the DNS entry by passing &#x60;ip&#x60;. For a Primary IP of type &#x60;ipv4&#x60; this must exactly match the IP address of the Primary IP. For a Primary IP of type &#x60;ipv6&#x60; this must be a single IP within the IPv6 /64 range that belongs to this Primary IP. You can add up to 100 IPv6 reverse DNS entries.  The target hostname is set by passing &#x60;dns_ptr&#x60;. 
    :type body: dict | bytes

    """
    body = ChangeDNSPTRRequest.from_dict(body)
    return web.Response(status=200)


async def primary_ips_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Primary IP Protection

    Changes the protection configuration of a Primary IP.  A Primary IP can only be delete protected if its &#x60;auto_delete&#x60; property is set to &#x60;false&#x60;. 

    :param id: ID of the Primary IP
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeProtectionRequest2.from_dict(body)
    return web.Response(status=200)


async def primary_ips_id_actions_unassign_post(request: web.Request, id) -> web.Response:
    """Unassign a Primary IP from a resource

    Unassigns a Primary IP from a Server.  The Server must be powered off (status &#x60;off&#x60;) in order for this operation to succeed.  Note that only Servers that have at least one network interface (public or private) attached can be powered on.  #### Call specific error codes  | Code                              | Description                                                   | |---------------------------------- |-------------------------------------------------------------- | | &#x60;server_not_stopped&#x60;              | The server is running, but needs to be powered off            | | &#x60;server_is_load_balancer_target&#x60;  | The server ipv4 address is a loadbalancer target              | 

    :param id: ID of the Primary IP
    :type id: int

    """
    return web.Response(status=200)
