from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def segment_analytics_0(request: web.Request, segment_id=None, length=None, ending_at=None) -> web.Response:
    """Segment Analytics

    This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;size\&quot; : (int) size of the segment on that date         },         ...     ] } &#x60;&#x60;&#x60;

    :param segment_id: (Required) String  Segment API identifier.
    :type segment_id: str
    :param length: (Required) Integer  Max number of days before &#x60;ending_at&#x60; to include in the returned series - must be between 1 and 100 inclusive.
    :type length: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request.
    :type ending_at: str

    """
    return web.Response(status=200)


async def segment_details_0(request: web.Request, segment_id=None) -> web.Response:
    """Segment Details

    This endpoint allows you to retrieve relevant information on the segment, which can be identified by the &#x60;segment_id&#x60;.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {       \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,       \&quot;created_at\&quot; : (string) date created as ISO 8601 date,       \&quot;updated_at\&quot; : (string) date last updated as ISO 8601 date,       \&quot;name\&quot; : (string) segment name,       \&quot;description\&quot; : (string) human-readable description of filters,       \&quot;text_description\&quot; : (string) segment description,        \&quot;tags\&quot; : (array) tag names associated with the segment } &#x60;&#x60;&#x60;

    :param segment_id: (Required) String  Segment API identifier
    :type segment_id: str

    """
    return web.Response(status=200)


async def segment_list_0(request: web.Request, page=None, sort_direction=None) -> web.Response:
    """Segment List

    This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.  ### Request Components - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;segments\&quot; : [         {             \&quot;id\&quot; : (string) Segment API Identifier,             \&quot;name\&quot; : (string) segment name,             \&quot;analytics_tracking_enabled\&quot; : (boolean) whether the segment has analytics tracking enabled,             \&quot;tags\&quot; : (array) tag names associated with the segment         },         ...     ] } &#x60;&#x60;&#x60;

    :param page: (Optional) Integer  The page of segments to return, defaults to 0 (returns the first set of up to 100)
    :type page: str
    :param sort_direction: (Optional) String  Pass in the value &#x60;desc&#x60; to sort by creation time from newest to oldest. Pass in &#x60;asc&#x60; to sort from oldest to newest. If &#x60;sort_direction&#x60; is not included, the default order is oldest to newest.
    :type sort_direction: str

    """
    return web.Response(status=200)
