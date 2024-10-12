from typing import List, Dict
from aiohttp import web

from openapi_server.models.v3_error_response import V3ErrorResponse
from openapi_server import util


async def fare_estimate_get_fare_estimate_by_zone(request: web.Request, min_zone, max_zone, journey_touch_on_utc=None, journey_touch_off_utc=None, is_journey_in_free_tram_zone=None, travelled_route_types=None, token=None, devid=None, signature=None) -> web.Response:
    """Estimate a fare by zone

    

    :param min_zone: Minimum Zone travelled through ie. 1
    :type min_zone: int
    :param max_zone: Maximum Zone travelled through id. 6
    :type max_zone: int
    :param journey_touch_on_utc: JourneyTouchOnUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53).
    :type journey_touch_on_utc: str
    :param journey_touch_off_utc: JourneyTouchOffUtc in format yyyy-M-d h:m (e.g 2016-5-31 16:53).
    :type journey_touch_off_utc: str
    :param is_journey_in_free_tram_zone: 
    :type is_journey_in_free_tram_zone: bool
    :param travelled_route_types: 
    :type travelled_route_types: List[int]
    :param token: Please ignore
    :type token: str
    :param devid: Your developer id
    :type devid: str
    :param signature: Authentication signature for request
    :type signature: str

    """
    journey_touch_on_utc = util.deserialize_datetime(journey_touch_on_utc)
    journey_touch_off_utc = util.deserialize_datetime(journey_touch_off_utc)
    return web.Response(status=200)
