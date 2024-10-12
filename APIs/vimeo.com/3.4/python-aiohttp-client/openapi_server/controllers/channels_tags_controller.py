from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_tags_to_channel_request import AddTagsToChannelRequest
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.tag import Tag
from openapi_server import util


async def add_channel_tag(request: web.Request, channel_id, word) -> web.Response:
    """Add a specific tag to a channel

    This method adds a single tag to the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param word: The word to use as the tag.
    :type word: str

    """
    return web.Response(status=200)


async def add_tags_to_channel(request: web.Request, channel_id, body) -> web.Response:
    """Add a list of tags to a channel

    This method adds multiple tags to the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddTagsToChannelRequest.from_dict(body)
    return web.Response(status=200)


async def check_if_channel_has_tag(request: web.Request, channel_id, word) -> web.Response:
    """Check if a tag has been added to a channel

    This method determines whether a specific tag has been added to the channel in question.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param word: The word to use as the tag.
    :type word: str

    """
    return web.Response(status=200)


async def delete_tag_from_channel(request: web.Request, channel_id, word) -> web.Response:
    """Remove a tag from a channel

    This method removes a single tag from the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param word: The word to use as the tag.
    :type word: str

    """
    return web.Response(status=200)


async def get_channel_tags(request: web.Request, channel_id) -> web.Response:
    """Get all the tags that have been added to a channel

    This method gets all the tags that have been added to the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)
