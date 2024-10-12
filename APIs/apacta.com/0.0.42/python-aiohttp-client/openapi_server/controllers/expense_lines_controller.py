from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_lines_expense_line_id_get200_response import ExpenseLinesExpenseLineIdGet200Response
from openapi_server.models.expense_lines_get200_response import ExpenseLinesGet200Response
from openapi_server.models.expense_lines_post_request import ExpenseLinesPostRequest
from openapi_server import util


async def expense_lines_expense_line_id_delete(request: web.Request, expense_line_id) -> web.Response:
    """Delete expense line

    

    :param expense_line_id: 
    :type expense_line_id: str

    """
    return web.Response(status=200)


async def expense_lines_expense_line_id_get(request: web.Request, expense_line_id) -> web.Response:
    """Show expense line

    

    :param expense_line_id: 
    :type expense_line_id: str

    """
    return web.Response(status=200)


async def expense_lines_expense_line_id_put(request: web.Request, expense_line_id) -> web.Response:
    """Edit expense line

    

    :param expense_line_id: 
    :type expense_line_id: str

    """
    return web.Response(status=200)


async def expense_lines_get(request: web.Request, created_by_id=None, currency_id=None, expense_id=None) -> web.Response:
    """Show list of expense lines

    

    :param created_by_id: 
    :type created_by_id: str
    :type created_by_id: str
    :param currency_id: 
    :type currency_id: str
    :type currency_id: str
    :param expense_id: 
    :type expense_id: str
    :type expense_id: str

    """
    return web.Response(status=200)


async def expense_lines_post(request: web.Request, body=None) -> web.Response:
    """Add line to expense

    

    :param body: 
    :type body: dict | bytes

    """
    body = ExpenseLinesPostRequest.from_dict(body)
    return web.Response(status=200)
