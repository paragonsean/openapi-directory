from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_dimension_values_response import ListDimensionValuesResponse
from openapi_server.models.list_dimensions_response import ListDimensionsResponse
from openapi_server import util


async def list_dimension_values(request: web.Request, dimension_id, limit=None, page=None, filters=None, timeframe=None) -> web.Response:
    """Lists the values for a specific dimension

    Lists the values for a dimension along with a total count of related views.  Note: This API replaces the list-filter-values API call. 

    :param dimension_id: ID of the Dimension
    :type dimension_id: str
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


async def list_dimensions(request: web.Request, ) -> web.Response:
    """List Dimensions

    List all available dimensions.  Note: This API replaces the list-filters API call. 


    """
    return web.Response(status=200)
