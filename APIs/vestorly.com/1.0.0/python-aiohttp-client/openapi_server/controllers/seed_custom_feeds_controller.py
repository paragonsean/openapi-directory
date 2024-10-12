from typing import List, Dict
from aiohttp import web

from openapi_server.models.seed_custom_feed_input import SeedCustomFeedInput
from openapi_server.models.seed_custom_feedresponse import SeedCustomFeedresponse
from openapi_server.models.seed_custom_feeds import SeedCustomFeeds
from openapi_server import util


async def create_seed_custom_feed(request: web.Request, vestorly_auth, seed_custom_feed, access_token=None) -> web.Response:
    """create_seed_custom_feed

    Creates a new Category Keyword

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param seed_custom_feed: Category to add
    :type seed_custom_feed: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    seed_custom_feed = SeedCustomFeedInput.from_dict(seed_custom_feed)
    return web.Response(status=200)


async def delete_seed_custom_feed(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """delete_seed_custom_feed

    Deletes a Category keywords

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of seed category to delete
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_seed_custom_feed_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """find_seed_custom_feed_by_id

    Returns a single Category keyword

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Seed Custom Feed Id to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_seed_custom_feeds(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_seed_custom_feeds

    Returns all Categories keywords

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_seed_custom_feed_by_id(request: web.Request, vestorly_auth, id, seed_custom_feed, access_token=None) -> web.Response:
    """update_seed_custom_feed_by_id

    Updates a Category keywords

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of seed category to update
    :type id: str
    :param seed_custom_feed: Category keywords to add
    :type seed_custom_feed: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    seed_custom_feed = SeedCustomFeedInput.from_dict(seed_custom_feed)
    return web.Response(status=200)
