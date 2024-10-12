from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_channel_moderators_request import AddChannelModeratorsRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.remove_channel_moderators_request import RemoveChannelModeratorsRequest
from openapi_server.models.replace_channel_moderators_request import ReplaceChannelModeratorsRequest
from openapi_server.models.user import User
from openapi_server import util


async def add_channel_moderator(request: web.Request, channel_id, user_id) -> web.Response:
    """Add a specific channel moderator

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def add_channel_moderators(request: web.Request, channel_id, body) -> web.Response:
    """Add a list of channel moderators

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddChannelModeratorsRequest.from_dict(body)
    return web.Response(status=200)


async def get_channel_moderator(request: web.Request, channel_id, user_id) -> web.Response:
    """Get a specific channel moderator

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def get_channel_moderators(request: web.Request, channel_id, direction=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the moderators in a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
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


async def remove_channel_moderator(request: web.Request, channel_id, user_id) -> web.Response:
    """Remove a specific channel moderator

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def remove_channel_moderators(request: web.Request, channel_id, body) -> web.Response:
    """Remove a list of channel moderators

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveChannelModeratorsRequest.from_dict(body)
    return web.Response(status=200)


async def replace_channel_moderators(request: web.Request, channel_id, body) -> web.Response:
    """Replace the moderators of a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = ReplaceChannelModeratorsRequest.from_dict(body)
    return web.Response(status=200)
