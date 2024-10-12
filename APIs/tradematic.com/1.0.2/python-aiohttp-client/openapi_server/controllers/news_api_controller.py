from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.news import News
from openapi_server import util


async def news_news_get(request: web.Request, ) -> web.Response:
    """Get news list

    Get news list


    """
    return web.Response(status=200)


async def news_news_newsid_get(request: web.Request, newsid) -> web.Response:
    """Get news by ID

    Get news by ID

    :param newsid: 
    :type newsid: int

    """
    return web.Response(status=200)
