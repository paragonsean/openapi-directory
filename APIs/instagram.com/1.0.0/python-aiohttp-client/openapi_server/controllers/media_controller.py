from typing import List, Dict
from aiohttp import web

from openapi_server.models.media_entry_response import MediaEntryResponse
from openapi_server.models.media_search_response import MediaSearchResponse
from openapi_server import util


async def media_media_id_get(request: web.Request, media_id) -> web.Response:
    """Get information about a media object.

    Get information about a media object. The returned type key will allow you to differentiate between image and video media.  **Note:** if you authenticate with an OAuth Token, you will receive the user_has_liked key which quickly tells you whether the current user has liked this media item. 

    :param media_id: The ID of the media resource.
    :type media_id: str

    """
    return web.Response(status=200)


async def media_popular_get(request: web.Request, ) -> web.Response:
    """Get a list of currently popular media.

    Get a list of what media is most popular at the moment. Can return mix of &#x60;image&#x60; and &#x60;video&#x60; types.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 


    """
    return web.Response(status=200)


async def media_search_get(request: web.Request, lat, lng, min_timestamp=None, max_timestamp=None, distance=None) -> web.Response:
    """Search for media in a given area.

    Search for media in a given area. The default time span is set to 5 days. The time span must not exceed 7 days. Defaults time stamps cover the last 5 days. Can return mix of &#x60;image&#x60; and &#x60;video&#x60; types. 

    :param lat: Latitude of the center search coordinate. If used, &#x60;lng&#x60; is required.
    :type lat: float
    :param lng: Longitude of the center search coordinate. If used, &#x60;lat&#x60; is required.
    :type lng: float
    :param min_timestamp: A unix timestamp. All media returned will be taken later than this timestamp.
    :type min_timestamp: int
    :param max_timestamp: A unix timestamp. All media returned will be taken earlier than this timestamp.
    :type max_timestamp: int
    :param distance: Default is 1km (distance&#x3D;1000), max distance is 5km.
    :type distance: int

    """
    return web.Response(status=200)


async def media_shortcode_shortcode_get(request: web.Request, shortcode) -> web.Response:
    """Get information about a media object.

    This endpoint returns the same response as &#x60;GET /media/{media-id}&#x60;.  A media object&#39;s shortcode can be found in its shortlink URL. An example shortlink is &#x60;http://instagram.com/p/D/&#x60;, its corresponding shortcode is &#x60;D&#x60;. 

    :param shortcode: The short code of the media resource.
    :type shortcode: str

    """
    return web.Response(status=200)
