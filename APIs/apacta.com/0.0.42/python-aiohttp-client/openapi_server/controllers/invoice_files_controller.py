from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.get_invoice_files200_response import GetInvoiceFiles200Response
from openapi_server.models.get_one_invoice_files200_response import GetOneInvoiceFiles200Response
from openapi_server.models.unauthorized_error import UnauthorizedError
from openapi_server import util


async def create_invoice_file(request: web.Request, invoice_id, file_id, invoice_id2, type=None) -> web.Response:
    """Create a new invoice file

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param file_id: 
    :type file_id: str
    :type file_id: str
    :param invoice_id2: 
    :type invoice_id2: str
    :type invoice_id2: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def get_invoice_files(request: web.Request, invoice_id) -> web.Response:
    """Get list of invoice files

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str

    """
    return web.Response(status=200)


async def get_one_invoice_files(request: web.Request, invoice_id, file_id) -> web.Response:
    """Get an invoice files

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param file_id: 
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)


async def invoices_invoice_id_files_file_id_delete(request: web.Request, invoice_id, file_id) -> web.Response:
    """Delete invoice file

    

    :param invoice_id: 
    :type invoice_id: str
    :type invoice_id: str
    :param file_id: 
    :type file_id: str
    :type file_id: str

    """
    return web.Response(status=200)
