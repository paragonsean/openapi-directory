from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_network_alerts_history200_response_inner import GetNetworkAlertsHistory200ResponseInner
from openapi_server.models.get_organization_sensor_readings_history200_response_inner import GetOrganizationSensorReadingsHistory200ResponseInner
from openapi_server import util


async def get_device_camera_analytics_zone_history_3(request: web.Request, serial, zone_id, t0=None, t1=None, timespan=None, resolution=None, object_type=None) -> web.Response:
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


async def get_network_alerts_history_2(request: web.Request, network_id, per_page=None, starting_after=None, ending_before=None) -> web.Response:
    """Return the alert history for this network

    Return the alert history for this network

    :param network_id: 
    :type network_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str

    """
    return web.Response(status=200)


async def get_organization_sensor_readings_history_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, t0=None, t1=None, timespan=None, network_ids=None, serials=None, metrics=None) -> web.Response:
    """Return all reported readings from sensors in a given timespan, sorted by timestamp

    Return all reported readings from sensors in a given timespan, sorted by timestamp

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param t0: The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
    :type t0: str
    :param t1: The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    :type t1: str
    :param timespan: The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    :type timespan: float
    :param network_ids: Optional parameter to filter readings by network.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter readings by sensor.
    :type serials: List[str]
    :param metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    :type metrics: List[str]

    """
    return web.Response(status=200)
