from typing import List, Dict
from aiohttp import web

from openapi_server.models.blog_article_list import BlogArticleList
from openapi_server import util


async def get_blog_posts(request: web.Request, locale=None, fallback=None, page=None, per_page=None) -> web.Response:
    """Get blog posts - ordered by created desc by default

    

    :param locale: Article language, default &#x60;en&#x60;. When no blog article is available and &#x60;fallback&#x3D;true&#x60; is specified, it falls back to &#x60;en&#x60;.
    :type locale: str
    :param fallback: When &#x60;true&#x60;, and no article is found in the locale, it falls back to &#x60;locale&#x3D;en&#x60;.
    :type fallback: bool
    :param page: 
    :type page: int
    :param per_page: 
    :type per_page: int

    """
    return web.Response(status=200)
