from typing import List, Dict
from aiohttp import web

from openapi_server.models.expense_attachment_request import ExpenseAttachmentRequest
from openapi_server.models.expense_attachment_upload_result import ExpenseAttachmentUploadResult
from openapi_server.models.expense_delete_result_set import ExpenseDeleteResultSet
from openapi_server.models.expense_details import ExpenseDetails
from openapi_server.models.expense_list import ExpenseList
from openapi_server.models.new_expense import NewExpense
from openapi_server.models.update_expense import UpdateExpense
from openapi_server import util


async def expense_approval(request: web.Request, expense_ids, user_id=None, send_notifications=None) -> web.Response:
    """Submit Expenses for Approval.

    

    :param expense_ids: A collection of ExpenseID&#39;s that should be submitted for approval. If not provided, submits all verified expenses for approval.
    :type expense_ids: List[int]
    :param user_id: The user to submit the Expenses for. Defaults to current user. Only allowed to be different from the current user when the current user has rights to Impersonate other users.
    :type user_id: int
    :param send_notifications: Send email alerts to expense approvers. Defaults to true
    :type send_notifications: bool

    """
    return web.Response(status=200)


async def expense_attachment(request: web.Request, body) -> web.Response:
    """expense_attachment

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExpenseAttachmentRequest.from_dict(body)
    return web.Response(status=200)


async def expense_delete(request: web.Request, expense_ids) -> web.Response:
    """Delete a Timesheet Entry

    

    :param expense_ids: A collection of ExpenseIDs to delete
    :type expense_ids: List[int]

    """
    return web.Response(status=200)


async def expense_get(request: web.Request, updated_after=None, expense_date_from=None, expense_date_to=None, user_email=None, user_id=None, category_name=None, customer_id=None, project_id=None, is_chargeable=None, is_invoiced=None, expense_reimbursement_idfk=None, expense_payment_method_idfk=None, expense_approval_status_code=None, search=None, page_size=None, page_number=None, sort=None) -> web.Response:
    """Gets list of Expenses

    

    :param updated_after: 
    :type updated_after: str
    :param expense_date_from: 
    :type expense_date_from: str
    :param expense_date_to: 
    :type expense_date_to: str
    :param user_email: 
    :type user_email: str
    :param user_id: 
    :type user_id: int
    :param category_name: 
    :type category_name: str
    :param customer_id: 
    :type customer_id: int
    :param project_id: 
    :type project_id: int
    :param is_chargeable: 
    :type is_chargeable: bool
    :param is_invoiced: 
    :type is_invoiced: bool
    :param expense_reimbursement_idfk: 
    :type expense_reimbursement_idfk: int
    :param expense_payment_method_idfk: 
    :type expense_payment_method_idfk: int
    :param expense_approval_status_code: 
    :type expense_approval_status_code: str
    :param search: 
    :type search: str
    :param page_size: Number of items per page (max 1000)
    :type page_size: int
    :param page_number: Page to display. Starts from 1.
    :type page_number: int
    :param sort: 
    :type sort: str

    """
    updated_after = util.deserialize_datetime(updated_after)
    expense_date_from = util.deserialize_datetime(expense_date_from)
    expense_date_to = util.deserialize_datetime(expense_date_to)
    return web.Response(status=200)


async def expense_get_by_id(request: web.Request, id) -> web.Response:
    """Gets an Expense Entry by Expense ID

    

    :param id: Expense ID number
    :type id: int

    """
    return web.Response(status=200)


async def expense_post(request: web.Request, model) -> web.Response:
    """Create an Expense

    Create an Expense

    :param model: 
    :type model: dict | bytes

    """
    model = NewExpense.from_dict(model)
    return web.Response(status=200)


async def expense_put(request: web.Request, model) -> web.Response:
    """Update an Expense

    Update an Expense

    :param model: 
    :type model: dict | bytes

    """
    model = UpdateExpense.from_dict(model)
    return web.Response(status=200)
