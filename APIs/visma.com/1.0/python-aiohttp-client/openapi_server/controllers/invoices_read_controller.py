from typing import List, Dict
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.expenses_class import ExpensesClass
from openapi_server.models.invoice_output_model import InvoiceOutputModel
from openapi_server.models.invoice_row_output_model import InvoiceRowOutputModel
from openapi_server.models.invoice_row_type import InvoiceRowType
from openapi_server.models.invoice_settings_output_model import InvoiceSettingsOutputModel
from openapi_server.models.key_value_pair_of_string_and_sort_direction import KeyValuePairOfStringAndSortDirection
from openapi_server.models.product_type import ProductType
from openapi_server.models.project_fee_output_model import ProjectFeeOutputModel
from openapi_server.models.project_invoice_settings_output_model import ProjectInvoiceSettingsOutputModel
from openapi_server.models.project_travel_expense_output_model import ProjectTravelExpenseOutputModel
from openapi_server.models.reimbursed_project_fee_output_model import ReimbursedProjectFeeOutputModel
from openapi_server.models.reimbursed_project_travel_expense_output_model import ReimbursedProjectTravelExpenseOutputModel
from openapi_server.models.reimbursed_work_hour_output_model import ReimbursedWorkHourOutputModel
from openapi_server.models.work_hour_output_model import WorkHourOutputModel
from openapi_server import util


async def finvoices_get_finvoice_by_invoice_guid(request: web.Request, invoice_guid) -> web.Response:
    """finvoices_get_finvoice_by_invoice_guid

    

    :param invoice_guid: 
    :type invoice_guid: str

    """
    return web.Response(status=200)


async def finvoices_get_finvoices_by_invoice_status(request: web.Request, invoice_status_guid) -> web.Response:
    """finvoices_get_finvoices_by_invoice_status

    

    :param invoice_status_guid: 
    :type invoice_status_guid: str

    """
    return web.Response(status=200)


async def invoice_rows_get_invoice_row(request: web.Request, guid) -> web.Response:
    """Get invoice row by ID

    

    :param guid: GUID of the invoice row.
    :type guid: str

    """
    return web.Response(status=200)


async def invoice_rows_get_invoice_rows(request: web.Request, page_token=None, row_count=None, changed_since=None) -> web.Response:
    """Get invoice rows

    

    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param changed_since: Optional: Get invoice rows that have been added or changed after this date time (greater or equal).
    :type changed_since: str

    """
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def invoice_rows_get_invoice_rows_for_invoice(request: web.Request, invoice_guid, page_token=None, row_count=None, row_type=None) -> web.Response:
    """Get Invoice rows for an invoice.

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param row_type: Optional: Type of the row. Either Hours or ProjectFees, Default all.
    :type row_type: dict | bytes

    """
    row_type = .from_dict(row_type)
    return web.Response(status=200)


async def invoice_settings_get_invoice_settings(request: web.Request, invoice_guid) -> web.Response:
    """Get invoice settings by invoice GUID

    

    :param invoice_guid: Invoice GUID used to get the invoice settings.
    :type invoice_guid: str

    """
    return web.Response(status=200)


async def invoices_get_invoice(request: web.Request, guid) -> web.Response:
    """Get invoice by ID

    

    :param guid: GUID of the invoice.
    :type guid: str

    """
    return web.Response(status=200)


