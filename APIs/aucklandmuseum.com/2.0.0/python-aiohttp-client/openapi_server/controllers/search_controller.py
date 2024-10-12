from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_search(request: web.Request, index, operation, q=None) -> web.Response:
    """Perform simple search queries over Auckland Museum Collections and Cenotaph data

    Use this endpoint to perform simple search queries for finding information and subjects you may be interested in  Searches performed via this endpoint run against an [Elastic](www.elastic.co) server. This endpoint mirrors the Elastic search API documented [here](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/search-search.html)  Use the   - &#x60;collectionsonline&#x60; index to perform searches over other all Collections data   - &#x60;cenotaph&#x60; index to perform searches over Cenotaph data 

    :param index: search index name Possible values: * &#x60;collectionsonline&#x60; * &#x60;cenotaph&#x60; 
    :type index: str
    :param operation: One of the supported elasticsearch operations like &#x60;_search&#x60; or &#x60;_suggest&#x60;
    :type operation: str
    :param q: One of the supported elasticsearch query parameter values for key &#x60;q&#x60;
    :type q: str

    """
    return web.Response(status=200)


async def post_search(request: web.Request, index, operation, body=None) -> web.Response:
    """Perform complex search queries over Auckland Museum Collections and Cenotaph data

    Searches performed via this endpoint run against an [Elastic](www.elastic.co) server. This endpoint mirrors the Elastic search API documented [here](https://www.elastic.co/guide/en/elasticsearch/reference/1.5/search-search.html)  Use the   - &#x60;collectionsonline&#x60; index to perform searches over other all Collections data   - &#x60;cenotaph&#x60; index to perform searches over Cenotaph data 

    :param index: search index name Possible values: * &#x60;collectionsonline&#x60; * &#x60;cenotaph&#x60; 
    :type index: str
    :param operation: One of the supported elasticsearch operations like &#x60;_search&#x60; or &#x60;_suggest&#x60;
    :type operation: str
    :param body: body
    :type body: 

    """
    return web.Response(status=200)
