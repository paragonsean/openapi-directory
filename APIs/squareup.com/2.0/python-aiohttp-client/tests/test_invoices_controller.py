# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cancel_invoice_request import CancelInvoiceRequest
from openapi_server.models.cancel_invoice_response import CancelInvoiceResponse
from openapi_server.models.create_invoice_request import CreateInvoiceRequest
from openapi_server.models.create_invoice_response import CreateInvoiceResponse
from openapi_server.models.delete_invoice_response import DeleteInvoiceResponse
from openapi_server.models.get_invoice_response import GetInvoiceResponse
from openapi_server.models.list_invoices_response import ListInvoicesResponse
from openapi_server.models.publish_invoice_request import PublishInvoiceRequest
from openapi_server.models.publish_invoice_response import PublishInvoiceResponse
from openapi_server.models.search_invoices_request import SearchInvoicesRequest
from openapi_server.models.search_invoices_response import SearchInvoicesResponse
from openapi_server.models.update_invoice_request import UpdateInvoiceRequest
from openapi_server.models.update_invoice_response import UpdateInvoiceResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_invoice(client):
    """Test case for cancel_invoice

    CancelInvoice
    """
    body = {"request_body":{"version":0}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/invoices/{invoice_id}/cancel'.format(invoice_id='invoice_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_invoice(client):
    """Test case for create_invoice

    CreateInvoice
    """
    body = {"request_body":{"idempotency_key":"ce3748f9-5fc1-4762-aa12-aae5e843f1f4","invoice":{"accepted_payment_methods":{"bank_account":False,"card":True,"square_gift_card":False},"custom_fields":[{"label":"Event Reference Number","placement":"ABOVE_LINE_ITEMS","value":"Ref. #1234"},{"label":"Terms of Service","placement":"BELOW_LINE_ITEMS","value":"The terms of service are..."}],"delivery_method":"EMAIL","description":"We appreciate your business!","invoice_number":"inv-100","location_id":"ES0RJRZYEC39A","order_id":"CAISENgvlJ6jLWAzERDzjyHVybY","payment_requests":[{"automatic_payment_source":"NONE","due_date":"2030-01-24","reminders":[{"message":"Your invoice is due tomorrow","relative_scheduled_days":-1}],"request_type":"BALANCE","tipping_enabled":True}],"primary_recipient":{"customer_id":"JDKYHBWT1D4F8MFH63DBMEN8Y4"},"scheduled_at":"2030-01-13T10:00:00Z","title":"Event Planning Services"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/invoices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_invoice(client):
    """Test case for delete_invoice

    DeleteInvoice
    """
    params = [('version', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/invoices/{invoice_id}'.format(invoice_id='invoice_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_invoice(client):
    """Test case for get_invoice

    GetInvoice
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/invoices/{invoice_id}'.format(invoice_id='invoice_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_invoices(client):
    """Test case for list_invoices

    ListInvoices
    """
    params = [('location_id', 'location_id_example'),
                    ('cursor', 'cursor_example'),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_publish_invoice(client):
    """Test case for publish_invoice

    PublishInvoice
    """
    body = {"request_body":{"idempotency_key":"32da42d0-1997-41b0-826b-f09464fc2c2e","version":1}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/invoices/{invoice_id}/publish'.format(invoice_id='invoice_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_invoices(client):
    """Test case for search_invoices

    SearchInvoices
    """
    body = {"request_body":{"query":{"filter":{"customer_ids":["JDKYHBWT1D4F8MFH63DBMEN8Y4"],"location_ids":["ES0RJRZYEC39A"]},"limit":100,"sort":{"field":"INVOICE_SORT_DATE","order":"DESC"}}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/invoices/search',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_invoice(client):
    """Test case for update_invoice

    UpdateInvoice
    """
    body = {"request_body":{"fields_to_clear":["payments_requests[2da7964f-f3d2-4f43-81e8-5aa220bf3355].reminders"],"idempotency_key":"4ee82288-0910-499e-ab4c-5d0071dad1be","invoice":{"payment_requests":[{"tipping_enabled":False,"uid":"2da7964f-f3d2-4f43-81e8-5aa220bf3355"}]}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/invoices/{invoice_id}'.format(invoice_id='invoice_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

