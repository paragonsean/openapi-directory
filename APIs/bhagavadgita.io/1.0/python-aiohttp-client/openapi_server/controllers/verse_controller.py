from typing import List, Dict
from aiohttp import web

from openapi_server.models.verse_schema import VerseSchema
from openapi_server import util


async def api_v1_chapters_chapter_number_verses_get(request: web.Request, access_token, chapter_number, language=None) -> web.Response:
    """Get all the Verses from a Chapter.

    Get a list of all Verses from a particular Chapter.&lt;br/&gt;

    :param access_token: Your app&#39;s access token.
    :type access_token: str
    :param chapter_number: Which Chapter Number to filter?
    :type chapter_number: int
    :param language: Language to query. Leave blank for english.
    :type language: str

    """
    return web.Response(status=200)


async def api_v1_chapters_chapter_number_verses_verse_number_get(request: web.Request, access_token, chapter_number, verse_number, language=None) -> web.Response:
    """Get a particular verse from a chapter.

    Get a specific verse from a specific chapter.&lt;br/&gt;

    :param access_token: Your app&#39;s access token.
    :type access_token: str
    :param chapter_number: Which Chapter Number to filter?
    :type chapter_number: int
    :param verse_number: Which Verse Number to filter?
    :type verse_number: str
    :param language: Language to query. Leave blank for english.
    :type language: str

    """
    return web.Response(status=200)


async def api_v1_verses_get(request: web.Request, access_token, language=None) -> web.Response:
    """Get all the Verses.

    Get a list of all Verses.&lt;br/&gt;

    :param access_token: Your app&#39;s access token.
    :type access_token: str
    :param language: Language to query. Leave blank for english.
    :type language: str

    """
    return web.Response(status=200)
