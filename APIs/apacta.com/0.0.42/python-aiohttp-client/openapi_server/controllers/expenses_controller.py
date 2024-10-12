from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expenses_expense_id_get200_response import ExpensesExpenseIdGet200Response
from openapi_server.models.expenses_get200_response import ExpensesGet200Response
from openapi_server.models.expenses_highest_amount_get200_response import ExpensesHighestAmountGet200Response
from openapi_server.models.expenses_post_request import ExpensesPostRequest
from openapi_server import util


async def bulk_delete_expenses(request: web.Request, body) -> web.Response:
    """Bulk delete expenses

    

    :param body: expense ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)


async def expenses_expense_id_delete(request: web.Request, expense_id) -> web.Response:
    """Delete expense

    

    :param expense_id: 
    :type expense_id: str

    """
    return web.Response(status=200)


async def expenses_expense_id_get(request: web.Request, expense_id) -> web.Response:
    """Show expense

    

    :param expense_id: 
    :type expense_id: str

    """
    return web.Response(status=200)


async def expenses_expense_id_put(request: web.Request, expense_id) -> web.Response:
    """Edit expense

    

    :param expense_id: 
    :type expense_id: str

    """
    return web.Response(status=200)


async def expenses_get(request: web.Request, created_by_id=None, company_id=None, contact_id=None, project_id=None, due_date=None, gt_created=None, lt_created=None, status=None, is_imported=None, min_amount=None, max_amount=None, projects=None) -> web.Response:
    """Show list of expenses

    

    :param created_by_id: 
    :type created_by_id: str
    :type created_by_id: str
    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param contact_id: 
    :type contact_id: str
    :type contact_id: str
    :param project_id: 
    :type project_id: str
    :type project_id: str
    :param due_date: Filter by [valid&#x3D;records in future including today], [exceeded&#x3D;records in past] or [null&#x3D;all records]
    :type due_date: str
    :param gt_created: Created after date
    :type gt_created: str
    :param lt_created: Created before date
    :type lt_created: str
    :param status: Filter by status identifier. [null&#x3D;all records]
    :type status: str
    :param is_imported: 
    :type is_imported: bool
    :param min_amount: Expenses &#x60;total_selling_price&#x60; &gt; &#x60;min_amount&#x60;
    :type min_amount: float
    :param max_amount: Expenses &#x60;total_selling_price&#x60; &lt; &#x60;max_amount&#x60;
    :type max_amount: float
    :param projects: You can select &#x60;all projects&#x60;, &#x60;no projects&#x60; or select &#x60;multiple projects&#x60;
    :type projects: str

    """
    gt_created = util.deserialize_date(gt_created)
    lt_created = util.deserialize_date(lt_created)
    return web.Response(status=200)


async def expenses_highest_amount_get(request: web.Request, gt_created, lt_created) -> web.Response:
    """Show highest Expense amount(&#x60;total_selling_price&#x60;)

    

    :param gt_created: Used to filter time range
    :type gt_created: str
    :param lt_created: Used to filter time range
    :type lt_created: str

    """
    gt_created = util.deserialize_date(gt_created)
    lt_created = util.deserialize_date(lt_created)
    return web.Response(status=200)


async def expenses_post(request: web.Request, body=None) -> web.Response:
    """Add line to expense

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExpensesPostRequest.from_dict(body)
    return web.Response(status=200)


async def send_emails_expenses(request: web.Request, body) -> web.Response:
    """Bulk delete expenses

    

    :param body: expense ids
    :type body: dict | bytes

    """
    body = BulkActionRequestBody.from_dict(body)
    return web.Response(status=200)
