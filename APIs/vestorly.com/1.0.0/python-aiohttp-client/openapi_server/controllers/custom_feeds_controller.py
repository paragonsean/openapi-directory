from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_feed_input import CustomFeedInput
from openapi_server.models.custom_feedresponse import CustomFeedresponse
from openapi_server.models.custom_feeds import CustomFeeds
from openapi_server import util


async def create_custom_feed(request: web.Request, vestorly_auth, custom_feed, access_token=None) -> web.Response:
    """create_custom_feed

    Creates a new Category

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param custom_feed: Category to add
    :type custom_feed: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    custom_feed = CustomFeedInput.from_dict(custom_feed)
    return web.Response(status=200)


async def delete_custom_feed(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """delete_custom_feed

    Deletes a new Category

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of category to delete
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def duplicate_custom_feed(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """duplicate_custom_feed

    Duplicates Category

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of category to duplicate
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_custom_feed_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """find_custom_feed_by_id

    Returns a single Category

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Custom Feed Id to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_custom_feeds(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_custom_feeds

    Returns all Categories

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_category_by_id(request: web.Request, vestorly_auth, id, custom_feed, access_token=None) -> web.Response:
    """update_category_by_id

    Updates a Category

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of category to update
    :type id: str
    :param custom_feed: Category to add
    :type custom_feed: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    custom_feed = CustomFeedInput.from_dict(custom_feed)
    return web.Response(status=200)
