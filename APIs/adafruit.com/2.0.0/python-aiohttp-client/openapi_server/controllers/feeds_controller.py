from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_feed_request import CreateFeedRequest
from openapi_server.models.feed import Feed
from openapi_server.models.group import Group
from openapi_server import util


async def add_feed_to_group_0(request: web.Request, group_key, username, feed_key=None) -> web.Response:
    """Add an existing Feed to a Group

    

    :param group_key: 
    :type group_key: str
    :param username: a valid username string
    :type username: str
    :param feed_key: 
    :type feed_key: str

    """
    return web.Response(status=200)


async def all_feeds(request: web.Request, username) -> web.Response:
    """All feeds for current user

    The Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed.

    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def all_group_feeds_0(request: web.Request, group_key, username) -> web.Response:
    """All feeds for current user in a given group

    The Group Feeds endpoint returns information about the user&#39;s feeds. The response includes the latest value of each feed, and other metadata about each feed, but only for feeds within the given group.

    :param group_key: 
    :type group_key: str
    :param username: a valid username string
    :type username: str

    """
    return web.Response(status=200)


async def create_feed(request: web.Request, username, feed, group_key=None) -> web.Response:
    """Create a new Feed

    

    :param username: a valid username string
    :type username: str
    :param feed: 
    :type feed: dict | bytes
    :param group_key: 
    :type group_key: str

    """
    feed = CreateFeedRequest.from_dict(feed)
    return web.Response(status=200)


async def create_group_feed(request: web.Request, username, group_key, feed) -> web.Response:
    """Create a new Feed in a Group

    

    :param username: a valid username string
    :type username: str
    :param group_key: 
    :type group_key: str
    :param feed: 
    :type feed: dict | bytes

    """
    feed = CreateFeedRequest.from_dict(feed)
    return web.Response(status=200)


async def destroy_feed(request: web.Request, username, feed_key) -> web.Response:
    """Delete an existing Feed

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str

    """
    return web.Response(status=200)


async def get_feed(request: web.Request, username, feed_key) -> web.Response:
    """Get feed by feed key

    Returns feed based on the feed key

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str

    """
    return web.Response(status=200)


async def get_feed_details(request: web.Request, username, feed_key) -> web.Response:
    """Get detailed feed by feed key

    Returns more detailed feed record based on the feed key

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str

    """
    return web.Response(status=200)


async def remove_feed_from_group_0(request: web.Request, group_key, username, feed_key=None) -> web.Response:
    """Remove a Feed from a Group

    

    :param group_key: 
    :type group_key: str
    :param username: a valid username string
    :type username: str
    :param feed_key: 
    :type feed_key: str

    """
    return web.Response(status=200)


async def replace_feed(request: web.Request, username, feed_key, feed) -> web.Response:
    """Replace an existing Feed

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param feed: 
    :type feed: dict | bytes

    """
    feed = CreateFeedRequest.from_dict(feed)
    return web.Response(status=200)


async def update_feed(request: web.Request, username, feed_key, feed) -> web.Response:
    """Update properties of an existing Feed

    

    :param username: a valid username string
    :type username: str
    :param feed_key: a valid feed key
    :type feed_key: str
    :param feed: 
    :type feed: dict | bytes

    """
    feed = CreateFeedRequest.from_dict(feed)
    return web.Response(status=200)
