from typing import List, Dict
from aiohttp import web

from openapi_server.models.count_result import CountResult
from openapi_server.models.error_result import ErrorResult
from openapi_server import util


async def age(request: web.Request, location, age_group, occurence_type, hour) -> web.Response:
    """Presence in a location aggregated by age

    Get count of people in a given location and an hour, aggregated by age.

    :param location: basic residential unit
    :type location: str
    :param age_group: age-group specification (1: 8-18, 2: 19-25, 3: 26-35, 4: 36-55, 5: 56+)
    :type age_group: str
    :param occurence_type: occurence type in the basic residential unit (1 - transit, 2 - visit)
    :type occurence_type: str
    :param hour: time interval for the count aggregation (from 0 to 23)
    :type hour: str

    """
    return web.Response(status=200)


async def gender(request: web.Request, location, g, occurence_type, hour) -> web.Response:
    """Presence in a location aggregated by gender

    Get count of people in a given location and an hour, aggregated by gender.

    :param location: basic residential unit
    :type location: str
    :param g: gender specification (1 - male, 2 - female)
    :type g: str
    :param occurence_type: occurence type in the basic residential unit (1 - transit, 2 - visit)
    :type occurence_type: str
    :param hour: time interval for the count aggregation (from 0 to 23)
    :type hour: str

    """
    return web.Response(status=200)
