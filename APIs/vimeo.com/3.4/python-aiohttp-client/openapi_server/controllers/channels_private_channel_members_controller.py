from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.set_channel_privacy_users_request import SetChannelPrivacyUsersRequest
from openapi_server.models.user import User
from openapi_server import util


async def delete_channel_privacy_user(request: web.Request, channel_id, user_id) -> web.Response:
    """Restrict a user from viewing a private channel

    This method prevents a single user from being able to access the specified private channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_channel_privacy_users(request: web.Request, channel_id, direction=None, page=None, per_page=None) -> web.Response:
    """Get all the users who can view a private channel

    This method gets all the users who have access to the specified private channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)


async def set_channel_privacy_user(request: web.Request, channel_id, user_id) -> web.Response:
    """Permit a specific user to view a private channel

    This method gives a single user access to the specified private channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def set_channel_privacy_users(request: web.Request, channel_id, body) -> web.Response:
    """Permit a list of users to view a private channel

    This method gives multiple users access to the specified private channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = SetChannelPrivacyUsersRequest.from_dict(body)
    return web.Response(status=200)
