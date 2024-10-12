from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_checkout_post201_response import ClockingRecordsCheckoutPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server import util


async def expenses_expense_id_original_files_file_id_get(request: web.Request, expense_id, file_id) -> web.Response:
    """Show OIOUBL file

    

    :param expense_id: 
    :type expense_id: str
    :param file_id: 
    :type file_id: str

    """
    return web.Response(status=200)


async def expenses_expense_id_original_files_get(request: web.Request, expense_id) -> web.Response:
    """Show list of all OIOUBL files for the expense

    

    :param expense_id: 
    :type expense_id: str

    """
    return web.Response(status=200)
