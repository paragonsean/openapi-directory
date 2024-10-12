# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.create_success_response import CreateSuccessResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.integrations_products_sync_get200_response import IntegrationsProductsSyncGet200Response
from openapi_server.models.invoices_get200_response import InvoicesGet200Response
from openapi_server.models.invoices_invoice_id_get200_response import InvoicesInvoiceIdGet200Response
from openapi_server.models.invoices_invoice_id_put_request import InvoicesInvoiceIdPutRequest
from openapi_server.models.invoices_post_request import InvoicesPostRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_invoices(client):
    """Test case for bulk_delete_invoices

    Bulk delete invoices
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/invoices/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_get(client):
    """Test case for invoices_get

    View list of invoices
    """
    params = [('contact_id', 'contact_id_example'),
                    ('project_id', 'project_id_example'),
                    ('invoice_number', 'invoice_number_example'),
                    ('offer_number', 'offer_number_example'),
                    ('is_draft', 56),
                    ('is_offer', 56),
                    ('is_locked', 56),
                    ('is_fixed_price', 56),
                    ('date_from', '2013-10-20'),
                    ('date_to', '2013-10-20'),
                    ('issued_date', '2013-10-20'),
                    ('sent_as_draft', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_copy_post(client):
    """Test case for invoices_invoice_id_copy_post

    Create a copy of an invoice
    """
    params = [('project_id', 'project_id_example'),
                    ('contact_id', 'contact_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/invoices/{invoice_id}/copy'.format(invoice_id='invoice_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_delete(client):
    """Test case for invoices_invoice_id_delete

    Delete invoice
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/invoices/{invoice_id}'.format(invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_get(client):
    """Test case for invoices_invoice_id_get

    View invoice
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoices/{invoice_id}'.format(invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_link_project_pdf_post(client):
    """Test case for invoices_invoice_id_link_project_pdf_post

    Creates an invoice file containing the project's pdf overview
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/invoices/{invoice_id}/linkProjectPdf'.format(invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_put(client):
    """Test case for invoices_invoice_id_put

    Edit invoice
    """
    body = openapi_server.InvoicesInvoiceIdPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/invoices/{invoice_id}'.format(invoice_id='invoice_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_invoice_id_unlink_project_pdf_post(client):
    """Test case for invoices_invoice_id_unlink_project_pdf_post

    Deletes the linked project overview pdf
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/invoices/{invoice_id}/unlinkProjectPdf'.format(invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_post(client):
    """Test case for invoices_post

    Add invoice
    """
    body = openapi_server.InvoicesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/invoices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoices_vat_options_get(client):
    """Test case for invoices_vat_options_get

    List VAT options
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/invoices/vatOptions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

