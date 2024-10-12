from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.user import User
from openapi_server import util


async def check_if_user_subscribed_to_channel(request: web.Request, channel_id, user_id) -> web.Response:
    """Check if a user follows a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def check_if_user_subscribed_to_channel_alt1(request: web.Request, channel_id) -> web.Response:
    """Check if a user follows a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)


async def get_channel_subscribers(request: web.Request, channel_id, filter, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the followers of a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param filter: The attribute by which to filter the results.
    :type filter: str
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


async def subscribe_to_channel(request: web.Request, channel_id, user_id) -> web.Response:
    """Subscribe a user to a specific channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def subscribe_to_channel_alt1(request: web.Request, channel_id) -> web.Response:
    """Subscribe a user to a specific channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)


async def unsubscribe_from_channel(request: web.Request, channel_id, user_id) -> web.Response:
    """Unsubscribe a user from a specific channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def unsubscribe_from_channel_alt1(request: web.Request, channel_id) -> web.Response:
    """Unsubscribe a user from a specific channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)