async def invoices_get_invoices(request: web.Request, row_count=None, page_token=None, payment_date_start=None, invoice_status_guids=None, project_guids=None, project_owner_guids=None, project_business_unit_guids=None, customer_guids=None, start_date=None, end_date=None, minimum_total_excluding_tax=None, maximum_total_excluding_tax=None, reference_numbers=None, numbers=None, changed_since=None, sales_person_guids=None, created_by_user_guids=None) -> web.Response:
    """Get Invoices

    

    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param payment_date_start: Optional: Get only invoices paid at this date or later. Default: Get invoices regardless of payment date.
    :type payment_date_start: str
    :param invoice_status_guids: Optional: Get invoices with this status only. Default: all statuses.
    :type invoice_status_guids: List[str]
    :param project_guids: Optional: ID of the project to get the invoices. If not provided, returns for all projects. Default all.
    :type project_guids: List[str]
    :param project_owner_guids: Optional: ID of the project manager to get the invoices for. If not provided, returns for all project managers. Default all.
    :type project_owner_guids: List[str]
    :param project_business_unit_guids: Optional: ID of the business unit of the project. If not provided, returns for all business units. Default all.
    :type project_business_unit_guids: List[str]
    :param customer_guids: Optional: List of customer IDs. Get invoices for these customers.
    :type customer_guids: List[str]
    :param start_date: Optional: starting date from which to get the invoices. Default all.
    :type start_date: str
    :param end_date: Optional: end date from which to get the invoices. Default all.
    :type end_date: str
    :param minimum_total_excluding_tax: Optional: specifies minimum value for invoice total in organization currency.
    :type minimum_total_excluding_tax: float
    :param maximum_total_excluding_tax: Optional: specifies maximum value for invoice total in organization currency.
    :type maximum_total_excluding_tax: float
    :param reference_numbers: Optional: Invoice reference number. If not provided, returns invoices with any invoice reference number.
    :type reference_numbers: List[str]
    :param numbers: Optional: Invoice number. If not provided, returns invoices with any invoice number.
    :type numbers: List[int]
    :param changed_since: Optional: Get invoices that have been added or changed after this date time (greater or equal).
    :type changed_since: str
    :param sales_person_guids: Optional: ID of the salesperson to get the invoices for. If not provided, returns for all sales persons.
    :type sales_person_guids: List[str]
    :param created_by_user_guids: Optional: ID of the user who created the invoice. If not provided, returns for all users.
    :type created_by_user_guids: List[str]

    """
    payment_date_start = util.deserialize_datetime(payment_date_start)
    start_date = util.deserialize_datetime(start_date)
    end_date = util.deserialize_datetime(end_date)
    changed_since = util.deserialize_datetime(changed_since)
    return web.Response(status=200)


async def project_fees_get_invoice_project_fees(request: web.Request, invoice_guid, page_token=None, row_count=None, product_type=None) -> web.Response:
    """Get all the project fees on an invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param product_type: Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
    :type product_type: dict | bytes

    """
    product_type = .from_dict(product_type)
    return web.Response(status=200)


async def project_fees_get_invoice_row_project_fees(request: web.Request, invoice_row_guid, page_token=None, row_count=None, product_type=None) -> web.Response:
    """Get all the project fees on an invoice row

    

    :param invoice_row_guid: ID of the invoice row.
    :type invoice_row_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param product_type: Optional: ProjectFee&#39;s product type. if given, it filters the projectFees by the given type. FixedFees (Own work), Materials (Products), Subcontracting
    :type product_type: dict | bytes

    """
    product_type = .from_dict(product_type)
    return web.Response(status=200)


async def project_fees_get_uninvoiced_project_fees_for_invoice(request: web.Request, invoice_guid, page_token=None, row_count=None, is_billable=None) -> web.Response:
    """Get uninvoiced project fees available for invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: Number of rows to fetch.
    :type row_count: int
    :param is_billable: Optional: Filter the project fees. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool

    """
    return web.Response(status=200)


async def project_invoice_settings_get_project_invoice_setting(request: web.Request, guid) -> web.Response:
    """Get project invoice settings by ID.

    

    :param guid: ID of the project invoice settings.
    :type guid: str

    """
    return web.Response(status=200)


async def project_invoice_settings_get_project_invoice_settings(request: web.Request, project_guid) -> web.Response:
    """Get project invoice settings by project ID.

    

    :param project_guid: ID of the project.
    :type project_guid: str

    """
    return web.Response(status=200)


async def project_travel_expenses_get_invoice_project_travel_expenses(request: web.Request, invoice_guid, page_token=None, row_count=None, expense_class=None) -> web.Response:
    """Get all the project travel expenses on an invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param expense_class: Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    :type expense_class: dict | bytes

    """
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def project_travel_expenses_get_invoice_row_project_travel_expenses(request: web.Request, invoice_row_guid, page_token=None, row_count=None, expense_class=None) -> web.Response:
    """Get all the project travel expenses on an invoice row

    

    :param invoice_row_guid: ID of the invoice row.
    :type invoice_row_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param expense_class: Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    :type expense_class: dict | bytes

    """
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def project_travel_expenses_get_uninvoiced_project_travel_expenses_for_invoice(request: web.Request, invoice_guid, is_billable=None, page_token=None, row_count=None, expense_class=None) -> web.Response:
    """Get uninvoiced project travel expenses available for invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param is_billable: Optional: Filter the travel expenses. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param expense_class: Optional: Class of the expense. Mileage, DailyAllowance or OtherTravelExpense
    :type expense_class: dict | bytes

    """
    expense_class = .from_dict(expense_class)
    return web.Response(status=200)


