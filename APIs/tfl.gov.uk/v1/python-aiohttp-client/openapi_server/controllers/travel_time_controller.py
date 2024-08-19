from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def travel_time_get_compare_overlay(request: web.Request, z, pin_lat, pin_lon, map_center_lat, map_center_lon, scenario_title, time_of_day_id, mode_id, width, height, direction, travel_time_interval, compare_type, compare_value) -> web.Response:
    """Gets the TravelTime overlay.

    

    :param z: The zoom level.
    :type z: int
    :param pin_lat: The latitude of the pin.
    :type pin_lat: float
    :param pin_lon: The longitude of the pin.
    :type pin_lon: float
    :param map_center_lat: The map center latitude.
    :type map_center_lat: float
    :param map_center_lon: The map center longitude.
    :type map_center_lon: float
    :param scenario_title: The title of the scenario.
    :type scenario_title: str
    :param time_of_day_id: The id for the time of day (AM/INTER/PM)
    :type time_of_day_id: str
    :param mode_id: The id of the mode.
    :type mode_id: str
    :param width: The width of the requested overlay.
    :type width: int
    :param height: The height of the requested overlay.
    :type height: int
    :param direction: The direction of travel.
    :type direction: str
    :param travel_time_interval: The total minutes between the travel time bands
    :type travel_time_interval: int
    :param compare_type: 
    :type compare_type: str
    :param compare_value: 
    :type compare_value: str

    """
    return web.Response(status=200)


async def travel_time_get_overlay(request: web.Request, z, pin_lat, pin_lon, map_center_lat, map_center_lon, scenario_title, time_of_day_id, mode_id, width, height, direction, travel_time_interval) -> web.Response:
    """Gets the TravelTime overlay.

    

    :param z: The zoom level.
    :type z: int
    :param pin_lat: The latitude of the pin.
    :type pin_lat: float
    :param pin_lon: The longitude of the pin.
    :type pin_lon: float
    :param map_center_lat: The map center latitude.
    :type map_center_lat: float
    :param map_center_lon: The map center longitude.
    :type map_center_lon: float
    :param scenario_title: The title of the scenario.
    :type scenario_title: str
    :param time_of_day_id: The id for the time of day (AM/INTER/PM)
    :type time_of_day_id: str
    :param mode_id: The id of the mode.
    :type mode_id: str
    :param width: The width of the requested overlay.
    :type width: int
    :param height: The height of the requested overlay.
    :type height: int
    :param direction: The direction of travel.
    :type direction: str
    :param travel_time_interval: The total minutes between the travel time bands
    :type travel_time_interval: int

    """
    return web.Response(status=200)
