from typing import List, Dict
from aiohttp import web

from openapi_server.models.member import Member
from openapi_server.models.memberresponse import Memberresponse
from openapi_server.models.members import Members
from openapi_server import util


async def create_member(request: web.Request, vestorly_auth, member, access_token=None) -> web.Response:
    """create_member

    Create a new member in the Vestorly Platform

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param member: Member you want to create
    :type member: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    member = Member.from_dict(member)
    return web.Response(status=200)


async def find_member_by_id(request: web.Request, id, vestorly_auth, access_token=None) -> web.Response:
    """find_member_by_id

    Returns a single member

    :param id: Mongo ID of member to fetch
    :type id: str
    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_members(request: web.Request, vestorly_auth, access_token=None, start=None, limit=None) -> web.Response:
    """find_members

    Returns all members

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str
    :param start: Skips number of members from start
    :type start: int
    :param limit: Number of members to return
    :type limit: int

    """
    return web.Response(status=200)


async def update_member_by_id(request: web.Request, id, vestorly_auth, member, access_token=None) -> web.Response:
    """update_member_by_id

    Updates a single member

    :param id: Mongo ID of member to fetch
    :type id: str
    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param member: Member you want to update
    :type member: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    member = Member.from_dict(member)
    return web.Response(status=200)
