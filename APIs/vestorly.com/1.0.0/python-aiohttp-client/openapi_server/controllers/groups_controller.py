from typing import List, Dict
from aiohttp import web

from openapi_server.models.group_input import GroupInput
from openapi_server.models.groupresponse import Groupresponse
from openapi_server.models.groups import Groups
from openapi_server import util


async def create_group(request: web.Request, vestorly_auth, group, access_token=None) -> web.Response:
    """create_group

    Creates a new Group

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param group: Group to add
    :type group: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    group = GroupInput.from_dict(group)
    return web.Response(status=200)


async def delete_group(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """delete_group

    Deletes a Group

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of group to delete
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_group_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """find_group_by_id

    Returns a single group if user has access

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Mongo ID of group to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_groups(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_groups

    Returns all groups

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_group_by_id(request: web.Request, vestorly_auth, id, group, access_token=None) -> web.Response:
    """update_group_by_id

    Updates a Group

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of group to update
    :type id: str
    :param group: Group to update
    :type group: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    group = GroupInput.from_dict(group)
    return web.Response(status=200)
