from typing import List, Dict
from aiohttp import web

from openapi_server.models.chapter_schema import ChapterSchema
from openapi_server import util


async def api_v1_chapters_chapter_number_get(request: web.Request, access_token, chapter_number, language=None) -> web.Response:
    """Get a specific chapter from the Bhagavad Gita.

    Get information about a specific chapter from the Bhagavad Gita.&lt;br/&gt;

    :param access_token: Your app&#39;s access token.
    :type access_token: str
    :param chapter_number: Which Chapter Number to filter?
    :type chapter_number: int
    :param language: Language to query. Leave blank for english.
    :type language: str

    """
    return web.Response(status=200)


async def api_v1_chapters_get(request: web.Request, access_token, language=None) -> web.Response:
    """Get all the 18 Chapters of the Bhagavad Gita.

    Get a list of all the 18 Chapters of the Bhagavad Gita.&lt;br/&gt;

    :param access_token: Your app&#39;s access token.
    :type access_token: str
    :param language: Language to query. Leave blank for english.
    :type language: str

    """
    return web.Response(status=200)
