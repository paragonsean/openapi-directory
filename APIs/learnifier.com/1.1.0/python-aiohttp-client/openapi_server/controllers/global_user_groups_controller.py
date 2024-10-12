from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.global_user_group import GlobalUserGroup
from openapi_server.models.user import User
from openapi_server import util


async def globalusergroups_get(request: web.Request, ) -> web.Response:
    """List Global User Groups.

    Returns a list of Global User Groups. Global User Groups are set up for the realm, and will generate groups that can be used on the client level. 


    """
    return web.Response(status=200)


async def globalusergroups_groupid_members_get(request: web.Request, groupid) -> web.Response:
    """List of all users in group.

    Returns a list of all members in User Groups that are based on the Global Group with this groupid. 

    :param groupid: ID of group
    :type groupid: int

    """
    return web.Response(status=200)
