from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_files_expense_file_id_get200_response import ExpenseFilesExpenseFileIdGet200Response
from openapi_server.models.expense_files_expense_file_id_put200_response import ExpenseFilesExpenseFileIdPut200Response
from openapi_server.models.expense_files_get200_response import ExpenseFilesGet200Response
from openapi_server import util


async def expense_files_expense_file_id_delete(request: web.Request, expense_file_id) -> web.Response:
    """Delete file

    

    :param expense_file_id: 
    :type expense_file_id: str

    """
    return web.Response(status=200)


async def expense_files_expense_file_id_get(request: web.Request, expense_file_id) -> web.Response:
    """Show file

    

    :param expense_file_id: 
    :type expense_file_id: str

    """
    return web.Response(status=200)


async def expense_files_expense_file_id_put(request: web.Request, expense_file_id) -> web.Response:
    """Edit file

    

    :param expense_file_id: 
    :type expense_file_id: str
    :type expense_file_id: str

    """
    return web.Response(status=200)


async def expense_files_get(request: web.Request, created_by_id=None, expense_id=None) -> web.Response:
    """Show list of expense files

    

    :param created_by_id: 
    :type created_by_id: str
    :type created_by_id: str
    :param expense_id: 
    :type expense_id: str
    :type expense_id: str

    """
    return web.Response(status=200)


async def expense_files_post(request: web.Request, file, description=None) -> web.Response:
    """Add file to expense

    

    :param file: 
    :type file: str
    :param description: 
    :type description: str

    """
    return web.Response(status=200)
