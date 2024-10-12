from typing import List, Dict
from aiohttp import web

from openapi_server.models.schema1 import Schema1
from openapi_server.models.schema2 import Schema2
from openapi_server import util


async def create_network_group_1(request: web.Request, owner_id, body=None) -> web.Response:
    """Create Network Group

    Creates a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_network_group_external_peer_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Add external peer

    Adds an external peer to a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def create_network_group_member_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Add member

    Adds a member to a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Schema2.from_dict(body)
    return web.Response(status=200)


async def delete_network_group_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Delete Network Group

    Deletes a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_network_group_external_peer_1(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Remove external peer

    Removes an external peer from a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_network_group_member_1(request: web.Request, owner_id, network_group_id, member_id, body=None) -> web.Response:
    """Remove member

    Removes a member from a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param member_id: Automatically added
    :type member_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_network_group_peer_1(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Remove peer

    Removes a peer from a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Get Network Group

    Gets details of a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_member_1(request: web.Request, owner_id, network_group_id, member_id, body=None) -> web.Response:
    """Get member

    Gets details of a Network Group member.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param member_id: Automatically added
    :type member_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_peer_1(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Get peer

    Gets details of a Network Group peer.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_stream_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """Network Group SSE

    Retrieves the current Network Group details as a Server Sent Event.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_wire_guard_configuration_1(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Get WireGuard® configuration

    Gets the current WireGuard® tunnel configuration file for a Network Group peer.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def get_network_group_wire_guard_configuration_stream_1(request: web.Request, owner_id, network_group_id, peer_id, body=None) -> web.Response:
    """Get WireGuard® configuration

    Gets the current WireGuard® tunnel configuration file for a Network Group peer as a Server Sent Event.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param peer_id: Automatically added
    :type peer_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def list_network_group_members_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """List members

    Lists members in a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def list_network_group_peers_1(request: web.Request, owner_id, network_group_id, body=None) -> web.Response:
    """List peers

    Lists peers in a Network Group.

    :param owner_id: Automatically added
    :type owner_id: str
    :param network_group_id: Automatically added
    :type network_group_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def list_network_groups_1(request: web.Request, owner_id, body=None) -> web.Response:
    """List Network Groups

    Lists Network Groups from an owner.

    :param owner_id: Automatically added
    :type owner_id: str
    :param body: 
    :type body: 

    """
    return web.Response(status=200)
