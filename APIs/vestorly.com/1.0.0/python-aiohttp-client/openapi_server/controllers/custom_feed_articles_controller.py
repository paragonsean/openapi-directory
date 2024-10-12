from typing import List, Dict
from aiohttp import web

from openapi_server.models.articles import Articles
from openapi_server import util


async def find_custom_feed_articles(request: web.Request, vestorly_auth, id, access_token=None, limit=None, sort_by=None, start=None, created_at_gte_days_ago=None, text_query=None) -> web.Response:
    """find_custom_feed_articles

    Returns Articles by Category

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Category Id to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str
    :param limit: Limit on the number of articles to return
    :type limit: int
    :param sort_by: Field on model to sort by
    :type sort_by: str
    :param start: Field where the fetch will start from
    :type start: int
    :param created_at_gte_days_ago: Filter retrieved articles since this date
    :type created_at_gte_days_ago: str
    :param text_query: Search query parameter
    :type text_query: str

    """
    return web.Response(status=200)
