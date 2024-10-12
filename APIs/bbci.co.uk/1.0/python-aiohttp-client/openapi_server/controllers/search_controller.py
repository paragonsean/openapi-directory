from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search(request: web.Request, q, lang, rights, availability) -> web.Response:
    """Search

    Search

    :param q: The term to search for.
    :type q: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)


async def search_suggest(request: web.Request, q, lang, rights, availability) -> web.Response:
    """Search-suggest

    Search-suggest

    :param q: The term to search for.
    :type q: str
    :param lang: The language for any applicable localised strings.
    :type lang: str
    :param rights: The rights group to limit results to.
    :type rights: str
    :param availability: Whether to return all, or available programmes
    :type availability: str

    """
    return web.Response(status=200)
