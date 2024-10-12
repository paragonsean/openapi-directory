from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_news(request: web.Request, query=None) -> web.Response:
    """Retrieves the latest news whose content contains the query string.

    

    :param query: Used to query news articles on their title and body. For example, ?query&#x3D;apple will return news stories that have &#39;apple&#39; in their title or body.
    :type query: str

    """
    return web.Response(status=200)
