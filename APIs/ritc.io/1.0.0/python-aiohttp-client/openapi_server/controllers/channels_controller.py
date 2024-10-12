from typing import List, Dict
from aiohttp import web

from openapi_server.models.channel import Channel
from openapi_server.models.channel_response import ChannelResponse
from openapi_server.models.function7 import Function7
from openapi_server.models.function_response import FunctionResponse
from openapi_server.models.rule import Rule
from openapi_server import util


async def add_channel(request: web.Request, channel_object) -> web.Response:
    """add_channel

    Create a channel

    :param channel_object: Channel information
    :type channel_object: dict | bytes

    """
    channel_object = Channel.from_dict(channel_object)
    return web.Response(status=200)


async def add_channel_function(request: web.Request, channel_id, channel_function_object) -> web.Response:
    """add_channel_function

    Create a channel function

    :param channel_id: Id of Channel
    :type channel_id: str
    :param channel_function_object: Channel Function information
    :type channel_function_object: dict | bytes

    """
    channel_function_object = Function7.from_dict(channel_function_object)
    return web.Response(status=200)


async def get_channel(request: web.Request, channel_id) -> web.Response:
    """get_channel

    Get channel information

    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def get_channel_function(request: web.Request, channel_id, function_id) -> web.Response:
    """get_channel_function

    Get channel function information

    :param channel_id: Id of Channel
    :type channel_id: str
    :param function_id: Id of Channel Function
    :type function_id: str

    """
    return web.Response(status=200)


async def list_anonymous_channels(request: web.Request, ) -> web.Response:
    """list_anonymous_channels

    Retrieve Channels anonymously


    """
    return web.Response(status=200)


async def list_channel_functions(request: web.Request, channel_id) -> web.Response:
    """list_channel_functions

    Retrieve Channel Functions

    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def list_channels(request: web.Request, ) -> web.Response:
    """list_channels

    Retrieve Channels


    """
    return web.Response(status=200)


async def remove_channel(request: web.Request, channel_id) -> web.Response:
    """remove_channel

    Delete a channel

    :param channel_id: Id of Channel
    :type channel_id: str

    """
    return web.Response(status=200)


async def update_channel(request: web.Request, channel_id, channel_object) -> web.Response:
    """update_channel

    Update a channel

    :param channel_id: Id of Channel
    :type channel_id: str
    :param channel_object: Channel information
    :type channel_object: dict | bytes

    """
    channel_object = Rule.from_dict(channel_object)
    return web.Response(status=200)
