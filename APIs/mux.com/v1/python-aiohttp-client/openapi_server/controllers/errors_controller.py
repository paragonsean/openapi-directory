from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_errors_response import ListErrorsResponse
from openapi_server import util


async def list_errors(request: web.Request, filters=None, timeframe=None) -> web.Response:
    """List Errors

    Returns a list of errors.

    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]

    """
    return web.Response(status=200)
