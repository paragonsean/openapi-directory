from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def pirate_generate_insult_get(request: web.Request, limit=None) -> web.Response:
    """pirate_generate_insult_get

    Generate random pirate insults.

    :param limit: No of insults to generate
    :type limit: int

    """
    return web.Response(status=200)


async def pirate_generate_lorem_ipsum_get(request: web.Request, type=None, limit=None) -> web.Response:
    """pirate_generate_lorem_ipsum_get

    Generate pirate lorem ipsum.

    :param type: Type of element to generate &#x60;paragraphs/sentences/words&#x60;.
    :type type: str
    :param limit: No of elements to generate
    :type limit: int

    """
    return web.Response(status=200)


async def pirate_generate_name_get(request: web.Request, variation=None, limit=None) -> web.Response:
    """pirate_generate_name_get

    Generate random pirate names.

    :param variation: Variation to generate &#x60;male/female&#x60;.
    :type variation: str
    :param limit: No of names to generate
    :type limit: int

    """
    return web.Response(status=200)
