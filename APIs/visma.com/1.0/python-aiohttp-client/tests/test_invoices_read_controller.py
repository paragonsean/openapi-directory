# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_finvoices_get_finvoice_by_invoice_guid(client):
    """Test case for finvoices_get_finvoice_by_invoice_guid

    
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/finvoice'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_finvoices_get_finvoices_by_invoice_status(client):
    """Test case for finvoices_get_finvoices_by_invoice_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicestatuses/{invoice_status_guid}/finvoices'.format(invoice_status_guid='invoice_status_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_rows_get_invoice_row(client):
    """Test case for invoice_rows_get_invoice_row

    Get invoice row by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_rows_get_invoice_rows(client):
    """Test case for invoice_rows_get_invoice_rows

    Get invoice rows
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_rows_get_invoice_rows_for_invoice(client):
    """Test case for invoice_rows_get_invoice_rows_for_invoice

    Get Invoice rows for an invoice.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('rowType', openapi_server.InvoiceRowType())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/invoicerows'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_settings_get_invoice_settings(client):
    """Test case for invoice_settings_get_invoice_settings

    Get invoice settings by invoice GUID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/invoicesettings'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_get_invoice(client):
    """Test case for invoices_get_invoice

    Get invoice by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_get_invoices(client):
    """Test case for invoices_get_invoices

    Get Invoices
    """
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example'),
                    ('paymentDateStart', '2013-10-20T19:20:30+01:00'),
                    ('invoiceStatusGuids', ['invoice_status_guids_example']),
                    ('projectGuids', ['project_guids_example']),
                    ('projectOwnerGuids', ['project_owner_guids_example']),
                    ('projectBusinessUnitGuids', ['project_business_unit_guids_example']),
                    ('customerGuids', ['customer_guids_example']),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00'),
                    ('minimumTotalExcludingTax', 3.4),
                    ('maximumTotalExcludingTax', 3.4),
                    ('referenceNumbers', ['reference_numbers_example']),
                    ('numbers', [56]),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('salesPersonGuids', ['sales_person_guids_example']),
                    ('createdByUserGuids', ['created_by_user_guids_example'])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_invoice_project_fees(client):
    """Test case for project_fees_get_invoice_project_fees

    Get all the project fees on an invoice
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('productType', openapi_server.ProductType())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/projectfees'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_invoice_row_project_fees(client):
    """Test case for project_fees_get_invoice_row_project_fees

    Get all the project fees on an invoice row
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('productType', openapi_server.ProductType())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{invoice_row_guid}/projectfees'.format(invoice_row_guid='invoice_row_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_fees_get_uninvoiced_project_fees_for_invoice(client):
    """Test case for project_fees_get_uninvoiced_project_fees_for_invoice

    Get uninvoiced project fees available for invoice
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isBillable', True)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/uninvoicedprojectfees'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_get_project_invoice_setting(client):
    """Test case for project_invoice_settings_get_project_invoice_setting

    Get project invoice settings by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectinvoicesettings/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_invoice_settings_get_project_invoice_settings(client):
    """Test case for project_invoice_settings_get_project_invoice_settings

    Get project invoice settings by project ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projectinvoicesettings'.format(project_guid='project_guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_invoice_project_travel_expenses(client):
    """Test case for project_travel_expenses_get_invoice_project_travel_expenses

    Get all the project travel expenses on an invoice
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('expenseClass', openapi_server.ExpensesClass())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/projecttravelexpenses'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_invoice_row_project_travel_expenses(client):
    """Test case for project_travel_expenses_get_invoice_row_project_travel_expenses

    Get all the project travel expenses on an invoice row
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('expenseClass', openapi_server.ExpensesClass())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{invoice_row_guid}/projecttravelexpenses'.format(invoice_row_guid='invoice_row_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_uninvoiced_project_travel_expenses_for_invoice(client):
    """Test case for project_travel_expenses_get_uninvoiced_project_travel_expenses_for_invoice

    Get uninvoiced project travel expenses available for invoice
    """
    params = [('isBillable', True),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('expenseClass', openapi_server.ExpensesClass())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/uninvoicedprojecttravelexpenses'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reimbursed_project_fees_get_invoice_reimbursed_project_fees(client):
    """Test case for reimbursed_project_fees_get_invoice_reimbursed_project_fees

    Get all the project fees on an invoice
    """
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/reimbursedprojectfees'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reimbursed_project_fees_get_invoice_row_reimbursed_project_fees(client):
    """Test case for reimbursed_project_fees_get_invoice_row_reimbursed_project_fees

    Get all the project fees on an invoice row
    """
    params = [('rowCount', 56),
                    ('pageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{invoice_row_guid}/reimbursedprojectfees'.format(invoice_row_guid='invoice_row_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reimbursed_project_travel_expenses_get_invoice_project_travel_expenses(client):
    """Test case for reimbursed_project_travel_expenses_get_invoice_project_travel_expenses

    Get all the project travel expenses on an invoice.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/reimbursedprojecttravelexpenses'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reimbursed_project_travel_expenses_get_invoice_row_project_travel_expenses(client):
    """Test case for reimbursed_project_travel_expenses_get_invoice_row_project_travel_expenses

    Get all the project travel expenses on an invoice row.
    """
    params = [('firstRow', 0),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{invoice_row_guid}/reimbursedprojecttravelexpenses'.format(invoice_row_guid='invoice_row_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reimbursed_work_hours_get_invoice_reimbursed_work_hours(client):
    """Test case for reimbursed_work_hours_get_invoice_reimbursed_work_hours

    Get all reimbursed hours on an invoice.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/reimbursedworkhours'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reimbursed_work_hours_get_invoice_row_reimbursed_work_hours(client):
    """Test case for reimbursed_work_hours_get_invoice_row_reimbursed_work_hours

    Get all reimbursed hours on an invoice row.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56),
                    ('textToSearch', ''),
                    ('calculateRowCount', False),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{invoice_row_guid}/reimbursedworkhours'.format(invoice_row_guid='invoice_row_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_invoice_row_work_hours(client):
    """Test case for work_hours_get_invoice_row_work_hours

    Get all the work hours on an invoice row
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicerows/{invoice_row_guid}/workhours'.format(invoice_row_guid='invoice_row_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_invoice_work_hours(client):
    """Test case for work_hours_get_invoice_work_hours

    Get all the work hours on an invoice
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/workhours'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_work_hours_get_uninvoiced_work_hours_for_invoice(client):
    """Test case for work_hours_get_uninvoiced_work_hours_for_invoice

    Get uninvoiced work hours available for invoice
    """
    params = [('isBillable', True),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/uninvoicedworkhours'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

