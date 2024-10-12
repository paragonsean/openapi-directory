from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_organization_sensor_readings_latest200_response_inner import GetOrganizationSensorReadingsLatest200ResponseInner
from openapi_server import util


async def get_organization_sensor_readings_latest_2(request: web.Request, organization_id, per_page=None, starting_after=None, ending_before=None, network_ids=None, serials=None, metrics=None) -> web.Response:
    """Return the latest available reading for each metric from each sensor, sorted by sensor serial

    Return the latest available reading for each metric from each sensor, sorted by sensor serial

    :param organization_id: 
    :type organization_id: str
    :param per_page: The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
    :type per_page: int
    :param starting_after: A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type starting_after: str
    :param ending_before: A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    :type ending_before: str
    :param network_ids: Optional parameter to filter readings by network.
    :type network_ids: List[str]
    :param serials: Optional parameter to filter readings by sensor.
    :type serials: List[str]
    :param metrics: Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    :type metrics: List[str]

    """
    return web.Response(status=200)
