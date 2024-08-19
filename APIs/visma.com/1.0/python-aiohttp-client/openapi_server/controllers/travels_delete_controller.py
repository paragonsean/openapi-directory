from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server import util


async def project_travel_expenses_delete_project_travel_expense(request: web.Request, guid) -> web.Response:
    """Deletes a project travel expense.

    Returns: No Content (204) if succeeded.

    :param guid: GUID used to delete the project travel expense.
    :type guid: str

    """
    return web.Response(status=200)


async def travel_reimbursements_delete_travel_reimbursement(request: web.Request, guid) -> web.Response:
    """Delete a travel reimbursement

    

    :param guid: GUID of travel reimbursement
    :type guid: str

    """
    return web.Response(status=200)
