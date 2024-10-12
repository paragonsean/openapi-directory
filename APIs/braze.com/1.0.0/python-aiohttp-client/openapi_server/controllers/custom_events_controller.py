from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def custom_events_analytics_0(request: web.Request, event=None, length=None, unit=None, ending_at=None, app_id=None, segment_id=None) -> web.Response:
    """Custom Events Analytics

    This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.  ### Components Used -[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) point in time - as ISO 8601 extended when unit is \&quot;hour\&quot; and as ISO 8601 date when unit is \&quot;day\&quot;,             \&quot;count\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |

    :param event: (Required) String  The name of the custom event for which to return analytics 
    :type event: str
    :param length: (Required) Integer  Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive
    :type length: str
    :param unit: (Optional) String  Unit of time between data points - can be \&quot;day\&quot; or \&quot;hour\&quot; (defaults to \&quot;day\&quot;)
    :type unit: str
    :param ending_at: (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    :type ending_at: str
    :param app_id: (Optional) String  App API identifier retrieved from the Developer Console to limit analytics to a specific app
    :type app_id: str
    :param segment_id: (Optional) String  Segment API identifier indicating the analytics enabled segment for which event analytics should be returned
    :type segment_id: str

    """
    return web.Response(status=200)


async def custom_events_list_0(request: web.Request, page=None) -> web.Response:
    """Custom Events List

    This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;events\&quot; : [         \&quot;Event A\&quot;,         \&quot;Event B\&quot;,         \&quot;Event C\&quot;,         ...     ] } &#x60;&#x60;&#x60;  ### Fatal Error Response Codes  The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.  | Error Code       | Reason / Cause                                                   | | ---------------- | ---------------------------------------------------------------- | | 400 Bad Request  | Bad Syntax                                                       | | 401 Unauthorized | Unknown or missing REST API Key                                  | | 429 Rate Limited | Over rate limit                                                  | | 5XX              | Internal server error, you should retry with exponential backoff |

    :param page: (Optional) Integer  The page of event names to return, defaults to 0 (returns the first set of up to 250)
    :type page: str

    """
    return web.Response(status=200)
