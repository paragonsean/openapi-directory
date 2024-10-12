from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def app_sessions_by_time_0(request: web.Request, length=None, unit=None, ending_at=None, app_id=None, segment_id=None) -> web.Response:
    """App Sessions by Time

    This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.  ### Components Used - [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;sessions\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

    :param length: (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive.
    :type length: str
    :param unit: (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;). 
    :type unit: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request.
    :type ending_at: str
    :param app_id: (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app.
    :type app_id: str
    :param segment_id: (Optional) String  Segment API identifier indicating the analytics enabled segment for which sessions should be returned.
    :type segment_id: str

    """
    return web.Response(status=200)
