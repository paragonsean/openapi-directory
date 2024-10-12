from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user import AddUser
from openapi_server.models.add_user_response import AddUserResponse
from openapi_server.models.error import Error
from openapi_server.models.participation import Participation
from openapi_server.models.user import User
from openapi_server.models.user_participation_info import UserParticipationInfo
from openapi_server.models.user_with_permissions import UserWithPermissions
from openapi_server import util


async def extparticipation_get(request: web.Request, extid) -> web.Response:
    """Gets a participation by external id

    Gets a participation by external id.

    :param extid: The external id of the participation
    :type extid: str

    """
    return web.Response(status=200)


async def extuser_get(request: web.Request, extid) -> web.Response:
    """Gets a user by external id

    Gets a user by external id.

    :param extid: The external id of the user
    :type extid: str

    """
    return web.Response(status=200)


async def users_get(request: web.Request, limit=None, offset=None) -> web.Response:
    """Lists all users

    Lists all users. Only api callers that have full access can call this method.

    :param limit: The maximum number of users to return
    :type limit: int
    :param offset: The offset to start listing users from
    :type offset: int

    """
    return web.Response(status=200)


async def users_post(request: web.Request, body) -> web.Response:
    """Adds a user

    Adds a user. No two users can have the same email address. Email is saved WITH case but compared regardless of case. Email can be changed for a user assuming it doesn&#39;t cause a conflict.

    :param body: 
    :type body: dict | bytes

    """
    body = AddUser.from_dict(body)
    return web.Response(status=200)


async def users_userid_get(request: web.Request, userid) -> web.Response:
    """User information

    Returns information about a user 

    :param userid: A user id
    :type userid: str

    """
    return web.Response(status=200)


async def users_userid_patch(request: web.Request, userid, body) -> web.Response:
    """Updates user information

    Updates a user. All values that have a key defined in the input will be set. So if a value should not be updated omit it totally from the input, otherwise it will be unset.

    :param userid: The user id
    :type userid: str
    :type userid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddUser.from_dict(body)
    return web.Response(status=200)


async def users_userid_pickey_apikeyget(request: web.Request, userid, apikey) -> web.Response:
    """User profile picture

    Returns a thumbnail picture of the user. This can either be a selected picture or an auto generated image. This method doesn&#39;t require a full sign in. The api key is sufficient. The image is square and is likely, but not necessary, to be in 128x128 PNG format. However the format will always be either PNG, JPEG or GIF. 

    :param userid: The user id
    :type userid: str
    :param apikey: 
    :type apikey: str

    """
    return web.Response(status=200)


async def users_userid_project_participations_get(request: web.Request, userid) -> web.Response:
    """Returns information about the projects the user is a participant in.

    Returns information about the projects the user is a participant in. Only the projects that the current token have access to will be listed. 

    :param userid: A user id
    :type userid: str
    :type userid: str

    """
    return web.Response(status=200)
