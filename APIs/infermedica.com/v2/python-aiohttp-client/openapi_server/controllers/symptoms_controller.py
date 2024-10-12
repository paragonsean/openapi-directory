from typing import List, Dict
from aiohttp import web

from openapi_server.models.symptom_details import SymptomDetails
from openapi_server.models.symptom_public import SymptomPublic
from openapi_server import util


async def get_all_symptoms(request: web.Request, age_value=None, age_unit=None, enable_triage_5=None) -> web.Response:
    """List all symptoms

    Returns a list of all available symptoms.

    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param enable_triage_5: enable 5-level triage values
    :type enable_triage_5: bool

    """
    return web.Response(status=200)


async def get_symptom(request: web.Request, id, age_value=None, age_unit=None, enable_triage_5=None) -> web.Response:
    """Get symptoms by id

    Returns details of a single symptom specified by id parameter.

    :param id: symptoms id
    :type id: str
    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str
    :param enable_triage_5: enable 5-level triage values
    :type enable_triage_5: bool

    """
    return web.Response(status=200)
