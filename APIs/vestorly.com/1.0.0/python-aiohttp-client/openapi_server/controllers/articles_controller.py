from typing import List, Dict
from aiohttp import web

from openapi_server.models.articleresponse import Articleresponse
from openapi_server.models.articles import Articles
from openapi_server import util


async def find_article_by_id(request: web.Request, vestorly_auth, id, access_token=None) -> web.Response:
    """find_article_by_id

    Returns a single article

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param id: Article Id to fetch
    :type id: str
    :param access_token: OAuth Token
    :type access_token: str

    """
    return web.Response(status=200)


async def find_articles(request: web.Request, vestorly_auth, access_token=None, limit=None, text_query=None, sort_direction=None, sort_by=None) -> web.Response:
    """find_articles

    Returns all articles

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str
    :param limit: Limit on the number of articles to return
    :type limit: int
    :param text_query: Search query parameter
    :type text_query: str
    :param sort_direction: Direction of sort (used with sort_by parameter)
    :type sort_direction: str
    :param sort_by: Field on model to sort by
    :type sort_by: str

    """
    return web.Response(status=200)
