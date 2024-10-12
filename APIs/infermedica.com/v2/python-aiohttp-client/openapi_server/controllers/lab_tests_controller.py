from typing import List, Dict
from aiohttp import web

from openapi_server.models.lab_test_details import LabTestDetails
from openapi_server.models.lab_test_public import LabTestPublic
from openapi_server import util


async def get_all_lab_tests(request: web.Request, age_value=None, age_unit=None) -> web.Response:
    """List all lab tests

    Returns a list of all available lab tests.

    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str

    """
    return web.Response(status=200)


async def get_lab_test(request: web.Request, id, age_value=None, age_unit=None) -> web.Response:
    """Get lab test by id

    Returns details of a single lab test specified by id parameter.

    :param id: lab test id
    :type id: str
    :param age_value: age value
    :type age_value: int
    :param age_unit: unit in which age value was provided
    :type age_unit: str

    """
    return web.Response(status=200)
