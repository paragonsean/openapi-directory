from typing import List, Dict
from aiohttp import web

from openapi_server.models.employee import Employee
from openapi_server.models.employee_info import EmployeeInfo
from openapi_server.models.error import Error
from openapi_server import util


async def get_all_employees(request: web.Request, company_id, pagesize=None, pagenumber=None, includetotalcount=None) -> web.Response:
    """Get all employees

    Get All Employees API will return employee data currently available in Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param pagesize: Number of records per page. Default value is 25.
    :type pagesize: int
    :param pagenumber: Page number to retrieve; page numbers are 0-based (so to get the first page of results, pass pagenumber&#x3D;0). Default value is 0.
    :type pagenumber: int
    :param includetotalcount: Whether to include the total record count in the header&#39;s X-Pcty-Total-Count property. Default value is true.
    :type includetotalcount: bool

    """
    return web.Response(status=200)


async def get_employee(request: web.Request, company_id, employee_id) -> web.Response:
    """Get employee

    Get Employee API will return employee data currently available in Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str

    """
    return web.Response(status=200)


async def update_employee(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Update employee

    Update Employee API will update existing employee data in WebPay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: Employee Model
    :type body: dict | bytes

    """
    body = Employee.from_dict(body)
    return web.Response(status=200)
