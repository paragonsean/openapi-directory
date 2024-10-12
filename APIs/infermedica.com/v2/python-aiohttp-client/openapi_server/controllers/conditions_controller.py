from typing import List, Dict
from aiohttp import web

from openapi_server.models.condition_details import ConditionDetails
from openapi_server.models.condition_public import ConditionPublic
from openapi_server import util


async def get_all_conditions(request: web.Request, age_value=None, age_unit=None, enable_triage_5=None) -> web.Response:
    """List all conditions

    Returns a list of all available conditions.

    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param enable_triage_5: enable 5-level triage values
    :type enable_triage_5: bool

    """
    return web.Response(status=200)


async def get_condition(request: web.Request, id, age_value=None, age_unit=None, enable_triage_5=None) -> web.Response:
    """Get condition by id

    Returns details of a single condition specified by id parameter.

    :param id: condition id
    :type id: str
    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param enable_triage_5: enable 5-level triage values
    :type enable_triage_5: bool

    """
    return web.Response(status=200)
