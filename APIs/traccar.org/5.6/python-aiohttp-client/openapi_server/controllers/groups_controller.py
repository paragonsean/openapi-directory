from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server import util


async def groups_get(request: web.Request, all=None, user_id=None) -> web.Response:
    """Fetch a list of Groups

    Without any params, returns a list of the Groups the user belongs to

    :param all: Can only be used by admins or managers to fetch all entities
    :type all: bool
    :param user_id: Standard users can use this only with their own _userId_
    :type user_id: int

    """
    return web.Response(status=200)


async def groups_id_delete(request: web.Request, id) -> web.Response:
    """Delete a Group

    

    :param id: 
    :type id: int

    """
    return web.Response(status=200)


async def groups_id_put(request: web.Request, id, body) -> web.Response:
    """Update a Group

    

    :param id: 
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)


async def groups_post(request: web.Request, body) -> web.Response:
    """Create a Group

    

    :param body: 
    :type body: dict | bytes

    """
    body = Group.from_dict(body)
    return web.Response(status=200)
