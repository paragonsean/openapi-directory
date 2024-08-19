from typing import List, Dict
from aiohttp import web

from openapi_server.models.earning import Earning
from openapi_server.models.error import Error
from openapi_server import util


async def add_or_update_an_employee_earning(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add/Update Earning

    Add/Update Earning API sends new or updated employee earnings information directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: Earning Model
    :type body: dict | bytes

    """
    body = Earning.from_dict(body)
    return web.Response(status=200)


async def delete_earning_by_earning_code_and_start_date(request: web.Request, company_id, employee_id, earning_code, start_date) -> web.Response:
    """Delete Earning by Earning Code and Start Date

    Delete Earning by Earning Code and Start Date

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param earning_code: Earning Code
    :type earning_code: str
    :param start_date: Start Date
    :type start_date: str

    """
    return web.Response(status=200)


async def get_all_earnings(request: web.Request, company_id, employee_id) -> web.Response:
    """Get All Earnings

    Get All Earnings returns all earnings for the selected employee.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str

    """
    return web.Response(status=200)


async def get_earning_by_earning_code_and_start_date(request: web.Request, company_id, employee_id, earning_code, start_date) -> web.Response:
    """Get Earning by Earning Code and Start Date

    Get Earnings returns the single earning with the provided earning code and start date for the selected employee.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param earning_code: Earning Code
    :type earning_code: str
    :param start_date: Start Date
    :type start_date: str

    """
    return web.Response(status=200)


async def get_earnings_by_earning_code(request: web.Request, company_id, employee_id, earning_code) -> web.Response:
    """Get Earnings by Earning Code

    Get Earnings returns all earnings with the provided earning code for the selected employee.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param earning_code: Earning Code
    :type earning_code: str

    """
    return web.Response(status=200)
