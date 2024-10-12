from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_articles_response import GetArticlesResponse
from openapi_server import util


async def get_articles(request: web.Request, q=None, page=None, per_page=None, top=None) -> web.Response:
    """Get a list of filtered articles

    

    :param q: Accepts keywords to use as a search query.
    :type q: str
    :param page: Pagination Page
    :type page: int
    :param per_page: Page size (the number of items to return per page).
    :type per_page: int
    :param top: Returns the most popular articles in the last N days. &#39;top&#39; indicates the number of days since publication of the articles returned. This param can be used in conjuction with q or tag.
    :type top: str

    """
    return web.Response(status=200)
