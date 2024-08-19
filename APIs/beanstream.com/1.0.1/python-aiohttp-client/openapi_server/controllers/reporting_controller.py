from typing import List, Dict
from aiohttp import web

from openapi_server.models.beanstream_exception import BeanstreamException
from openapi_server.models.search_query import SearchQuery
from openapi_server.models.search_result import SearchResult
from openapi_server import util


async def reports_post(request: web.Request, search_query=None) -> web.Response:
    """Search Query

    Query for transactions using a date range and optional search criteria. This method allows you to page your search results if you are expecting a lot of results to be returned. The page start value begins at 1. If no records are found the API will return a 404 error message. For details on the parameters and allowed values for Criteria please visit the documentation http://developer.beanstream.com/documentation/analyze-payments/search-specific-criteria/

    :param search_query: 
    :type search_query: dict | bytes

    """
    search_query = SearchQuery.from_dict(search_query)
    return web.Response(status=200)
