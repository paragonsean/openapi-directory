from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_feed_filter_input import CustomFeedFilterInput
from openapi_server.models.custom_feed_filterresponse import CustomFeedFilterresponse
from openapi_server.models.custom_feed_filters import CustomFeedFilters
from openapi_server import util


async def create_custom_feed_filter(request: web.Request, vestorly_auth, custom_feed_filter, access_token=None) -> web.Response:
    """create_custom_feed_filter

    Creates a new Category filter

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param custom_feed_filter: Category filter to add
    :type custom_feed_filter: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    custom_feed_filter = CustomFeedFilterInput.from_dict(custom_feed_filter)
    return web.Response(status=200)


async def delete_custom_feed_filter(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """delete_custom_feed_filter

    Deletes the Category&#39;s filter

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of category filter to delete
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_custom_feed_filter_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """find_custom_feed_filter_by_id

    Returns a single Category&#39;s filter

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Custom Feed Filter Id to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_custom_feed_filters(request: web.Request, vestorly_auth, access_token=None) -> web.Response:
    """find_custom_feed_filters

    Returns all Categorie&#39;s filters

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def update_custom_feed_filter_by_id(request: web.Request, vestorly_auth, id, custom_feed_filter, access_token=None) -> web.Response:
    """update_custom_feed_filter_by_id

    Updates a Category Feed Filter

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: id of category filter to update
    :type id: str
    :param custom_feed_filter: Category filter to add
    :type custom_feed_filter: dict | bytes
    :param access_token: OAuth Token
    :type access_token: str

    """
    custom_feed_filter = CustomFeedFilterInput.from_dict(custom_feed_filter)
    return web.Response(status=200)
