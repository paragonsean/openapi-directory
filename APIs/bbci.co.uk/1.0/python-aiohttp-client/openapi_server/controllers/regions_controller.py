from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_regions(request: web.Request, lang) -> web.Response:
    """List all regions

    Get the list of all the regions TV &amp; iPlayer.

    :param lang: The language for any applicable localised strings.
    :type lang: str

    """
    return web.Response(status=200)
