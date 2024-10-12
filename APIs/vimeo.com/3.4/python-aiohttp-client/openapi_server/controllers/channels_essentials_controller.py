from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.create_channel_request import CreateChannelRequest
from openapi_server.models.edit_channel_request import EditChannelRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def create_channel(request: web.Request, body) -> web.Response:
    """Create a channel

    This method creates a new channel.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateChannelRequest.from_dict(body)
    return web.Response(status=200)


async def delete_channel(request: web.Request, channel_id) -> web.Response:
    """Delete a channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)


async def edit_channel(request: web.Request, channel_id, body=None) -> web.Response:
    """Edit a channel

    This method edits the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditChannelRequest.from_dict(body)
    return web.Response(status=200)


async def get_channel(request: web.Request, channel_id) -> web.Response:
    """Get a specific channel

    

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)


async def get_channel_subscriptions(request: web.Request, user_id, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the channels to which a user subscribes

    

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


async def get_channel_subscriptions_alt1(request: web.Request, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the channels to which a user subscribes

    

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


async def get_channels(request: web.Request, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all channels

    

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
    :param sort: The way to sort the results.  Option descriptions:  * &#x60;relevant&#x60; - Relevant sorting is available only for search queries. 
    :type sort: str

    """
    return web.Response(status=200)
