# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_invoice_request1 import ChangeInvoiceRequest1
from openapi_server.models.getinvoicesfromacheckingaccount1 import Getinvoicesfromacheckingaccount1
from openapi_server.models.markaninvoiceas_paid_request1 import MarkaninvoiceasPaidRequest1
from openapi_server.models.paidinvoices1 import Paidinvoices1
from openapi_server.models.postponeaninvoice_request1 import PostponeaninvoiceRequest1
from openapi_server.models.retrievedinvoice1 import Retrievedinvoice1


pytestmark = pytest.mark.asyncio

async def test_cancel_invoice(client):
    """Test case for cancel_invoice

    Cancel Invoice
    """
    headers = { 
        'Accept': 'text/plain',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/creditcontrol/accounts/{credit_account_id}/invoices/{invoice_id}'.format(credit_account_id='insert identifier here', invoice_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_invoice(client):
    """Test case for change_invoice

    Change Invoice
    """
    body = {"observation":"string (optional)","paymentLink":"string (URL) (optional)","status":"string"}
    params = [('friendlyId', 'insert identifier here')]
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/invoices/{invoice_id}'.format(credit_account_id='insert identifier here', invoice_id='insert identifier here'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_markaninvoiceas_paid(client):
    """Test case for markaninvoiceas_paid

    Mark an invoice as Paid
    """
    body = {"value":"number (FULL invoice value [deprecated])"}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/creditcontrol/accounts/{credit_account_id}/invoices/{invoice_id}/payments'.format(credit_account_id='isert indentifier here', invoice_id='insert identifier here'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_postponeaninvoice(client):
    """Test case for postponeaninvoice

    Postpone an invoice
    """
    body = {"dueDays":"number (integer)"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'accept': 'application/json',
        'content_type': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/creditcontrol/accounts/{credit_account_id}/invoices/{invoice_id}/postponement'.format(credit_account_id='credit_account_id_example', invoice_id='invoice_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_invoiceby_id(client):
    """Test case for retrieve_invoiceby_id

    Retrieve Invoice by Id
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/accounts/{credit_account_id}/invoices/{invoice_id}'.format(credit_account_id='insert identifier here', invoice_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchallinvoices(client):
    """Test case for searchallinvoices

    Search all invoices
    """
    params = [('from', ''),
                    ('to', ''),
                    ('createdDateFrom', ''),
                    ('createdDateTo', ''),
                    ('value', 3.4),
                    ('status', 'Paid'),
                    ('friendlyId', 'insert identifier here'),
                    ('creditAccountId', 'B75F0')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/invoices',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searchallinvoicesofa_account(client):
    """Test case for searchallinvoicesofa_account

    Retrieve invoice by creditAccountId
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/creditcontrol/accounts/{credit_account_id}/invoices'.format(credit_account_id='insert identifier here'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

