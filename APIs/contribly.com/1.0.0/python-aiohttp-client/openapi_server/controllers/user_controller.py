from typing import List, Dict
from aiohttp import web

from openapi_server.models.linked_profile import LinkedProfile
from openapi_server.models.user import User
from openapi_server import util


async def users_get(request: web.Request, assignment=None, country=None, minimum_contributions=None, linked_profile=None, owned_by=None, submitted_before=None, submitted_after=None, username=None) -> web.Response:
    """List users

    

    :param assignment: Restrict results to the users who have contributed to this assignment.
    :type assignment: str
    :param country: Restrict results to the users who have submitted a contribution with a public location located within this country.
    :type country: str
    :param minimum_contributions: Restrict results to the users who have submitted at least this many contributions.
    :type minimum_contributions: 
    :param linked_profile: Restrict results to the users who a linked profile of this type.
    :type linked_profile: str
    :param owned_by: Restrict results to the users who are owned by of this owner.
    :type owned_by: str
    :param submitted_before: Limit results to users who have submitted at least one contribution before this date time.
    :type submitted_before: str
    :param submitted_after: Limit results to users who have submitted at least one contribution after this date time.
    :type submitted_after: str
    :param username: Restrict results to the user with this username.
    :type username: str

    """
    submitted_before = util.deserialize_datetime(submitted_before)
    submitted_after = util.deserialize_datetime(submitted_after)
    return web.Response(status=200)


async def users_id_get(request: web.Request, id) -> web.Response:
    """Retrieve a single user by id

    

    :param id: Id of the user to return
    :type id: str

    """
    return web.Response(status=200)


async def users_id_linked_type_get(request: web.Request, id, type) -> web.Response:
    """Retrieve a users linked profile by type

    

    :param id: Id of the user to return
    :type id: str
    :param type: Type of the linked profile to fetch
    :type type: str

    """
    return web.Response(status=200)
