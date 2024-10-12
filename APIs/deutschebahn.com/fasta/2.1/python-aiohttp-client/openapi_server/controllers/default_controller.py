from typing import List, Dict
from aiohttp import web

from openapi_server.models.facility import Facility
from openapi_server.models.station import Station
from openapi_server import util


async def find_facilities(request: web.Request, type=None, state=None, equipmentnumbers=None, stationnumber=None, area=None) -> web.Response:
    """find_facilities

    Access to public facilities (escalators and elevators) in railway stations

    :param type: Type of the facility.
    :type type: List[str]
    :param state: Operational state of the facility.
    :type state: List[str]
    :param equipmentnumbers: List of equipmentnumbers to select.
    :type equipmentnumbers: List[int]
    :param stationnumber: Number of the station the facilities belong to.
    :type stationnumber: int
    :param area: Geo coordinate rectangle in WGS84-format to filter facilities by geographical position. Parameters must be 4 numbers exactly as follows: longitudeWest, latitudeSouth, longitudeEast, latitudeNorth.
    :type area: List[str]

    """
    return web.Response(status=200)


async def find_station_by_station_number(request: web.Request, stationnumber) -> web.Response:
    """find_station_by_station_number

    Returns information about a station (and its corresponding facilities) identified by a stationnumber.

    :param stationnumber: Number of the station to fetch.
    :type stationnumber: int

    """
    return web.Response(status=200)


async def get_facility_by_equipment_number(request: web.Request, equipmentnumber) -> web.Response:
    """get_facility_by_equipment_number

    Returns the facility identified by its equipmentnumber.

    :param equipmentnumber: Equipmentnumber of the facility to fetch.
    :type equipmentnumber: int

    """
    return web.Response(status=200)
