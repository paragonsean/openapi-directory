from typing import List, Dict
from aiohttp import web

from openapi_server.models.risk_factor_details import RiskFactorDetails
from openapi_server.models.risk_factor_public import RiskFactorPublic
from openapi_server import util


async def get_all_risk_factors(request: web.Request, age_value=None, age_unit=None, enable_triage_5=None) -> web.Response:
    """List all risk factors

    Returns a list of all available risk factors.

    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param enable_triage_5: enable 5-level triage values
    :type enable_triage_5: bool

    """
    return web.Response(status=200)


async def get_risk_factor(request: web.Request, id, age_value=None, age_unit=None, enable_triage_5=None) -> web.Response:
    """Get risk factor by id

    Returns details of a single risk factor specified by id parameter.

    :param id: risk factor id
    :type id: str
    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param enable_triage_5: enable 5-level triage values
    :type enable_triage_5: bool

    """
    return web.Response(status=200)
