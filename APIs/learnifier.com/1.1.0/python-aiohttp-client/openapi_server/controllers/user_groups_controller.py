from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_group import AddUserGroup
from openapi_server.models.add_user_group_member import AddUserGroupMember
from openapi_server.models.error import Error
from openapi_server.models.group_id import GroupId
from openapi_server.models.user import User
from openapi_server.models.user_group import UserGroup
from openapi_server.models.user_id import UserId
from openapi_server import util


async def orgunits_orgid_usergroups_get(request: web.Request, orgid) -> web.Response:
    """List User Groups.

    Returns a list of User Groups for the org unit. 

    :param orgid: ID of organization
    :type orgid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_usergroups_groupid_get(request: web.Request, orgid, groupid) -> web.Response:
    """Get user group

    Returns single User Group. 

    :param orgid: ID of organization
    :type orgid: int
    :param groupid: ID of group
    :type groupid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_usergroups_groupid_members_get(request: web.Request, orgid, groupid) -> web.Response:
    """List of all users in group.

    Returns a list of all members in User Groups that are based on the Global Group with this groupid. 

    :param orgid: ID of organization
    :type orgid: int
    :param groupid: ID of group
    :type groupid: int

    """
    return web.Response(status=200)


async def orgunits_orgid_usergroups_groupid_members_post(request: web.Request, orgid, groupid, body) -> web.Response:
    """Add user group member.

    Adds a user to user group. 

    :param orgid: ID of organization
    :type orgid: int
    :param groupid: ID of group
    :type groupid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddUserGroupMember.from_dict(body)
    return web.Response(status=200)


async def orgunits_orgid_usergroups_groupid_members_uuid_delete(request: web.Request, orgid, groupid, uuid) -> web.Response:
    """Remove user group member.

    Removes a user from a user group. 

    :param orgid: ID of organization
    :type orgid: int
    :param groupid: ID of group
    :type groupid: int
    :param uuid: UUID of user to remove from group.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def orgunits_orgid_usergroups_post(request: web.Request, orgid, body) -> web.Response:
    """Create a User Group.

    Create a User Group. 

    :param orgid: ID of organization
    :type orgid: int
    :param body: 
    :type body: dict | bytes

    """
    body = AddUserGroup.from_dict(body)
    return web.Response(status=200)
