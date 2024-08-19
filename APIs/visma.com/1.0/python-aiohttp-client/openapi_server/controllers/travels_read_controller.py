from typing import List, Dict
from aiohttp import web

from openapi_server.models.deleted_project_travel_expense_model import DeletedProjectTravelExpenseModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.expenses_class import ExpensesClass
from openapi_server.models.project_travel_expense_output_model import ProjectTravelExpenseOutputModel
from openapi_server.models.travel_reimbursement_output_model import TravelReimbursementOutputModel
from openapi_server import util


async def project_travel_expenses_get_deleted_project_travel_expenses(request: web.Request, page_token=None, row_count=None, project_guid=None, user_guid=None, deleted_since=None) -> web.Response:
    """Get the deleted project travel expenses.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param project_guid: Optional: ID of the project for the deleted project travel expenses to be fetched. If not provided, returns for all projects. Default all.
    :type project_guid: List[str]
    :param user_guid: Optional: ID of the user. If not provided, returns for all users. Default all.
    :type user_guid: List[str]
    :param deleted_since: Optional: Get project travel expenses that have been deleted after this date time (greater or equal).
    :type deleted_since: str

    """
    deleted_since = util.deserialize_datetime(deleted_since)
    return web.Response(status=200)


async def project_travel_expenses_get_project_travel_expense(request: web.Request, guid) -> web.Response:
    """Get project travel expense by ID.

    

    :param guid: Id used to get the project travel expense.
    :type guid: str

    """
    return web.Response(status=200)


async def project_travel_expenses_get_project_travel_expenses(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get the project travel expenses.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get project travel expenses that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_travel_expenses_get_project_travel_expenses_for_project(request: web.Request, project_guid, is_billable=None, is_billed=None, invoiceable_date=None, page_token=None, row_count=None, is_billable_period_in_future=None, expense_class=None) -> web.Response:
    """Get all the project travel expenses for a project

    

    :param project_guid: ID of the project.
    :type project_guid: str
    :param is_billable: Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool
    :param is_billed: Optional: Filter the travel expenses. If true/false, only the ones that are/are not invoiced are returned. If null, all are returned. Default is null.
    :type is_billed: bool
    :param invoiceable_date: Optional: Filter the project fees. When given, only the ones that are invoiceable before or on the given date are returned. Default is null.
    :type invoiceable_date: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param is_billable_period_in_future: Optional. Filter the project travel expenses. If true/false, only the ones that will be billable in the future are returned. If null, all are returned. Default is false.
    :type is_billable_period_in_future: bool
    :param expense_class: Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    :type expense_class: dict | bytes

    """
    invoiceable_date = util.deserialize_datetime(invoiceable_date)
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def project_travel_expenses_get_project_travel_expenses_for_travel_reimbursement(request: web.Request, travel_reimbursement_guid, page_token=None, row_count=None, expense_class=None) -> web.Response:
    """Get all the project travel expenses for a travel reimbursement

    

    :param travel_reimbursement_guid: Optional: ID of the travel reimbursement
    :type travel_reimbursement_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param expense_class: Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    :type expense_class: dict | bytes

    """
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def project_travel_expenses_get_project_travel_expenses_for_user(request: web.Request, user_guid, start_date=None, end_date=None, page_token=None, row_count=None, expense_class=None, is_reimbursed=None, is_travel_reimbursement_required=None, travel_reimbursement_guid=None, cost_currency_guid=None) -> web.Response:
    """Get all the project travel expenses for a user

    

    :param user_guid: ID of the user.
    :type user_guid: str
    :param start_date: Optional: starting date from which to get the travel expenses. Default all.
    :type start_date: str
    :param end_date: Optional: starting date to which to get the travel expenses. Default all.
    :type end_date: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param expense_class: Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    :type expense_class: dict | bytes
    :param is_reimbursed: Optional. Filter the project travel expenses. If true/false, only the ones that are reimbursed are returned. If null, all are returned. Default is null.
    :type is_reimbursed: bool
    :param is_travel_reimbursement_required: Optional: Filter the project travel expenses by whether or not the reimbursement is required. Default all.
    :type is_travel_reimbursement_required: bool
    :param travel_reimbursement_guid: Optional: ID of the travel reimbursement
    :type travel_reimbursement_guid: str
    :param cost_currency_guid: Optional: ID of the cost currency.
    :type cost_currency_guid: str

    """
    start_date = util.deserialize_date(start_date)
    end_date = util.deserialize_date(end_date)
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def travel_reimbursements_get_travel_reimbursement(request: web.Request, guid) -> web.Response:
    """Get travel reimbursement by ID

    

    :param guid: ID of travel reimbursement
    :type guid: str

    """
    return web.Response(status=200)


async def travel_reimbursements_get_travel_reimbursements(request: web.Request, page_token=None, row_count=None, changed_since=None, travel_reimbursement_status_guids=None) -> web.Response:
    """Get travel reimbursements.

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param changed_since: Optional: Get travel reimbursements that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param travel_reimbursement_status_guids: Optional: List of travel reimbursement status ids.
    :type travel_reimbursement_status_guids: List[str]

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)
