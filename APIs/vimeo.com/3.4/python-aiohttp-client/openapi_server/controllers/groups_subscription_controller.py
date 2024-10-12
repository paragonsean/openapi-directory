from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def join_group(request: web.Request, group_id, user_id) -> web.Response:
    """Add a user to a group

    

    :param group_id: The ID of the group.
    :type group_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def join_group_alt1(request: web.Request, group_id) -> web.Response:
    """Add a user to a group

    

    :param group_id: The ID of the group.
    :type group_id: 

    """
    return web.Response(status=200)


async def leave_group(request: web.Request, group_id, user_id) -> web.Response:
    """Remove a user from a group

    

    :param group_id: The ID of the group.
    :type group_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def leave_group_alt1(request: web.Request, group_id) -> web.Response:
    """Remove a user from a group

    

    :param group_id: The ID of the group.
    :type group_id: 

    """
    return web.Response(status=200)
