from typing import List, Dict
from aiohttp import web

from openapi_server.models.employee_hours_get200_response import EmployeeHoursGet200Response
from openapi_server import util


async def employee_hours_get(request: web.Request, date_from, date_to) -> web.Response:
    """Used to retrieve details about the logged in user&#39;s hours

    

    :param date_from: Date formatted as Y-m-d (2016-06-28)
    :type date_from: str
    :param date_to: Date formatted as Y-m-d (2016-06-28)
    :type date_to: str

    """
    return web.Response(status=200)
