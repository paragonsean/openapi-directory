from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def news_search_read(request: web.Request, title) -> web.Response:
    """Return news or article search result

    Return news or article search result  ### Response Class (Status 200)  * __{title}__: Used as a key word to search news and articles,  For more details on how news &amp; articles are listed [see here][ref]. [ref]: https://etmdb.com/en/news-list/-updated_date

    :param title: 
    :type title: str

    """
    return web.Response(status=200)
