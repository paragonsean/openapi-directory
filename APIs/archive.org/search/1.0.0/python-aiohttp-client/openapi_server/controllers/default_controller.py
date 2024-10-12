from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.organic_result import OrganicResult
from openapi_server.models.scrape_result import ScrapeResult
from openapi_server import util


async def search_v1_fields_get(request: web.Request, param_callback=None) -> web.Response:
    """search_v1_fields_get

    Fields that can be requested

    :param param_callback: Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
    :type param_callback: str

    """
    return web.Response(status=200)


async def search_v1_organic_get(request: web.Request, q=None, _field=None, size=None, total_only=None, param_callback=None) -> web.Response:
    """search_v1_organic_get

    Return relevance-based results from search queries 

    :param q: Lucene-type search query
    :type q: str
    :param _field: Metadata field
    :type _field: str
    :param size: Number of query results to return
    :type size: int
    :param total_only: Request total only; do not return hits
    :type total_only: bool
    :param param_callback: Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
    :type param_callback: str

    """
    return web.Response(status=200)


async def search_v1_scrape_get(request: web.Request, q=None, _field=None, sort=None, size=None, cursor=None, total_only=None, param_callback=None) -> web.Response:
    """search_v1_scrape_get

    Scrape search results from Internet Archive, allowing a scrolling cursor 

    :param q: Lucene-type search query
    :type q: str
    :param _field: Metadata field
    :type _field: str
    :param sort: sort collations
    :type sort: str
    :param size: Number of query results to return
    :type size: int
    :param cursor: Cursor for scrolling (used for subsequent calls)
    :type cursor: str
    :param total_only: Request total only; do not return hits
    :type total_only: bool
    :param param_callback: Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument.
    :type param_callback: str

    """
    return web.Response(status=200)
