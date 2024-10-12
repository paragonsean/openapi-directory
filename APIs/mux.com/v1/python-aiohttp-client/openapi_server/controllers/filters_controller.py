from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_filter_values_response import ListFilterValuesResponse
from openapi_server.models.list_filters_response import ListFiltersResponse
from openapi_server import util


async def list_filter_values(request: web.Request, filter_id, limit=None, page=None, filters=None, timeframe=None) -> web.Response:
    """Lists values for a specific filter

    The API has been replaced by the list-dimension-values API call.  Lists the values for a filter along with a total count of related views. 

    :param filter_id: ID of the Filter
    :type filter_id: str
    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]

    """
    return web.Response(status=200)


async def list_filters(request: web.Request, ) -> web.Response:
    """List Filters

    The API has been replaced by the list-dimensions API call.  Lists all the filters broken out into basic and advanced. 


    """
    return web.Response(status=200)
