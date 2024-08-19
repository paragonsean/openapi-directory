from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_delivery_usage_response import ListDeliveryUsageResponse
from openapi_server import util


async def list_delivery_usage(request: web.Request, page=None, limit=None, asset_id=None, live_stream_id=None, timeframe=None) -> web.Response:
    """List Usage

    Returns a list of delivery usage records and their associated Asset IDs or Live Stream IDs.

    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int
    :param limit: Number of items to include in the response
    :type limit: int
    :param asset_id: Filter response to return delivery usage for this asset only. You cannot specify both the &#x60;asset_id&#x60; and &#x60;live_stream_id&#x60; parameters together.
    :type asset_id: str
    :param live_stream_id: Filter response to return delivery usage for assets for this live stream. You cannot specify both the &#x60;asset_id&#x60; and &#x60;live_stream_id&#x60; parameters together.
    :type live_stream_id: str
    :param timeframe: Time window to get delivery usage information. timeframe[0] indicates the start time, timeframe[1] indicates the end time in seconds since the Unix epoch. Default time window is 1 hour representing usage from 13th to 12th hour from when the request is made.
    :type timeframe: List[str]

    """
    return web.Response(status=200)
