from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_payload import AddUserPayload
from openapi_server.models.delete_user_payload import DeleteUserPayload
from openapi_server.models.list_user_response import ListUserResponse
from openapi_server.models.user_teams_response import UserTeamsResponse
from openapi_server.models.v1_user import V1User
from openapi_server import util


async def api_public_v1_user_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """List users

    Get a list of users for your organization  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_user_post(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Add a user

    Add a user to your organization  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddUserPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_user_user_delete(request: web.Request, x_vo_api_id, x_vo_api_key, user, body) -> web.Response:
    """Remove a user

    Remove a user from your organization. If no replacement is specified, an empty JSON payload (\&quot;{}\&quot;) is still required.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user to be deleted
    :type user: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteUserPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_user_user_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Retrieve information for a user

    Get the information for the specified user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user to fetch
    :type user: str

    """
    return web.Response(status=200)


async def api_public_v1_user_user_put(request: web.Request, x_vo_api_id, x_vo_api_key, user, body) -> web.Response:
    """Update a user

    Update the designated user  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user to be updated
    :type user: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddUserPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_user_user_teams_get(request: web.Request, x_vo_api_id, x_vo_api_key, user) -> web.Response:
    """Retrieve the user&#39;s team membership

    This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param user: The VictorOps user
    :type user: str

    """
    return web.Response(status=200)
