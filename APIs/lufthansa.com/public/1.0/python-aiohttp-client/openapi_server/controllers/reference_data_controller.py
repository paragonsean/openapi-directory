from typing import List, Dict
from aiohttp import web

from openapi_server.models.airport_response import AirportResponse
from openapi_server import util


async def references_aircraft_by_aircraft_code_get(request: web.Request, accept, aircraft_code, limit=None, offset=None) -> web.Response:
    """Aircraft

    List all aircraft types or one specific aircraft type.

    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param aircraft_code: 3-character IATA aircraft code
    :type aircraft_code: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def references_airlines_by_airline_code_get(request: web.Request, accept, airline_code, limit=None, offset=None) -> web.Response:
    """Airlines

    List all airlines or one specific airline.

    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param airline_code: 2-character IATA airline/carrier code
    :type airline_code: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def references_airports_by_airport_code_get(request: web.Request, accept, airport_code, lang=None, limit=None, offset=None, l_hoperated=None) -> web.Response:
    """Airports

    List all airports or one specific airport. All airports response is very large. It is possible to request the response in a specific language.

    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param airport_code: 3-letter IATA airport code
    :type airport_code: str
    :param lang: 2-letter ISO 3166-1 language code
    :type lang: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str
    :param l_hoperated: Restrict the results to locations with flights operated by LH (false&#x3D;0, true&#x3D;1)
    :type l_hoperated: bool

    """
    return web.Response(status=200)


async def references_airports_nearest_by_latitude_and_longitude_get(request: web.Request, latitude, longitude, accept, lang=None) -> web.Response:
    """Nearest Airports

    List the 5 closest airports to the given latitude and longitude, irrespective of the radius of the reference point.

    :param latitude: Latitude in decimal format to at most 3 decimal places
    :type latitude: int
    :param longitude: Longitude in decimal format to at most 3 decimal places
    :type longitude: int
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param lang: 2 letter ISO 3166-1 language code
    :type lang: str

    """
    return web.Response(status=200)


async def references_cities_by_city_code_get(request: web.Request, accept, city_code, lang=None, limit=None, offset=None) -> web.Response:
    """Cities

    List all cities or one specific city. It is possible to request the response in a specific language.

    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param city_code: 3-letter IATA city code
    :type city_code: str
    :param lang: 2 letter ISO 3166-1 language code
    :type lang: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def references_countries_by_country_code_get(request: web.Request, accept, country_code, lang=None, limit=None, offset=None) -> web.Response:
    """Countries

    List all countries or one specific country. It is possible to request the response in a specific language.

    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param country_code: 2-letter ISO 3166-1 country code
    :type country_code: str
    :param lang: 2 letter ISO 3166-1 language code
    :type lang: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)
