from typing import List, Dict
from aiohttp import web

from openapi_server.models.absence_periods_response import AbsencePeriodsResponse
from openapi_server.models.attendance_periods_response import AttendancePeriodsResponse
from openapi_server.models.company_time_off_types_get200_response import CompanyTimeOffTypesGet200Response
from openapi_server.models.company_time_offs_post201_response import CompanyTimeOffsPost201Response
from openapi_server.models.create_time_off_period_request import CreateTimeOffPeriodRequest
from openapi_server.models.detailed_error_response import DetailedErrorResponse
from openapi_server.models.employee_response import EmployeeResponse
from openapi_server.models.employees_response import EmployeesResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.new_attendance_period_request import NewAttendancePeriodRequest
from openapi_server.models.new_attendance_period_response import NewAttendancePeriodResponse
from openapi_server.models.response import Response
from openapi_server.models.update_attendance_period_request import UpdateAttendancePeriodRequest
from openapi_server import util


async def company_attendances_get(request: web.Request, start_date, end_date, updated_from=None, updated_to=None, employees=None, limit=None, offset=None) -> web.Response:
    """company_attendances_get

    This endpoint is responsible for fetching attendance data for the company employees. It is possible to paginate results, filter by period, the date and/or time it was updated, and/or specific employees. The result will contain a list of attendance periods, structured as defined here.

    :param start_date: First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results
    :type start_date: str
    :param end_date: Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results.
    :type end_date: str
    :param updated_from: Datetime from when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_from will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone.
    :type updated_from: str
    :param updated_to: Datetime until when the queried periods have been updated. Same format as updated_at. It is inclusive, so the day specified as updated_to will also be considered on the results. Can be just the date, or the date and the time, with or without the timezone.
    :type updated_to: str
    :param employees: A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned.
    :type employees: List[int]
    :param limit: Pagination attribute to limit how many attendances will be returned per page
    :type limit: int
    :param offset: Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
    :type offset: int

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def company_attendances_id_delete(request: web.Request, id) -> web.Response:
    """company_attendances_id_delete

    This endpoint is responsible for deleting attendance data for the company employees.

    :param id: ID of the attendance period to delete
    :type id: int

    """
    return web.Response(status=200)


async def company_attendances_id_patch(request: web.Request, id, body) -> web.Response:
    """company_attendances_id_patch

    This endpoint is responsible for updating attendance data for the company employees. Attributes are not required and if not specified, the current value will be used. It is not possible to change the employee id.

    :param id: ID of the attendance period to update
    :type id: int
    :param body: attendance period data to update
    :type body: dict | bytes

    """
    body = UpdateAttendancePeriodRequest.from_dict(body)
    return web.Response(status=200)


async def company_attendances_post(request: web.Request, body) -> web.Response:
    """company_attendances_post

    This endpoint is responsible for adding attendance data for the company employees. It is possible to add attendances for one or many employees at the same time. The payload sent on the request should be a list of attendance periods, in the form of an array containing attendance period objects.

    :param body: List of attendance periods to create
    :type body: dict | bytes

    """
    body = NewAttendancePeriodRequest.from_dict(body)
    return web.Response(status=200)


async def company_employees_employee_id_get(request: web.Request, employee_id) -> web.Response:
    """company_employees_employee_id_get

    Show employee by ID

    :param employee_id: Numeric &#x60;id&#x60; of the employee
    :type employee_id: int

    """
    return web.Response(status=200)


async def company_employees_employee_id_profile_picture_width_get(request: web.Request, employee_id, width) -> web.Response:
    """company_employees_employee_id_profile_picture_width_get

    Show employee profile picture

    :param employee_id: Numeric &#x60;id&#x60; of the employee
    :type employee_id: int
    :param width: Width of the image. Default 75x75
    :type width: int

    """
    return web.Response(status=200)


async def company_employees_get(request: web.Request, ) -> web.Response:
    """company_employees_get

    List Employees


    """
    return web.Response(status=200)


async def company_employees_post(request: web.Request, employee_email, employee_first_name, employee_last_name, employee_department=None, employee_gender=None, employee_hire_date=None, employee_position=None, employee_weekly_hours=None) -> web.Response:
    """Create an employee

    Creates new employee. Status of the employee will be set to &#x60;active&#x60; if &#x60;hire_date&#x60; provided is in past. Otherwise status will be set to &#x60;onboarding&#x60;. This endpoint will respond with &#x60;id&#x60; of created employee in case of success. 

    :param employee_email: Employee email
    :type employee_email: str
    :param employee_first_name: Employee first name
    :type employee_first_name: str
    :param employee_last_name: Employee last name
    :type employee_last_name: str
    :param employee_department: Employee department
    :type employee_department: str
    :param employee_gender: Employee gender
    :type employee_gender: str
    :param employee_hire_date: Employee hire date
    :type employee_hire_date: str
    :param employee_position: Employee position
    :type employee_position: str
    :param employee_weekly_hours: Employee weekly working hours
    :type employee_weekly_hours: 

    """
    employee_hire_date = util.deserialize_date(employee_hire_date)
    return web.Response(status=200)


async def company_time_off_types_get(request: web.Request, limit=None, offset=None) -> web.Response:
    """company_time_off_types_get

    Provides a list of available time-off types, for example &#39;Paid vacation&#39;, &#39;Parental leave&#39; or &#39;Home office&#39;

    :param limit: Pagination attribute to limit how many records will be returned per page
    :type limit: int
    :param offset: Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
    :type offset: int

    """
    return web.Response(status=200)


async def company_time_offs_get(request: web.Request, start_date=None, end_date=None, updated_from=None, updated_to=None, employees=None, limit=None, offset=None) -> web.Response:
    """company_time_offs_get

    This endpoint is responsible for fetching absence data for the company employees. It is possible to paginate results, filter by period and/or specific employees. The result will contain a list of absence periods, structured as defined here.

    :param start_date: First day of the period to be queried. It is inclusive, so the day specified as start_date will also be considered on the results
    :type start_date: str
    :param end_date: Last day of the period to be queried. It is inclusive, so the day specified as end_date will also be considered on the results.
    :type end_date: str
    :param updated_from: Datetime from when the queried periods have been updated. It is inclusive, so the day specified as updated_from will also be considered on the results.
    :type updated_from: str
    :param updated_to: Datetime until when the queried periods have been updated. It is inclusive, so the day specified as updated_to will also be considered on the results.
    :type updated_to: str
    :param employees: A list of Personio employee identifiers to filter the results. Only those employees specified here will be returned.
    :type employees: List[int]
    :param limit: Pagination attribute to limit how many attendances will be returned per page
    :type limit: int
    :param offset: Pagination attribute to identify which page you are requesting, by the form of telling an offset from the first record that would be returned.
    :type offset: int

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    return web.Response(status=200)


async def company_time_offs_id_delete(request: web.Request, id) -> web.Response:
    """company_time_offs_id_delete

    This endpoint is responsible for deleting absence period data for the company employees.

    :param id: ID of the absence period to delete
    :type id: int

    """
    return web.Response(status=200)


async def company_time_offs_id_get(request: web.Request, id) -> web.Response:
    """company_time_offs_id_get

    Absence Period

    :param id: Numeric &#x60;id&#x60; of the absence period
    :type id: int

    """
    return web.Response(status=200)


async def company_time_offs_post(request: web.Request, body) -> web.Response:
    """company_time_offs_post

    This endpoint is responsible for adding absence data for the company employees.

    :param body: Absence period to create
    :type body: dict | bytes

    """
    body = CreateTimeOffPeriodRequest.from_dict(body)
    return web.Response(status=200)
