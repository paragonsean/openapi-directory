from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_gifs_by_id200_response import GetGifsById200Response
from openapi_server.models.random_gif200_response import RandomGif200Response
from openapi_server import util


async def get_gif_by_id(request: web.Request, gif_id) -> web.Response:
    """Get GIF by Id

    Returns a GIF given that GIF&#39;s unique ID 

    :param gif_id: Filters results by specified GIF ID.
    :type gif_id: int

    """
    return web.Response(status=200)


async def get_gifs_by_id(request: web.Request, ids=None) -> web.Response:
    """Get GIFs by ID

    A multiget version of the get GIF by ID endpoint. 

    :param ids: Filters results by specified GIF IDs, separated by commas.
    :type ids: str

    """
    return web.Response(status=200)


async def random_gif(request: web.Request, tag=None, rating=None) -> web.Response:
    """Random GIF

    Returns a random GIF, limited by tag. Excluding the tag parameter will return a random GIF from the GIPHY catalog. 

    :param tag: Filters results by specified tag.
    :type tag: str
    :param rating: Filters results by specified rating.
    :type rating: str

    """
    return web.Response(status=200)


async def search_gifs(request: web.Request, q, limit=None, offset=None, rating=None, lang=None) -> web.Response:
    """Search GIFs

    Search all GIPHY GIFs for a word or phrase. Punctuation will be stripped and ignored.  Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling or american+psycho. 

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


async def translate_gif(request: web.Request, s) -> web.Response:
    """Translate phrase to GIF

    The translate API draws on search, but uses the GIPHY &#x60;special sauce&#x60; to handle translating from one vocabulary to another. In this case, words and phrases to GIF 

    :param s: Search term.
    :type s: str

    """
    return web.Response(status=200)


async def trending_gifs(request: web.Request, limit=None, offset=None, rating=None) -> web.Response:
    """Trending GIFs

    Fetch GIFs currently trending online. Hand curated by the GIPHY editorial team.  The data returned mirrors the GIFs showcased on the GIPHY homepage. Returns 25 results by default. 

    :param limit: The maximum number of records to return.
    :type limit: int
    :param offset: An optional results offset.
    :type offset: int
    :param rating: Filters results by specified rating.
    :type rating: str

    """
    return web.Response(status=200)
