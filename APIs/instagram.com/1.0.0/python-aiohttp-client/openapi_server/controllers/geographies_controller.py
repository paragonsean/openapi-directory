from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_list_response import MediaListResponse
from openapi_server import util


async def geographies_geo_id_media_recent_get(request: web.Request, geo_id, count=None, min_id=None) -> web.Response:
    """Get recent media from a custom geo-id.

    Get recent media from a geography subscription that you created.  **Note:** You can only access Geographies that were explicitly created by your OAuth client. Check the Geography Subscriptions section of the [real-time updates page](https://instagram.com/developer/realtime/). When you create a subscription to some geography that you define, you will be returned a unique &#x60;geo-id&#x60; that can be used in this query. To backfill photos from the location covered by this geography, use the [media search endpoint](https://instagram.com/developer/endpoints/media/).  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

    :param geo_id: The geography ID.
    :type geo_id: str
    :param count: Max number of media to return.
    :type count: int
    :param min_id: Return media before this &#x60;min_id&#x60;.
    :type min_id: str

    """
    return web.Response(status=200)
