from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server.models.v3_search_result import V3SearchResult
from openapi_server import util


async def search_search(request: web.Request, search_term, route_types=None, latitude=None, longitude=None, max_distance=None, include_addresses=None, include_outlets=None, match_stop_by_suburb=None, match_route_by_suburb=None, match_stop_by_gtfs_stop_id=None, token=None, devid=None, signature=None) -> web.Response:
    """View stops, routes and myki ticket outlets that match the search term

    

    :param search_term: Search text (note: if search text is numeric and/or less than 3 characters, the API will only return routes)
    :type search_term: str
    :param route_types: Filter by route_type; values returned via RouteTypes API (note: stops and routes are ordered by route_types specified)
    :type route_types: List[int]
    :param latitude: Filter by geographic coordinate of latitude
    :type latitude: float
    :param longitude: Filter by geographic coordinate of longitude
    :type longitude: float
    :param max_distance: Filter by maximum distance (in metres) from location specified via latitude and longitude parameters
    :type max_distance: float
    :param include_addresses: Placeholder for future development; currently unavailable
    :type include_addresses: bool
    :param include_outlets: Indicates if outlets will be returned in response (default &#x3D; true)
    :type include_outlets: bool
    :param match_stop_by_suburb: Indicates whether to find stops by suburbs in the search term (default &#x3D; true)
    :type match_stop_by_suburb: bool
    :param match_route_by_suburb: Indicates whether to find routes by suburbs in the search term (default &#x3D; true)
    :type match_route_by_suburb: bool
    :param match_stop_by_gtfs_stop_id: Indicates whether to search for stops according to a metlink stop ID (default &#x3D; false)
    :type match_stop_by_gtfs_stop_id: bool
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    return web.Response(status=200)
