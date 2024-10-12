from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User
from openapi_server import util


async def check_if_user_joined_group(request: web.Request, group_id, user_id) -> web.Response:
    """Check if a user has joined a group

    

    :param group_id: The ID of the group.
    :type group_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def check_if_user_joined_group_alt1(request: web.Request, group_id) -> web.Response:
    """Check if a user has joined a group

    

    :param group_id: The ID of the group.
    :type group_id: 

    """
    return web.Response(status=200)


async def get_group_members(request: web.Request, group_id, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the members of a group

    

    :param group_id: The ID of the group.
    :type group_id: 
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


async def get_user_groups(request: web.Request, user_id, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the groups that a user has joined

    

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


async def get_user_groups_alt1(request: web.Request, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the groups that a user has joined

    

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
