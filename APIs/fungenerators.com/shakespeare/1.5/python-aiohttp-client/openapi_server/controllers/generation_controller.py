from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def shakespeare_generate_insult_get(request: web.Request, limit=None) -> web.Response:
    """shakespeare_generate_insult_get

    Generate random Shakespeare style insults.

    :param limit: No of insults to generate
    :type limit: int

    """
    return web.Response(status=200)


async def shakespeare_generate_lorem_ipsum_get(request: web.Request, type=None, limit=None) -> web.Response:
    """shakespeare_generate_lorem_ipsum_get

    Generate Shakespeare lorem ipsum.

    :param type: Type of element to generate &#x60;paragraphs/sentences/words&#x60;.
    :type type: str
    :param limit: No of elements to generate
    :type limit: int

    """
    return web.Response(status=200)


async def shakespeare_generate_name_get(request: web.Request, variation=None, limit=None) -> web.Response:
    """shakespeare_generate_name_get

    Generate random Shakespearen names.

    :param variation: Variation to generate &#x60;male/female&#x60;.
    :type variation: str
    :param limit: No of names to generate
    :type limit: int

    """
    return web.Response(status=200)
