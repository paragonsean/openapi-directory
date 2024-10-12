from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_channel_categories_request import AddChannelCategoriesRequest
from openapi_server.models.category import Category
from openapi_server.models.error import Error
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def add_channel_categories(request: web.Request, channel_id, body) -> web.Response:
    """Add a list of categories to a channel

    This method adds multiple categories to the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = AddChannelCategoriesRequest.from_dict(body)
    return web.Response(status=200)


async def categorize_channel(request: web.Request, category, channel_id) -> web.Response:
    """Categorize a channel

    This method adds a channel to a category.

    :param category: The name of the category.
    :type category: str
    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)


async def delete_channel_category(request: web.Request, category, channel_id) -> web.Response:
    """Remove a category from a channel

    This method removes a single category from the specified channel.

    :param category: The name of the category.
    :type category: str
    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)


async def get_channel_categories(request: web.Request, channel_id) -> web.Response:
    """Get all the categories in a channel

    This method gets all the categories in the specified channel.

    :param channel_id: The ID of the channel.
    :type channel_id: 

    """
    return web.Response(status=200)
