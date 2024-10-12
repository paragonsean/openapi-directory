from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_fastest_departures_by_crs(request: web.Request, crs, api_key, filter_list, time_offset=None, time_window=None, service_details=None) -> web.Response:
    """getFastestDeparturesByCRS is used to get the fastest next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place.

    

    :param crs: The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
    :type crs: str
    :param api_key: The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    :type api_key: str
    :param filter_list: The CRS (Computer Reservation System) codes to show the fastest departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD.
    :type filter_list: str
    :param time_offset: The time window in minutes to offset the departure information by. For example, a value of 20 will show the fastest services departing after 20 minutes.
    :type time_offset: int
    :param time_window: The time window to show train services for in minutes. For example, a value of 60 will show the fastest services departing the station in the next 60 minutes.
    :type time_window: int
    :param service_details: Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    :type service_details: bool

    """
    return web.Response(status=200)


async def get_next_departures_by_crs(request: web.Request, crs, api_key, filter_list, time_offset=None, time_window=None, service_details=None) -> web.Response:
    """getNextDeparturesByCRS is used to get the next service running between two stations. Multiple destinations can be specified. This will typically return a single train service, but will also return a replacement bus or ferry service if in place. This will return the next departures for each of the filterList stations specified. It may not return the fastest next service. To get the fastest next service use the getFastestDeparturesByCRS endpoint.

    

    :param crs: The CRS (Computer Reservation System) for the station you wish to get departure information for, e.g. KGX for London Kings Cross.
    :type crs: str
    :param api_key: The National Rail OpenLDBWS API Key to use for looking up service information. You must register with National Rail to obtain this key and whitelist it with us. See https://api.departureboard.io/docs/registration for more information.
    :type api_key: str
    :param filter_list: The CRS (Computer Reservation System) codes to show departing services to. Up to 20 destination stations can be specified. These should be split by a comma, for example HAY,EAL,PAD.
    :type filter_list: str
    :param time_offset: The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the station within the next 20 minutes.
    :type time_offset: int
    :param time_window: The time window in minutes to offset the arrival and departure information by. For example, a value of 20 will not show services arriving to or departing from the selected station within the next 20 minutes.
    :type time_window: int
    :param service_details: Should the response contain information on the calling points for each service? If set to false, calling points will not be returned.
    :type service_details: bool

    """
    return web.Response(status=200)
