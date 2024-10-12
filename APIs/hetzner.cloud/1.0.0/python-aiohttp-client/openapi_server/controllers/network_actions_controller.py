from typing import List, Dict
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.add_delete_route_request import AddDeleteRouteRequest
from openapi_server.models.add_subnet_request import AddSubnetRequest
from openapi_server.models.change_ip_range_request import ChangeIPRangeRequest
from openapi_server.models.change_protection_request1 import ChangeProtectionRequest1
from openapi_server.models.delete_subnet_request import DeleteSubnetRequest
from openapi_server import util


async def networks_id_actions_action_id_get(request: web.Request, id, action_id) -> web.Response:
    """Get an Action for a Network

    Returns a specific Action for a Network.

    :param id: ID of the Network
    :type id: int
    :param action_id: ID of the Action
    :type action_id: int

    """
    return web.Response(status=200)


async def networks_id_actions_add_route_post(request: web.Request, id, body=None) -> web.Response:
    """Add a route to a Network

    Adds a route entry to a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddDeleteRouteRequest.from_dict(body)
    return web.Response(status=200)


async def networks_id_actions_add_subnet_post(request: web.Request, id, body=None) -> web.Response:
    """Add a subnet to a Network

    Adds a new subnet object to the Network. If you do not specify an &#x60;ip_range&#x60; for the subnet we will automatically pick the first available /24 range for you if possible.  Note: if the parent Network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddSubnetRequest.from_dict(body)
    return web.Response(status=200)


async def networks_id_actions_change_ip_range_post(request: web.Request, id, body=None) -> web.Response:
    """Change IP range of a Network

    Changes the IP range of a Network. IP ranges can only be extended and never shrunk. You can only add IPs at the end of an existing IP range. This means that the IP part of your existing range must stay the same and you can only change its netmask.  For example if you have a range &#x60;10.0.0.0/16&#x60; you want to extend then your new range must also start with the IP &#x60;10.0.0.0&#x60;. Your CIDR netmask &#x60;/16&#x60; may change to a number that is smaller than &#x60;16&#x60; thereby increasing the IP range. So valid entries would be &#x60;10.0.0.0/15&#x60;, &#x60;10.0.0.0/14&#x60;, &#x60;10.0.0.0/13&#x60; and so on.  After changing the IP range you will have to adjust the routes on your connected Servers by either rebooting them or manually changing the routes to your private Network interface.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeIPRangeRequest.from_dict(body)
    return web.Response(status=200)


async def networks_id_actions_change_protection_post(request: web.Request, id, body=None) -> web.Response:
    """Change Network Protection

    Changes the protection configuration of a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ChangeProtectionRequest1.from_dict(body)
    return web.Response(status=200)


async def networks_id_actions_delete_route_post(request: web.Request, id, body=None) -> web.Response:
    """Delete a route from a Network

    Delete a route entry from a Network.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddDeleteRouteRequest.from_dict(body)
    return web.Response(status=200)


async def networks_id_actions_delete_subnet_post(request: web.Request, id, body=None) -> web.Response:
    """Delete a subnet from a Network

    Deletes a single subnet entry from a Network. You cannot delete subnets which still have Servers attached. If you have Servers attached you first need to detach all Servers that use IPs from this subnet before you can delete the subnet.  Note: if the Network object changes during the request, the response will be a “conflict” error. 

    :param id: ID of the Network
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteSubnetRequest.from_dict(body)
    return web.Response(status=200)


async def networks_id_actions_get(request: web.Request, id, sort=None, status=None) -> web.Response:
    """Get all Actions for a Network

    Returns all Action objects for a Network. You can sort the results by using the &#x60;sort&#x60; URI parameter, and filter them with the &#x60;status&#x60; parameter.

    :param id: ID of the Network
    :type id: int
    :param sort: Can be used multiple times.
    :type sort: str
    :param status: Can be used multiple times, the response will contain only Actions with specified statuses
    :type status: str

    """
    return web.Response(status=200)
