from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.project_travel_expense_input_model import ProjectTravelExpenseInputModel
from openapi_server.models.project_travel_expense_output_model import ProjectTravelExpenseOutputModel
from openapi_server.models.travel_reimbursement_input_model import TravelReimbursementInputModel
from openapi_server.models.travel_reimbursement_output_model import TravelReimbursementOutputModel
from openapi_server import util


async def project_travel_expenses_patch_project_travel_expense(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a project travel expense or a part of it.

    

    :param guid: ID of the project travel expense.
    :type guid: str
    :param body: JSON Patch document of ProjectTravelExpenseInputModel.
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def project_travel_expenses_post_project_travel_expense(request: web.Request, body=None) -> web.Response:
    """Insert a project travel expense.

    

    :param body: ProjectTravelExpenseInputModel.
    :type body: dict | bytes

    """
    body = ProjectTravelExpenseInputModel.from_dict(body)
    return web.Response(status=200)


async def travel_reimbursements_patch_travel_reimbursement(request: web.Request, guid, body=None) -> web.Response:
    """Update (Patch) a travel reimbursement

    

    :param guid: ID of the travel reimbursement
    :type guid: str
    :param body: JSON Patch document
    :type body: list | bytes

    """
    body = [PatchOperation.from_dict(d) for d in body]
    return web.Response(status=200)


async def travel_reimbursements_post_travel_reimbursement(request: web.Request, add_all_unreimbursed_travel_expenses=None, included_project_travel_expenses=None, body=None) -> web.Response:
    """Add a travel reimbursement

    

    :param add_all_unreimbursed_travel_expenses: Optional: Add all of user&#39;s unreimbursed travel expenses to reimbursement. Default is true. If TravelExpenseReimbursementStartDate is given in organization settings, travel expenses are added from that date onwards. If value is false then expenses from includedProjectTravelExpenses list are added.
    :type add_all_unreimbursed_travel_expenses: bool
    :param included_project_travel_expenses: Optional: A list of included projectTravelExpense GUIDs belonging to the user. If addAllUnreimbursedTravelExpenses is true then this list is ignored.
    :type included_project_travel_expenses: List[str]
    :param body: TravelReimbursementModel
    :type body: dict | bytes

    """
    body = TravelReimbursementInputModel.from_dict(body)
    return web.Response(status=200)
