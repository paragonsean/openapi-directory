from typing import List, Dict
from aiohttp import web

from openapi_server.models.language import Language
from openapi_server import util


async def get_languages(request: web.Request, filter=None) -> web.Response:
    """Get all languages

    

    :param filter: The attribute by which to filter the results.  Option descriptions:  * &#x60;texttracks&#x60; - Only return text track supported languages 
    :type filter: str

    """
    return web.Response(status=200)
