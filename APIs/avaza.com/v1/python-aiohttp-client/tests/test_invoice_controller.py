# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.invoice import Invoice
from openapi_server.models.invoice_list import InvoiceList
from openapi_server.models.new_invoice import NewInvoice


pytestmark = pytest.mark.asyncio

async def test_invoice_get(client):
    """Test case for invoice_get

    Gets list of Invoices
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example'),
                    ('CompanyIDFK', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Invoice',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_invoice_get_by_id(client):
    """Test case for invoice_get_by_id

    Gets Invoice by Invoice ID
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Invoice/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_invoice_post(client):
    """Test case for invoice_post

    Create a new draft invoice
    """
    model = {"ExchangeRate":6.027456183070403,"LineItems":[{"InventoryItemName":"InventoryItemName","UnitPrice":2.027123023002322,"Description":"Description","Discount":5.962133916683182,"TaxIDFK":9,"ProjectIDFK":2,"TaxName":"TaxName","InventoryItemIDFK":5,"Quantity":7.061401241503109,"TaxPercent":3.616076749251911},{"InventoryItemName":"InventoryItemName","UnitPrice":2.027123023002322,"Description":"Description","Discount":5.962133916683182,"TaxIDFK":9,"ProjectIDFK":2,"TaxName":"TaxName","InventoryItemIDFK":5,"Quantity":7.061401241503109,"TaxPercent":3.616076749251911}],"Email":"Email","Lastname":"Lastname","CompanyIDFK":0,"PaymentTerms":4,"Subject":"Subject","CurrencyCode":"CurrencyCode","Firstname":"Firstname","TransactionPrefix":"TransactionPrefix","CompanyName":"CompanyName","CustomerPONumber":"CustomerPONumber","DateIssued":"2000-01-23T04:56:07.000+00:00","InvoiceTemplateIDFK":1,"InvoiceNumber":"InvoiceNumber","DueDate":"2000-01-23T04:56:07.000+00:00","Notes":"Notes","TransactionTaxConfigCode":"TransactionTaxConfigCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Invoice',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

