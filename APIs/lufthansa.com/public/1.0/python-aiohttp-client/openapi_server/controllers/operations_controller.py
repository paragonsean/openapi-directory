from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def operations_flightstatus_arrivals_by_airport_code_and_from_date_time_get(request: web.Request, airport_code, from_date_time, accept, limit=None, offset=None) -> web.Response:
    """Flight Status at Arrival Airport

    Status of all arrivals at a given airport up to 4 hours from the provided date time.

    :param airport_code: 3-letter IATA aiport code (e.g. &#39;ZRH&#39;)
    :type airport_code: str
    :param from_date_time: Start of time range in local time of arrival airport (YYYY-MM-DDTHH:mm)
    :type from_date_time: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def operations_flightstatus_by_flight_number_and_date_get(request: web.Request, flight_number, _date, accept, limit=None, offset=None) -> web.Response:
    """Flight Status

    Status of a particular flight (boarding, delayed, etc.).

    :param flight_number: Flight number including carrier code and any suffix (e.g. &#39;LH400&#39;)
    :type flight_number: str
    :param _date: The departure date (YYYY-MM-DD) in the local time of the departure airport
    :type _date: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def operations_flightstatus_departures_by_airport_code_and_from_date_time_get(request: web.Request, airport_code, from_date_time, accept, limit=None, offset=None) -> web.Response:
    """Flight Status at Departure Airport

    Status of all departures from a given airport up to 4 hours from the provided date time.

    :param airport_code: Departure airport. 3-letter IATA airport code (e.g. &#39;HAM&#39;)
    :type airport_code: str
    :param from_date_time: Start of time range in local time of departure airport (YYYY-MM-DDTHH:mm)
    :type from_date_time: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def operations_flightstatus_route_date_by_origin_and_destination_get(request: web.Request, origin, destination, _date, accept, limit=None, offset=None) -> web.Response:
    """Flight Status by Route

    Status of flights between a given origin and destination on a given date.

    :param origin: 3-letter IATA airport (e.g. &#39;FRA&#39;)
    :type origin: str
    :param destination: 3-letter IATA airport code (e.g. &#39;JFK&#39;)
    :type destination: str
    :param _date: Departure date (YYYY-MM-DD) in local time of departure airport
    :type _date: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)


async def operations_schedules_from_date_time_by_origin_and_destination_get(request: web.Request, origin, destination, from_date_time, accept, direct_flights=None, limit=None, offset=None) -> web.Response:
    """Flight Schedules

    Scheduled flights between given airports on a given date.

    :param origin: Departure airport. 3-letter IATA airport code (e.g. &#39;ZRH&#39;)
    :type origin: str
    :param destination: Destination airport. 3-letter IATA airport code (e.g. &#39;FRA&#39;)
    :type destination: str
    :param from_date_time: Local departure date and optionally departure time (YYYY-MM-DD or YYYY-MM-DDTHH:mm). When not provided, time is assumed to be 00:01
    :type from_date_time: str
    :param accept: http header: application/json or application/xml (Acceptable values are: \&quot;application/json\&quot;, \&quot;application/xml\&quot;)
    :type accept: str
    :param direct_flights: Show only direct flights (false&#x3D;0, true&#x3D;1). Default is false
    :type direct_flights: bool
    :param limit: Number of records returned per request. Defaults to 20, maximum is 100 (if a value bigger than 100 is given, 100 will be taken)
    :type limit: str
    :param offset: Number of records skipped. Defaults to 0
    :type offset: str

    """
    return web.Response(status=200)
