from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_arrivals_and_departures_by_crs(request: web.Request, crs, api_key, num_services=None, time_offset=None, time_window=None, service_details=None, filter_station=None, filter_type=None) -> web.Response:
    """getArrivalsAndDeparturesByCRS is used to get a list of services arriving to and departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

    

    :param crs: The CRS (Computer Reservation System) for the Station you wish to get departure and arrival information for, e.g. KGX for London Kings Cross.
    :type crs: str
    :param api_key: The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    :type api_key: str
    :param num_services: The number of arriving and departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services arriving to or departing from this station within the time window specified.
    :type num_services: int
    :param time_offset: The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes.
    :type time_offset: int
    :param time_window: The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes.
    :type time_window: int
    :param service_details: Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    :type service_details: bool
    :param filter_station: The CRS (Computer Reservation System) code to filter the results by. When setting this you must also set the filterType parameter. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading) and filterType to from, will only show services arriving to London Paddington that stopped at Reading. Setting a filter for getArrivalsAndDeparturesByCRS is similar to performing a getArrivalsByCRS or getDeparturesByCRS lookup, with the appropriate filterStation parameter. However using the getArrivalsAndDeparturesByCRS endpoint shows more details for each of the returned services.
    :type filter_station: str
    :param filter_type: Determines if the filterStation parameter should be applied for services arriving to, or leaving from the selected station. Required if filterStation is set.
    :type filter_type: str

    """
    return web.Response(status=200)


async def get_arrivals_by_crs(request: web.Request, crs, api_key, num_services=None, time_offset=None, time_window=None, service_details=None, filter_station=None) -> web.Response:
    """getArrivalsByCRS is used to get a list of services arriving to a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

    

    :param crs: The CRS (Computer Reservation System) for the Station you wish to get arrival information for, e.g. KGX for London Kings Cross.
    :type crs: str
    :param api_key: The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    :type api_key: str
    :param num_services: The number of arriving train services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running to this station within the time window specified.
    :type num_services: int
    :param time_offset: The time window in minutes to offset the arrival information by. For example, a value of 20 will not show services arriving within the next 20 minutes.
    :type time_offset: int
    :param time_window: The time window to show train services for in minutes. For example, a value of 60 will show services arriving to the station in the next 60 minutes.
    :type time_window: int
    :param service_details: Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    :type service_details: bool
    :param filter_station: The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services arriving to Paddington that stopped at Reading.
    :type filter_station: str

    """
    return web.Response(status=200)


async def get_departures_by_crs(request: web.Request, crs, api_key, num_services=None, time_offset=None, time_window=None, service_details=None, filter_station=None) -> web.Response:
    """getDeparturesByCRS is used to get a list of services departing from a UK train station by the CRS (Computer Reservation System) code. This will typically return a list of train services, but will also return any replacement bus or ferry services that are in place.

    

    :param crs: The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
    :type crs: str
    :param api_key: The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    :type api_key: str
    :param num_services: The number of departing services to return. This is a maximum value, less may be returned if there is not a sufficient amount of services running from the selected station within the time window specified.
    :type num_services: int
    :param time_offset: The time window in minutes to offset the departure information by. For example, a value of 20 will not show services departing within the next 20 minutes.
    :type time_offset: int
    :param time_window: The time window to show services for in minutes. For example, a value of 60 will show services departing the station in the next 60 minutes.
    :type time_window: int
    :param service_details: Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    :type service_details: bool
    :param filter_station: The CRS (Computer Reservation System) code to filter the results by. For example, performing a lookup for PAD (London Paddington) and setting filterStation to RED (Reading), will only show services departing from Paddington that stop at Reading.
    :type filter_station: str

    """
    return web.Response(status=200)
