from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.follow_users_alt1_request import FollowUsersAlt1Request
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User
from openapi_server import util


async def check_if_user_is_following(request: web.Request, follow_user_id, user_id) -> web.Response:
    """Check if a user is following another user

    

    :param follow_user_id: The ID of the following user.
    :type follow_user_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def check_if_user_is_following_alt1(request: web.Request, follow_user_id) -> web.Response:
    """Check if a user is following another user

    

    :param follow_user_id: The ID of the following user.
    :type follow_user_id: 

    """
    return web.Response(status=200)


async def follow_user(request: web.Request, follow_user_id, user_id) -> web.Response:
    """Follow a specific user

    

    :param follow_user_id: The ID of the following user.
    :type follow_user_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def follow_user_alt1(request: web.Request, follow_user_id) -> web.Response:
    """Follow a specific user

    

    :param follow_user_id: The ID of the following user.
    :type follow_user_id: 

    """
    return web.Response(status=200)


async def follow_users(request: web.Request, user_id, body) -> web.Response:
    """Follow a list of users

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = FollowUsersAlt1Request.from_dict(body)
    return web.Response(status=200)


async def follow_users_alt1(request: web.Request, body) -> web.Response:
    """Follow a list of users

    

    :param body: 
    :type body: dict | bytes

    """
    body = FollowUsersAlt1Request.from_dict(body)
    return web.Response(status=200)


async def get_followers(request: web.Request, user_id, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the followers of a user

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_followers_alt1(request: web.Request, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the followers of a user

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_user_following(request: web.Request, user_id, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the users that a user is following

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_user_following_alt1(request: web.Request, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the users that a user is following

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def unfollow_user(request: web.Request, follow_user_id, user_id) -> web.Response:
    """Unfollow a user

    

    :param follow_user_id: The ID of the following user.
    :type follow_user_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def unfollow_user_alt1(request: web.Request, follow_user_id) -> web.Response:
    """Unfollow a user

    

    :param follow_user_id: The ID of the following user.
    :type follow_user_id: 

    """
    return web.Response(status=200)
