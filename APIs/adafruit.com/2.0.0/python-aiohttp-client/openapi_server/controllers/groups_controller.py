from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_dashboard_request import CreateDashboardRequest
from openapi_server.models.feed import Feed
from openapi_server.models.group import Group
from openapi_server import util


async def add_feed_to_group(request: web.Request, group_key, username, feed_key=None) -> web.Response:
    """Add an existing Feed to a Group

    

    :param group_key: 
    :type group_key: str
    :param username: a valid username string
    :type username: str
    :param feed_key: 
    :type feed_key: str

    """
    return web.Response(status=200)


async def all_group_feeds(request: web.Request, group_key, username) -> web.Response:
    """All feeds for current user in a given group

    The Group Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed, but only for feeds within the given group.

    :param group_key: 
    :type group_key: str
    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def all_groups(request: web.Request, username) -> web.Response:
    """All groups for current user

    The Groups endpoint returns information about the user&#39;s groups. The response includes the latest value of each feed in the group, and other metadata about the group. 

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def create_group(request: web.Request, username, group) -> web.Response:
    """Create a new Group

    

    :param username: a valid username string
    :type username: str
    :param group: 
    :type group: dict | bytes

    """
    group = CreateDashboardRequest.from_dict(group)
    return web.Response(status=200)


async def destroy_group(request: web.Request, username, group_key) -> web.Response:
    """Delete an existing Group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str

    """
    return web.Response(status=200)


async def get_group(request: web.Request, username, group_key) -> web.Response:
    """Returns Group based on ID

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str

    """
    return web.Response(status=200)


async def remove_feed_from_group(request: web.Request, group_key, username, feed_key=None) -> web.Response:
    """Remove a Feed from a Group

    

    :param group_key: 
    :type group_key: str
    :param username: a valid username string
    :type username: str
    :param feed_key: 
    :type feed_key: str

    """
    return web.Response(status=200)


async def replace_group(request: web.Request, username, group_key, group) -> web.Response:
    """Replace an existing Group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param group: 
    :type group: dict | bytes

    """
    group = CreateDashboardRequest.from_dict(group)
    return web.Response(status=200)


async def update_group(request: web.Request, username, group_key, group) -> web.Response:
    """Update properties of an existing Group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param group: 
    :type group: dict | bytes

    """
    group = CreateDashboardRequest.from_dict(group)
    return web.Response(status=200)
