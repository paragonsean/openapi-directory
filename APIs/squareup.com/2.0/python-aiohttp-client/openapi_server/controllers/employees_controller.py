from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_employees_response import ListEmployeesResponse
from openapi_server.models.retrieve_employee_response import RetrieveEmployeeResponse
from openapi_server import util


async def v2_employees_get(request: web.Request, location_id=None, status=None, limit=None, cursor=None) -> web.Response:
    """ListEmployees

    

    :param location_id: 
    :type location_id: str
    :param status: Specifies the EmployeeStatus to filter the employee by.
    :type status: str
    :param limit: The number of employees to be returned on each page.
    :type limit: int
    :param cursor: The token required to retrieve the specified page of results.
    :type cursor: str

    """
    return web.Response(status=200)


async def v2_employees_id_get(request: web.Request, id) -> web.Response:
    """RetrieveEmployee

    

    :param id: UUID for the employee that was requested.
    :type id: str

    """
    return web.Response(status=200)
