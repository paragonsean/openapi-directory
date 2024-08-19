from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_video_views_response import ListVideoViewsResponse
from openapi_server.models.video_view_response import VideoViewResponse
from openapi_server import util


async def get_video_view(request: web.Request, video_view_id) -> web.Response:
    """Get a Video View

    Returns the details of a video view.

    :param video_view_id: ID of the Video View
    :type video_view_id: str

    """
    return web.Response(status=200)


async def list_video_views(request: web.Request, limit=None, page=None, viewer_id=None, error_id=None, order_direction=None, filters=None, timeframe=None) -> web.Response:
    """List Video Views

    Returns a list of video views which match the filters and have a &#x60;view_end&#x60; within the specified timeframe.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param viewer_id: Viewer ID to filter results by. This value may be provided by the integration, or may be created by Mux.
    :type viewer_id: str
    :param error_id: Filter video views by the provided error ID (as returned in the error_type_id field in the list video views endpoint). If you provide any as the error ID, this will filter the results to those with any error.
    :type error_id: int
    :param order_direction: Sort order.
    :type order_direction: str
    :param filters: Limit the results to rows that match conditions from provided key:value pairs. Must be provided as an array query string parameter.  To exclude rows that match a certain condition, prepend a &#x60;!&#x60; character to the dimension.  Possible filter names are the same as returned by the List Filters endpoint.  Example:    * &#x60;filters[]&#x3D;operating_system:windows&amp;filters[]&#x3D;!country:US&#x60; 
    :type filters: List[str]
    :param timeframe: Timeframe window to limit results by. Must be provided as an array query string parameter (e.g. timeframe[]&#x3D;).  Accepted formats are...    * array of epoch timestamps e.g. &#x60;timeframe[]&#x3D;1498867200&amp;timeframe[]&#x3D;1498953600&#x60;   * duration string e.g. &#x60;timeframe[]&#x3D;24:hours or timeframe[]&#x3D;7:days&#x60; 
    :type timeframe: List[str]

    """
    return web.Response(status=200)
