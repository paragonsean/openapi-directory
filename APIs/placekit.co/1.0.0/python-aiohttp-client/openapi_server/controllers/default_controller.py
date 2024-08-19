from typing import List, Dict
from aiohttp import web

from openapi_server.models.results import Results
from openapi_server.models.reverse_request import ReverseRequest
from openapi_server.models.search_request import SearchRequest
from openapi_server import util


async def reverse(request: web.Request, payload=None) -> web.Response:
    """Reverse geocoding

    Performs a reverse geocoding search.  It will return the closest results around &#x60;coordinates&#x60;.\\ If &#x60;coordinates&#x60; are not set, it will use the user&#39;s IP to approximate its coordinates but results will be less accurate (city level accuracy instead of street level accuracy). 

    :param payload: Request parameters
    :type payload: dict | bytes

    """
    payload = ReverseRequest.from_dict(payload)
    return web.Response(status=200)


async def search(request: web.Request, payload=None) -> web.Response:
    """Search for addresses

    Performs a forward geocoding search.  It will return results around &#x60;coordinates&#x60; (if provided) and the best matching textual relevance.  **It is highly recommended** to set the &#x60;countries&#x60; parameter with the country you need results from for the best accuracy and revelance possible. 

    :param payload: Request parameters
    :type payload: dict | bytes

    """
    payload = SearchRequest.from_dict(payload)
    return web.Response(status=200)
