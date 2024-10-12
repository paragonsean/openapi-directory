from typing import List, Dict
from aiohttp import web

from openapi_server.models.distance_response import DistanceResponse
from openapi_server.models.elevation_response import ElevationResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.sun_position_response import SunPositionResponse
from openapi_server.models.timezone_response import TimezoneResponse
from openapi_server import util


async def get_distance(request: web.Request, location_a, location_b, unit=None) -> web.Response:
    """Calculate distance between lats/longs

    This webservice is providing you the ability to calculate the distance between 2 lat/long points, it returns you the value in km or miles

    :param location_a: The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point A
    :type location_a: str
    :param location_b: The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) of location point B
    :type location_b: str
    :param unit: The unit of length you want the elevation returned either meters or feet returned
    :type unit: str

    """
    return web.Response(status=200)


async def get_elevation(request: web.Request, locations, unit=None) -> web.Response:
    """Search elevation informations from lat/long

    This webservice is providing you the ability to retrieve the elevation in meters or feet of ONE or MULTIPLE given latitude/longitude point(s). &lt;br /&gt;If you use MULTIPLE lat/long point, the maximum number of point you can send in one request is 256. Be aware that if MULTIPLE mode, the results are de-deplicated if you are sending the same latitude/longitude point multiple times.&lt;br /&gt;If your workload is a batch of millions of lat/long point, You will also get better throughput if you send around 100 lat/long points in one request than the maximum. This maximum is mostly allowed for people trying to graph altitudes.

    :param locations: The location as a latitude / longitude point ( ex. 67.85572,20.22513 ) or a list of coordinates separated using the pipe (&#39;|&#39;) character. The maximum number of coordinates you can send at one time is 20 ( ex. 67.85572,20.22513|27.85572,20.22513 )
    :type locations: str
    :param unit: The unit of length you want the elevation returned either meters or feet returned
    :type unit: str

    """
    return web.Response(status=200)


async def get_sun(request: web.Request, location, _date=None) -> web.Response:
    """Search position of sun from lat/long and date

    This webservice is providing you the ability to retrieve the time of each phases of the sunlight cycle. Sunset, sunrise, sunriseEnd, golden hour, solarNoon, dawn, dusk and more for a given location and date. If the date if not provided, the response provided return informations for today at UTC time.

    :param location: Here you can send either a latitude / longitude
    :type location: str
    :param _date: The date for what you will get the data ( full-date notation as defined by RFC 3339, section 5.6, for example, 2017-07-21 ), if not provided as parameter, today is going to be used
    :type _date: str

    """
    _date = util.deserialize_date(_date)
    return web.Response(status=200)


async def get_timezone(request: web.Request, location) -> web.Response:
    """Search timezone and time informations from lat/long

    This webservice is providing you the ability to retrieve the tz database time zones ( https://en.wikipedia.org/wiki/List_of_tz_database_time_zones )  from a given location ( )latitude and longitude or IATA code ). It also returns you the current time at the provided location.

    :param location: Here you can send either a latitude / longitude ( ex. 67.85572,20.22513 ) or a IATA Code ( ex. LHR for London Heathrow)
    :type location: str

    """
    return web.Response(status=200)
