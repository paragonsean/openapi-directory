# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_file_data_get_data_for_file(client):
    """Test case for file_data_get_data_for_file

    Get file data by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/files/{guid}/filedata'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_file(client):
    """Test case for files_get_file

    Get file by ID.
    """
    params = [('includeDataInResponse', False)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/files/{guid}'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_invoice_file(client):
    """Test case for files_get_invoice_file

    Get invoice file by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoicefiles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_invoice_files(client):
    """Test case for files_get_invoice_files

    Get all files of a invoice by its id.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{invoice_guid}/files'.format(invoice_guid='invoice_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_project_file(client):
    """Test case for files_get_project_file

    Get project file by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projectfiles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_project_files(client):
    """Test case for files_get_project_files

    Get all files of a project by its id.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/files'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_travel_expense_file(client):
    """Test case for files_get_travel_expense_file

    Get travel expense file by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projecttravelexpensefiles/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_travel_expense_files(client):
    """Test case for files_get_travel_expense_files

    Get all files of a travel expense by its id.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56)]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projecttravelexpenses/{project_travel_expense_guid}/files'.format(project_travel_expense_guid='project_travel_expense_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_files_get_users_travel_expenses_files(client):
    """Test case for files_get_users_travel_expenses_files

    Get all files of all travel expenses of the user.
    """
    params = [('firstRow', 56),
                    ('rowCount', 56),
                    ('startDate', '2013-10-20T19:20:30+01:00'),
                    ('endDate', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/travelexpensesfiles'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_keywords_get_file_keywords(client):
    """Test case for keywords_get_file_keywords

    Get all the keywords for file.
    """
    params = [('active', True),
                    ('sortings', [openapi_server.KeyValuePairOfStringAndSortDirection()])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/files/{file_guid}/keywords'.format(file_guid='file_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pdf_get_invoice_pdf(client):
    """Test case for pdf_get_invoice_pdf

    Get an invoice PDF.
    """
    params = [('invoiceType', openapi_server.InvoiceType()),
                    ('pdfGetOptions', openapi_server.InvoicePdfGetOptions())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/invoices/{guid}/pdf'.format(guid='guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_pdf_get_travel_reimbursement_pdf(client):
    """Test case for pdf_get_travel_reimbursement_pdf

    Get a travel reimbursement PDF.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelreimbursements/{guid}/pdf'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

