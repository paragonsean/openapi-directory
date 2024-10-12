from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_representation import GroupRepresentation
from openapi_server.models.management_permission_reference import ManagementPermissionReference
from openapi_server.models.user_representation import UserRepresentation
from openapi_server import util


async def realm_groups_count_get(request: web.Request, realm, search=None, top=None) -> web.Response:
    """Returns the groups counts.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param search: 
    :type search: str
    :param top: 
    :type top: bool

    """
    return web.Response(status=200)


async def realm_groups_get(request: web.Request, realm, brief_representation=None, first=None, max=None, search=None) -> web.Response:
    """Get group hierarchy.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param brief_representation: 
    :type brief_representation: bool
    :param first: 
    :type first: int
    :param max: 
    :type max: int
    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def realm_groups_id_children_post(request: web.Request, realm, id, body) -> web.Response:
    """Set or create child.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_groups_id_delete(request: web.Request, realm, id) -> web.Response:
    """realm_groups_id_delete

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_get(request: web.Request, realm, id) -> web.Response:
    """realm_groups_id_get

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_management_permissions_get(request: web.Request, realm, id) -> web.Response:
    """Return object stating whether client Authorization permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def realm_groups_id_management_permissions_put(request: web.Request, realm, id, body) -> web.Response:
    """Return object stating whether client Authorization permissions have been initialized or not and a reference

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ManagementPermissionReference.from_dict(body)
    return web.Response(status=200)


async def realm_groups_id_members_get(request: web.Request, realm, id, brief_representation=None, first=None, max=None) -> web.Response:
    """Get users   Returns a list of users, filtered according to query parameters

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param brief_representation: Only return basic information (only guaranteed to return id, username, created, first and last name,  email, enabled state, email verification state, federation link, and access.  Note that it means that namely user attributes, required actions, and not before are not returned.)
    :type brief_representation: bool
    :param first: Pagination offset
    :type first: int
    :param max: Maximum results size (defaults to 100)
    :type max: int

    """
    return web.Response(status=200)


async def realm_groups_id_put(request: web.Request, realm, id, body) -> web.Response:
    """Update group, ignores subgroups.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param id: 
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupRepresentation.from_dict(body)
    return web.Response(status=200)


async def realm_groups_post(request: web.Request, realm, body) -> web.Response:
    """create or add a top level realm groupSet or create child.

    

    :param realm: realm name (not id!)
    :type realm: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupRepresentation.from_dict(body)
    return web.Response(status=200)
