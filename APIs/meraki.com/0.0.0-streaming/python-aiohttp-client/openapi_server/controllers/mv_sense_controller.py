from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_device_camera_analytics_live(request: web.Request, serial) -> web.Response:
    """Returns live state from camera of analytics zones

    Returns live state from camera of analytics zones

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_overview(request: web.Request, serial, t0=None, t1=None, timespan=None, object_type=None) -> web.Response:
    """Returns an overview of aggregate analytics data for a timespan

    Returns an overview of aggregate analytics data for a timespan

    :param serial: 
    :type serial: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
    :type timespan: float
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_recent(request: web.Request, serial, object_type=None) -> web.Response:
    """Returns most recent record for analytics zones

    Returns most recent record for analytics zones

    :param serial: 
    :type serial: str
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_zone_history(request: web.Request, serial, zone_id, t0=None, t1=None, timespan=None, resolution=None, object_type=None) -> web.Response:
    """Return historical records for analytic zones

    Return historical records for analytic zones

    :param serial: 
    :type serial: str
    :param zone_id: 
    :type zone_id: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 14 hours after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 14 hours. The default is 1 hour.
    :type timespan: float
    :param resolution: The time resolution in seconds for returned data. The valid resolutions are: 60. The default is 60.
    :type resolution: int
    :param object_type: [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    :type object_type: str

    """
    return web.Response(status=200)


async def get_device_camera_analytics_zones(request: web.Request, serial) -> web.Response:
    """Returns all configured analytic zones for this camera

    Returns all configured analytic zones for this camera

    :param serial: 
    :type serial: str

    """
    return web.Response(status=200)
