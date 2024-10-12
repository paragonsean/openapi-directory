# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bill import Bill
from openapi_server.models.bill_list import BillList
from openapi_server.models.new_bill import NewBill


pytestmark = pytest.mark.asyncio

async def test_bill_get(client):
    """Test case for bill_get

    Gets list of Bills
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
        path='/api/Bill',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bill_get_by_id(client):
    """Test case for bill_get_by_id

    Gets a Bill by Bill ID
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Bill/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_bill_post(client):
    """Test case for bill_post

    Create a new draft Bill
    """
    model = {"ExchangeRate":1.4658129805029452,"LineItems":[{"InventoryItemName":"InventoryItemName","UnitPrice":2.027123023002322,"Description":"Description","Discount":5.962133916683182,"TaxIDFK":9,"ProjectIDFK":2,"TaxName":"TaxName","InventoryItemIDFK":5,"Quantity":7.061401241503109,"TaxPercent":3.616076749251911},{"InventoryItemName":"InventoryItemName","UnitPrice":2.027123023002322,"Description":"Description","Discount":5.962133916683182,"TaxIDFK":9,"ProjectIDFK":2,"TaxName":"TaxName","InventoryItemIDFK":5,"Quantity":7.061401241503109,"TaxPercent":3.616076749251911}],"Email":"Email","Lastname":"Lastname","BillTemplateIDFK":0,"CompanyIDFK":6,"PaymentTerms":4,"BillNumber":"BillNumber","Subject":"Subject","CurrencyCode":"CurrencyCode","Firstname":"Firstname","TransactionPrefix":"TransactionPrefix","CompanyName":"CompanyName","DateIssued":"2000-01-23T04:56:07.000+00:00","SupplierPONumber":"SupplierPONumber","DueDate":"2000-01-23T04:56:07.000+00:00","Notes":"Notes","TransactionTaxConfigCode":"TransactionTaxConfigCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Bill',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

