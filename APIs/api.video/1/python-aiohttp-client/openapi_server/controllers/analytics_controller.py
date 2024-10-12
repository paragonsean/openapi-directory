from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.raw_statistics_list_live_stream_analytics_response import RawStatisticsListLiveStreamAnalyticsResponse
from openapi_server.models.raw_statistics_list_player_session_events_response import RawStatisticsListPlayerSessionEventsResponse
from openapi_server.models.raw_statistics_list_sessions_response import RawStatisticsListSessionsResponse
from openapi_server import util


async def g_et_analytics_live_streams_live_stream_id(request: web.Request, live_stream_id, period=None, current_page=None, page_size=None) -> web.Response:
    """List live stream player sessions

    

    :param live_stream_id: The unique identifier for the live stream you want to retrieve analytics for.
    :type live_stream_id: str
    :param period: Period must have one of the following formats:  - For a day : \&quot;2018-01-01\&quot;, - For a week: \&quot;2018-W01\&quot;,  - For a month: \&quot;2018-01\&quot; - For a year: \&quot;2018\&quot; For a range period:  -  Date range: \&quot;2018-01-01/2018-01-15\&quot; 
    :type period: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_analytics_sessions_session_id_events(request: web.Request, session_id, current_page=None, page_size=None) -> web.Response:
    """List player session events

    Useful to track and measure video&#39;s engagement.

    :param session_id: A unique identifier you can use to reference and track a session with.
    :type session_id: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_analytics_videos_video_id(request: web.Request, video_id, period=None, metadata=None, current_page=None, page_size=None) -> web.Response:
    """List video player sessions

    Retrieve all available user sessions for a specific video. Tutorials that use the [analytics endpoint](https://api.video/blog/endpoints/analytics).

    :param video_id: The unique identifier for the video you want to retrieve session information for.
    :type video_id: str
    :param period: Period must have one of the following formats:  - For a day : 2018-01-01, - For a week: 2018-W01,  - For a month: 2018-01 - For a year: 2018 For a range period:  -  Date range: 2018-01-01/2018-01-15 
    :type period: str
    :param metadata: Metadata and [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) filter. Send an array of key value pairs you want to filter sessios with.
    :type metadata: List[str]
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)
