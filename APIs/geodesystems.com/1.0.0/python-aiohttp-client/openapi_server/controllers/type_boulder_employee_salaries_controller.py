from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def search_boulder_employee_salaries(request: web.Request, text=None, name=None, description=None, fromdate=None, todate=None, createdate_from=None, createdate_to=None, changedate_from=None, changedate_to=None, group=None, filesuffix=None, maxlatitude=None, minlongitude=None, minlatitude=None, maxlongitude=None, max=None, skip=None, search_db_boulder_employee_salaries_position_description=None, search_db_boulder_employee_salaries_department=None, search_db_boulder_employee_salaries_employee_flsa_exempt_y_n=None, search_db_boulder_employee_salaries_pay_range_min=None, search_db_boulder_employee_salaries_pay_range_max=None, search_db_boulder_employee_salaries_employee_hourly_pay_rate=None, search_db_boulder_employee_salaries_employee_fte_in_this_position=None, search_db_boulder_employee_salaries_employee_annual_base_salary=None) -> web.Response:
    """Search API for &#39;Boulder Employee Salaries&#39; entry type

    API to search for entries of type Boulder Employee Salaries

    :param text: Search text
    :type text: str
    :param name: Search name
    :type name: str
    :param description: Search description
    :type description: str
    :param fromdate: From date
    :type fromdate: str
    :param todate: To date
    :type todate: str
    :param createdate_from: Archive create date from
    :type createdate_from: str
    :param createdate_to: Archive create date to
    :type createdate_to: str
    :param changedate_from: Archive change date from
    :type changedate_from: str
    :param changedate_to: Archive change date to
    :type changedate_to: str
    :param group: Parent entry
    :type group: str
    :param filesuffix: File suffix
    :type filesuffix: str
    :param maxlatitude: Northern bounds of search
    :type maxlatitude: float
    :param minlongitude: Western bounds of search
    :type minlongitude: float
    :param minlatitude: Southern bounds of search
    :type minlatitude: float
    :param maxlongitude: Eastern bounds of search
    :type maxlongitude: float
    :param max: Max number of results
    :type max: int
    :param skip: Number to skip
    :type skip: int
    :param search_db_boulder_employee_salaries_position_description: Position Description
    :type search_db_boulder_employee_salaries_position_description: str
    :param search_db_boulder_employee_salaries_department: Department
    :type search_db_boulder_employee_salaries_department: str
    :param search_db_boulder_employee_salaries_employee_flsa_exempt_y_n: Employee Flsa Exempt Y N
    :type search_db_boulder_employee_salaries_employee_flsa_exempt_y_n: str
    :param search_db_boulder_employee_salaries_pay_range_min: Pay Range Min
    :type search_db_boulder_employee_salaries_pay_range_min: float
    :param search_db_boulder_employee_salaries_pay_range_max: Pay Range Max
    :type search_db_boulder_employee_salaries_pay_range_max: float
    :param search_db_boulder_employee_salaries_employee_hourly_pay_rate: Employee Hourly Pay Rate
    :type search_db_boulder_employee_salaries_employee_hourly_pay_rate: float
    :param search_db_boulder_employee_salaries_employee_fte_in_this_position: Employee Fte In This Position
    :type search_db_boulder_employee_salaries_employee_fte_in_this_position: float
    :param search_db_boulder_employee_salaries_employee_annual_base_salary: Employee Annual Base Salary
    :type search_db_boulder_employee_salaries_employee_annual_base_salary: float

    """
    fromdate = util.deserialize_datetime(fromdate)
    todate = util.deserialize_datetime(todate)
    createdate_from = util.deserialize_datetime(createdate_from)
    createdate_to = util.deserialize_datetime(createdate_to)
    changedate_from = util.deserialize_datetime(changedate_from)
    changedate_to = util.deserialize_datetime(changedate_to)
    return web.Response(status=200)
