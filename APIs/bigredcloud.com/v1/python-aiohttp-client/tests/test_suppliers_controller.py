# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_tran_dto import AccountTranDto
from openapi_server.models.batch_item_supplier_dto import BatchItemSupplierDto
from openapi_server.models.owner_opening_balance_dto import OwnerOpeningBalanceDto
from openapi_server.models.owner_opening_balance_in_periods_dto import OwnerOpeningBalanceInPeriodsDto
from openapi_server.models.page_result_supplier_query_dto import PageResultSupplierQueryDto
from openapi_server.models.supplier_dto import SupplierDto


pytestmark = pytest.mark.asyncio

async def test_suppliers_delete(client):
    """Test case for suppliers_delete

    Removes an existing Supplier.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/suppliers/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_get(client):
    """Test case for suppliers_get

    Returns a list of company's Suppliers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" and \"code\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suppliers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_get_account_trans(client):
    """Test case for suppliers_get_account_trans

    Returns a list of Supplier's account transactions.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suppliers/{item_id}/accountTrans'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_get_opening_balance(client):
    """Test case for suppliers_get_opening_balance

    Returns a Supplier's opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suppliers/{item_id}/openingBalance'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_get_opening_balance_list(client):
    """Test case for suppliers_get_opening_balance_list

    Returns a list of Supplier's opening balance transactions.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suppliers/{item_id}/openingBalanceList'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_post(client):
    """Test case for suppliers_post

    Creates a new Supplier.
    """
    body = {"accountName":"Supplier Bank Acc","accountNumber":"12345678","additionalEmails":["email2@example.com","email3@example.com"],"address":["Address Line 1","Address Line 2"],"authCode":"VATEXCODE222","bank":{"branch":"Bank","id":1,"name":"bank Name","sortCode":"B01"},"code":"S001","contact":"John Smith","eFTReference":"Reference","email":"supplier@email.com","fax":"1234567890","id":10589,"mobile":"1234567890","name":"Supplier Name","ourCode":"OURCODE111","ownerTypeId":3,"phone":"1234596970","postponedAccounting":False,"timestamp":"/isQvNRD2wg=","vatAnalysisTypeId":1,"vatReg":"VATCODE0001","vatType":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/suppliers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_process_batch(client):
    """Test case for suppliers_process_batch

    Processes a batch of Suppliers.
    """
    body = [openapi_server.BatchItemSupplierDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/suppliers/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppliers_put(client):
    """Test case for suppliers_put

    Updates an existing Supplier.
    """
    body = {"accountName":"Supplier Bank Acc","accountNumber":"12345678","additionalEmails":["email2@example.com","email3@example.com"],"address":["Address Line 1","Address Line 2"],"authCode":"VATEXCODE222","bank":{"branch":"Bank","id":1,"name":"bank Name","sortCode":"B01"},"code":"S001","contact":"John Smith","eFTReference":"Reference","email":"supplier@email.com","fax":"1234567890","id":10589,"mobile":"1234567890","name":"Supplier Name","ourCode":"OURCODE111","ownerTypeId":3,"phone":"1234596970","postponedAccounting":False,"timestamp":"/isQvNRD2wg=","vatAnalysisTypeId":1,"vatReg":"VATCODE0001","vatType":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/suppliers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_suppliers_id_get(client):
    """Test case for v1_suppliers_id_get

    Returns information about a single Supplier. You may specify that Supplier's ledger balance should be calculated.
    """
    params = [('needBalance', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/suppliers/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

