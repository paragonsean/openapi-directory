from typing import List, Dict
from aiohttp import web

from openapi_server.models.location_info_response import LocationInfoResponse
from openapi_server.models.location_search_response import LocationSearchResponse
from openapi_server.models.media_list_response import MediaListResponse
from openapi_server import util


async def locations_location_id_get(request: web.Request, location_id) -> web.Response:
    """Get information about a location.

    Get information about a location.

    :param location_id: The location ID.
    :type location_id: str

    """
    return web.Response(status=200)


async def locations_location_id_media_recent_get(request: web.Request, location_id, min_timestamp=None, max_timestamp=None, min_id=None, max_id=None) -> web.Response:
    """Get a list of recent media objects from a given location.

    Get a list of recent media objects from a given location.

    :param location_id: The location ID.
    :type location_id: str
    :param min_timestamp: Return media after this UNIX timestamp.
    :type min_timestamp: int
    :param max_timestamp: Return media before this UNIX timestamp.
    :type max_timestamp: int
    :param min_id: Return media before this &#x60;min_id&#x60;.
    :type min_id: str
    :param max_id: Return media after this &#x60;max_id&#x60;.
    :type max_id: str

    """
    return web.Response(status=200)


async def locations_search_get(request: web.Request, distance=None, facebook_places_id=None, foursquare_id=None, lat=None, lng=None, foursquare_v2_id=None) -> web.Response:
    """Search for a location by geographic coordinate.

    Search for a location by geographic coordinate.

    :param distance: Default is 1000m (distance&#x3D;1000), max distance is 5000.
    :type distance: int
    :param facebook_places_id: Returns a location mapped off of a Facebook places id. If used, a Foursquare id and &#x60;lat&#x60;, &#x60;lng&#x60; are not required.
    :type facebook_places_id: str
    :param foursquare_id: Returns a location mapped off of a foursquare v1 api location id. If used, you are not required to use &#x60;lat&#x60; and &#x60;lng&#x60;. Note that this method is deprecated; you should use the new foursquare IDs with V2 of their API. 
    :type foursquare_id: str
    :param lat: Latitude of the center search coordinate. If used, &#x60;lng&#x60; is required.
    :type lat: float
    :param lng: Longitude of the center search coordinate. If used, &#x60;lat&#x60; is required.
    :type lng: float
    :param foursquare_v2_id: Returns a location mapped off of a foursquare v2 api location id. If used, you are not required to use &#x60;lat&#x60; and &#x60;lng&#x60;. 
    :type foursquare_v2_id: str

    """
    return web.Response(status=200)
