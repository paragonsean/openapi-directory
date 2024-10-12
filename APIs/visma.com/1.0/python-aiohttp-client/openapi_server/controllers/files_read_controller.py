from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.file_keyword_model import FileKeywordModel
from openapi_server.models.file_model import FileModel
from openapi_server.models.invoice_file_model import InvoiceFileModel
from openapi_server.models.invoice_pdf_get_options import InvoicePdfGetOptions
from openapi_server.models.invoice_type import InvoiceType
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.project_file_model import ProjectFileModel
from openapi_server.models.project_travel_expense_file_model import ProjectTravelExpenseFileModel
from openapi_server import util


async def file_data_get_data_for_file(request: web.Request, guid) -> web.Response:
    """Get file data by ID.

    Returns binary data, which contains content with type given in Content-Type header.

    :param guid: GUID used to get the file.
    :type guid: str

    """
    return web.Response(status=200)


async def files_get_file(request: web.Request, guid, include_data_in_response=None) -> web.Response:
    """Get file by ID.

    

    :param guid: GUID used to get the file.
    :type guid: str
    :param include_data_in_response: Is data included in response as base64 string.
    :type include_data_in_response: bool

    """
    return web.Response(status=200)


async def files_get_invoice_file(request: web.Request, guid) -> web.Response:
    """Get invoice file by ID.

    

    :param guid: GUID used to get the invoice file.
    :type guid: str

    """
    return web.Response(status=200)


async def files_get_invoice_files(request: web.Request, invoice_guid, first_row=None, row_count=None) -> web.Response:
    """Get all files of a invoice by its id.

    

    :param invoice_guid: GUID of the invoice used to get the files.
    :type invoice_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int

    """
    return web.Response(status=200)


async def files_get_project_file(request: web.Request, guid) -> web.Response:
    """Get project file by ID.

    

    :param guid: GUID used to get the project file.
    :type guid: str

    """
    return web.Response(status=200)


async def files_get_project_files(request: web.Request, project_guid, first_row=None, row_count=None, sortings=None) -> web.Response:
    """Get all files of a project by its id.

    

    :param project_guid: GUID of the project used to get the files.
    :type project_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def files_get_travel_expense_file(request: web.Request, guid) -> web.Response:
    """Get travel expense file by ID.

    

    :param guid: GUID used to get the travel expense file.
    :type guid: str

    """
    return web.Response(status=200)


async def files_get_travel_expense_files(request: web.Request, project_travel_expense_guid, first_row=None, row_count=None) -> web.Response:
    """Get all files of a travel expense by its id.

    

    :param project_travel_expense_guid: GUID of the travel expense used to get the files.
    :type project_travel_expense_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int

    """
    return web.Response(status=200)


async def files_get_users_travel_expenses_files(request: web.Request, user_guid, first_row=None, row_count=None, start_date=None, end_date=None) -> web.Response:
    """Get all files of all travel expenses of the user.

    

    :param user_guid: GUID of the user used to get the files attached to travel expenses.
    :type user_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch.
    :type row_count: int
    :param start_date: Optional: Start date to from which to check travel expenses.
    :type start_date: str
    :param end_date: Optional: End date to check for availability until travel expenses.
    :type end_date: str

    """
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    return web.Response(status=200)


async def keywords_get_file_keywords(request: web.Request, file_guid, active=None, sortings=None) -> web.Response:
    """Get all the keywords for file.

    

    :param file_guid: ID of the file for which keywords are requested.
    :type file_guid: str
    :param active: If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
    :type active: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def pdf_get_invoice_pdf(request: web.Request, guid, invoice_type=None, pdf_get_options=None) -> web.Response:
    """Get an invoice PDF.

    

    :param guid: The invoice GUID.
    :type guid: str
    :param invoice_type: Optional: type of invoice.
    :type invoice_type: dict | bytes
    :param pdf_get_options: Optional: what to include in the PDF. Defaults to InvoicePdfGetOptions.All.
    :type pdf_get_options: dict | bytes

    """
    invoice_type = .from_dict(invoice_type)
    pdf_get_options = .from_dict(pdf_get_options)
    return web.Response(status=200)


async def pdf_get_travel_reimbursement_pdf(request: web.Request, guid) -> web.Response:
    """Get a travel reimbursement PDF.

    

    :param guid: The travel reimbursement GUID.
    :type guid: str

    """
    return web.Response(status=200)
