from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_gifs_by_id200_response import GetGifsById200Response
from openapi_server.models.random_gif200_response import RandomGif200Response
from openapi_server import util


async def random_sticker(request: web.Request, tag=None, rating=None) -> web.Response:
    """Random Sticker

    Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog. 

    :param tag: Filters results by specified tag.
    :type tag: str
    :param rating: Filters results by specified rating.
    :type rating: str

    """
    return web.Response(status=200)


async def search_stickers(request: web.Request, q, limit=None, offset=None, rating=None, lang=None) -> web.Response:
    """Search Stickers

    Replicates the functionality and requirements of the classic GIPHY search, but returns animated stickers rather than GIFs. 

    :param q: Search query term or prhase.
    :type q: str
    :param limit: The maximum number of records to return.
    :type limit: int
    :param offset: An optional results offset.
    :type offset: int
    :param rating: Filters results by specified rating.
    :type rating: str
    :param lang: Specify default language for regional content; use a 2-letter ISO 639-1 language code.
    :type lang: str

    """
    return web.Response(status=200)


async def translate_sticker(request: web.Request, s) -> web.Response:
    """Translate phrase to Sticker

    The translate API draws on search, but uses the GIPHY &#x60;special sauce&#x60; to handle translating from one vocabulary to another. In this case, words and phrases to GIFs. 

    :param s: Search term.
    :type s: str

    """
    return web.Response(status=200)


async def trending_stickers(request: web.Request, limit=None, offset=None, rating=None) -> web.Response:
    """Trending Stickers

    Fetch Stickers currently trending online. Hand curated by the GIPHY editorial team. Returns 25 results by default. 

    :param limit: The maximum number of records to return.
    :type limit: int
    :param offset: An optional results offset.
    :type offset: int
    :param rating: Filters results by specified rating.
    :type rating: str

    """
    return web.Response(status=200)
