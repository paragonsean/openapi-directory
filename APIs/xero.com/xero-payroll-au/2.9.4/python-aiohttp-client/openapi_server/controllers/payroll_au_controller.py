from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_exception import APIException
from openapi_server.models.employee import Employee
from openapi_server.models.employees import Employees
from openapi_server.models.leave_application import LeaveApplication
from openapi_server.models.leave_applications import LeaveApplications
from openapi_server.models.pay_item import PayItem
from openapi_server.models.pay_items import PayItems
from openapi_server.models.pay_run import PayRun
from openapi_server.models.pay_runs import PayRuns
from openapi_server.models.payroll_calendar import PayrollCalendar
from openapi_server.models.payroll_calendars import PayrollCalendars
from openapi_server.models.payslip_lines import PayslipLines
from openapi_server.models.payslip_object import PayslipObject
from openapi_server.models.payslips import Payslips
from openapi_server.models.settings_object import SettingsObject
from openapi_server.models.super_fund import SuperFund
from openapi_server.models.super_fund_products import SuperFundProducts
from openapi_server.models.super_funds import SuperFunds
from openapi_server.models.timesheet import Timesheet
from openapi_server.models.timesheet_object import TimesheetObject
from openapi_server.models.timesheets import Timesheets
from openapi_server import util


async def create_employee(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a payroll employee

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [Employee.from_dict(d) for d in body]
    return web.Response(status=200)


async def create_leave_application(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a leave application

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [LeaveApplication.from_dict(d) for d in body]
    return web.Response(status=200)


async def create_pay_item(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a pay item

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PayItem.from_dict(body)
    return web.Response(status=200)


async def create_pay_run(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a pay run

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PayRun.from_dict(d) for d in body]
    return web.Response(status=200)


async def create_payroll_calendar(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a Payroll Calendar

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PayrollCalendar.from_dict(d) for d in body]
    return web.Response(status=200)


async def create_superfund(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a superfund

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [SuperFund.from_dict(d) for d in body]
    return web.Response(status=200)


async def create_timesheet(request: web.Request, xero_tenant_id, body) -> web.Response:
    """Creates a timesheet

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [Timesheet.from_dict(d) for d in body]
    return web.Response(status=200)


async def get_employee(request: web.Request, xero_tenant_id, employee_id) -> web.Response:
    """Retrieves an employee&#39;s detail by unique employee id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param employee_id: Employee id for single object
    :type employee_id: str
    :type employee_id: str

    """
    return web.Response(status=200)


async def get_employees(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Searches payroll employees

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 employees will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def get_leave_application(request: web.Request, xero_tenant_id, leave_application_id) -> web.Response:
    """Retrieves a leave application by a unique leave application id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param leave_application_id: Leave Application id for single object
    :type leave_application_id: str
    :type leave_application_id: str

    """
    return web.Response(status=200)


async def get_leave_applications(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves leave applications

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def get_pay_items(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves pay items

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def get_pay_run(request: web.Request, xero_tenant_id, pay_run_id) -> web.Response:
    """Retrieves a pay run by using a unique pay run id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param pay_run_id: PayRun id for single object
    :type pay_run_id: str
    :type pay_run_id: str

    """
    return web.Response(status=200)


async def get_pay_runs(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves pay runs

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 PayRuns will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def get_payroll_calendar(request: web.Request, xero_tenant_id, payroll_calendar_id) -> web.Response:
    """Retrieves payroll calendar by using a unique payroll calendar ID

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payroll_calendar_id: Payroll Calendar id for single object
    :type payroll_calendar_id: str
    :type payroll_calendar_id: str

    """
    return web.Response(status=200)


async def get_payroll_calendars(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves payroll calendars

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 objects will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def get_payslip(request: web.Request, xero_tenant_id, payslip_id) -> web.Response:
    """Retrieves for a payslip by a unique payslip id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payslip_id: Payslip id for single object
    :type payslip_id: str
    :type payslip_id: str

    """
    return web.Response(status=200)


async def get_settings(request: web.Request, xero_tenant_id) -> web.Response:
    """Retrieves payroll settings

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str

    """
    return web.Response(status=200)


async def get_superfund(request: web.Request, xero_tenant_id, super_fund_id) -> web.Response:
    """Retrieves a superfund by using a unique superfund ID

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param super_fund_id: Superfund id for single object
    :type super_fund_id: str
    :type super_fund_id: str

    """
    return web.Response(status=200)


async def get_superfund_products(request: web.Request, xero_tenant_id, abn=None, usi=None) -> web.Response:
    """Retrieves superfund products

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param abn: The ABN of the Regulated SuperFund
    :type abn: str
    :param usi: The USI of the Regulated SuperFund
    :type usi: str

    """
    return web.Response(status=200)


async def get_superfunds(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves superfunds

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 SuperFunds will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def get_timesheet(request: web.Request, xero_tenant_id, timesheet_id) -> web.Response:
    """Retrieves a timesheet by using a unique timesheet id

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param timesheet_id: Timesheet id for single object
    :type timesheet_id: str
    :type timesheet_id: str

    """
    return web.Response(status=200)


async def get_timesheets(request: web.Request, xero_tenant_id, if_modified_since=None, where=None, order=None, page=None) -> web.Response:
    """Retrieves timesheets

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param if_modified_since: Only records created or modified since this timestamp will be returned
    :type if_modified_since: str
    :param where: Filter by an any element
    :type where: str
    :param order: Order by an any element
    :type order: str
    :param page: e.g. page&#x3D;1 – Up to 100 timesheets will be returned in a single API call
    :type page: int

    """
    return web.Response(status=200)


async def update_employee(request: web.Request, xero_tenant_id, employee_id, body=None) -> web.Response:
    """Updates an employee&#39;s detail

    Update properties on a single employee

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param employee_id: Employee id for single object
    :type employee_id: str
    :type employee_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [Employee.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_leave_application(request: web.Request, xero_tenant_id, leave_application_id, body) -> web.Response:
    """Updates a specific leave application

    

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param leave_application_id: Leave Application id for single object
    :type leave_application_id: str
    :type leave_application_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [LeaveApplication.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_pay_run(request: web.Request, xero_tenant_id, pay_run_id, body=None) -> web.Response:
    """Updates a pay run

    Update properties on a single PayRun

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param pay_run_id: PayRun id for single object
    :type pay_run_id: str
    :type pay_run_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PayRun.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_payslip(request: web.Request, xero_tenant_id, payslip_id, body=None) -> web.Response:
    """Updates a payslip

    Update lines on a single payslips

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param payslip_id: Payslip id for single object
    :type payslip_id: str
    :type payslip_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [PayslipLines.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_superfund(request: web.Request, xero_tenant_id, super_fund_id, body=None) -> web.Response:
    """Updates a superfund

    Update properties on a single Superfund

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param super_fund_id: Superfund id for single object
    :type super_fund_id: str
    :type super_fund_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [SuperFund.from_dict(d) for d in body]
    return web.Response(status=200)


async def update_timesheet(request: web.Request, xero_tenant_id, timesheet_id, body=None) -> web.Response:
    """Updates a timesheet

    Update properties on a single timesheet

    :param xero_tenant_id: Xero identifier for Tenant
    :type xero_tenant_id: str
    :param timesheet_id: Timesheet id for single object
    :type timesheet_id: str
    :type timesheet_id: str
    :param body: 
    :type body: list | bytes

    """
    body = [Timesheet.from_dict(d) for d in body]
    return web.Response(status=200)
