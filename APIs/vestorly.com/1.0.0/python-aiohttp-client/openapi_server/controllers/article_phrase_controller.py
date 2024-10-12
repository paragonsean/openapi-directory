from typing import List, Dict
from aiohttp import web

from openapi_server.models.article_phrases import ArticlePhrases
from openapi_server import util


async def find_article_phrases(request: web.Request, vestorly_auth, access_token=None, text_search=None, size=None, _from=None) -> web.Response:
    """find_article_phrases

    Returns phrases used in Categories

    :param vestorly_auth: Vestorly Auth Token
    :type vestorly_auth: str
    :param access_token: OAuth Token
    :type access_token: str
    :param text_search: Text to search phrases
    :type text_search: str
    :param size: Number of returned phrases
    :type size: int
    :param _from: Number of phrases to skip
    :type _from: int

    """
    return web.Response(status=200)