async def reimbursed_project_fees_get_invoice_reimbursed_project_fees(request: web.Request, invoice_guid, row_count=None, page_token=None) -> web.Response:
    """Get all the project fees on an invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param row_count: Optional: Number of rows to fetch
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def reimbursed_project_fees_get_invoice_row_reimbursed_project_fees(request: web.Request, invoice_row_guid, row_count=None, page_token=None) -> web.Response:
    """Get all the project fees on an invoice row

    

    :param invoice_row_guid: ID of the invoice row.
    :type invoice_row_guid: str
    :param row_count: Optional: Number of rows to fetch
    :type row_count: int
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str

    """
    return web.Response(status=200)


async def reimbursed_project_travel_expenses_get_invoice_project_travel_expenses(request: web.Request, invoice_guid, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all the project travel expenses on an invoice.

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param text_to_search: Searched string: part of name or description.
    :type text_to_search: str
    :param calculate_row_count: Optional. If true, calculates the total count of project fees. Default false.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def reimbursed_project_travel_expenses_get_invoice_row_project_travel_expenses(request: web.Request, invoice_row_guid, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all the project travel expenses on an invoice row.

    

    :param invoice_row_guid: ID of the invoice row.
    :type invoice_row_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default all.
    :type row_count: int
    :param text_to_search: Searched string: part of name or description.
    :type text_to_search: str
    :param calculate_row_count: Optional. If true, calculates the total count of project fees. Default false.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def reimbursed_work_hours_get_invoice_reimbursed_work_hours(request: web.Request, invoice_guid, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all reimbursed hours on an invoice.

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from description or invoice description.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;DueDate&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;TotalIncludingTax&amp;sortings[1].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def reimbursed_work_hours_get_invoice_row_reimbursed_work_hours(request: web.Request, invoice_row_guid, first_row=None, row_count=None, text_to_search=None, calculate_row_count=None, sortings=None) -> web.Response:
    """Get all reimbursed hours on an invoice row.

    

    :param invoice_row_guid: ID of the invoice row.
    :type invoice_row_guid: str
    :param first_row: Optional: first row to fetch. Default 0 &#x3D; first row.
    :type first_row: int
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int
    :param text_to_search: Optional: Text to search from description or invoice description.
    :type text_to_search: str
    :param calculate_row_count: Optional: Calculate total number of rows.
    :type calculate_row_count: bool
    :param sortings: Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;DueDate&amp;sortings[0].value&#x3D;Asc&amp;sortings[1].key&#x3D;TotalIncludingTax&amp;sortings[1].value&#x3D;Desc\&quot;.
    :type sortings: list | bytes

    """
    sortings = [KeyValuePairOfStringAndSortDirection.from_dict(d) for d in sortings]
    return web.Response(status=200)


async def work_hours_get_invoice_row_work_hours(request: web.Request, invoice_row_guid, page_token=None, row_count=None) -> web.Response:
    """Get all the work hours on an invoice row

    

    :param invoice_row_guid: ID of the invoice row.
    :type invoice_row_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    return web.Response(status=200)


async def work_hours_get_invoice_work_hours(request: web.Request, invoice_guid, page_token=None, row_count=None) -> web.Response:
    """Get all the work hours on an invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    return web.Response(status=200)


async def work_hours_get_uninvoiced_work_hours_for_invoice(request: web.Request, invoice_guid, is_billable=None, page_token=None, row_count=None) -> web.Response:
    """Get uninvoiced work hours available for invoice

    

    :param invoice_guid: ID of the invoice.
    :type invoice_guid: str
    :param is_billable: Optional: Filter the work hours. If true/false, only the billable/non-billable ones are returned. If null, all are returned. Default is null.
    :type is_billable: bool
    :param page_token: Optional: page token to fetch the next page.
    :type page_token: str
    :param row_count: Optional: How many rows to fetch, Default 20, maximum 100.
    :type row_count: int

    """
    return web.Response(status=200)
