# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_tran_dto import AccountTranDto
from openapi_server.models.batch_item_customer_dto import BatchItemCustomerDto
from openapi_server.models.customer_dto import CustomerDto
from openapi_server.models.owner_opening_balance_dto import OwnerOpeningBalanceDto
from openapi_server.models.owner_opening_balance_in_periods_dto import OwnerOpeningBalanceInPeriodsDto
from openapi_server.models.page_result_customer_query_dto import PageResultCustomerQueryDto
from openapi_server.models.quote_dto import QuoteDto


pytestmark = pytest.mark.asyncio

async def test_customers_delete(client):
    """Test case for customers_delete

    Removes an existing Customer.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/customers/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get(client):
    """Test case for customers_get

    Returns a list of company's Customers. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" and \"code\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_account_trans(client):
    """Test case for customers_get_account_trans

    Returns a list of Customer's account transactions.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{item_id}/accountTrans'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_opening_balance(client):
    """Test case for customers_get_opening_balance

    Returns a Customer's opening balances, calculated for the next periods: current month, one month old, two months old, three and more months old.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{item_id}/openingBalance'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_opening_balance_list(client):
    """Test case for customers_get_opening_balance_list

    Returns a list of Customer's opening balance transactions.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{item_id}/openingBalanceList'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_quotes(client):
    """Test case for customers_get_quotes

    Returns a list of Customer's quotes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{item_id}/quotes'.format(item_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_post(client):
    """Test case for customers_post

    Creates a new Customer.
    """
    body = {"accountName":"","accountNumber":"12345678","additionalEmails":["email2@example.com","email3@example.com"],"address":["Address Line 1","Address Line 2"],"authCode":"VATEXCODE222","bank":{"branch":"Bank","id":1,"name":"bank Name","sortCode":"B01"},"businessIdentifierCode":"AIBI02","code":"12345678","contact":"John Smith","delivery":["Delivery 1","Delivery 2"],"eFTReference":"Reference","email":"customer@email.com","fax":"1234567890","id":10589,"internationalBankAccountNumber":"1233432532","mobile":"1234567890","name":"Customer Name 1","ourCode":"OURCODE111","ownerTypeId":1,"phone":"1234596970","timestamp":"MKXIu9RD2wg=","vatAnalysisTypeId":1,"vatReg":"VATCODE0001","vatType":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/customers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_process_batch(client):
    """Test case for customers_process_batch

    Processes a batch of Customers.
    """
    body = [openapi_server.BatchItemCustomerDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/customers/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_put(client):
    """Test case for customers_put

    Updates an existing Customer.
    """
    body = {"accountName":"","accountNumber":"12345678","additionalEmails":["email2@example.com","email3@example.com"],"address":["Address Line 1","Address Line 2"],"authCode":"VATEXCODE222","bank":{"branch":"Bank","id":1,"name":"bank Name","sortCode":"B01"},"businessIdentifierCode":"AIBI02","code":"12345678","contact":"John Smith","delivery":["Delivery 1","Delivery 2"],"eFTReference":"Reference","email":"customer@email.com","fax":"1234567890","id":10589,"internationalBankAccountNumber":"1233432532","mobile":"1234567890","name":"Customer Name 1","ourCode":"OURCODE111","ownerTypeId":1,"phone":"1234596970","timestamp":"MKXIu9RD2wg=","vatAnalysisTypeId":1,"vatReg":"VATCODE0001","vatType":2}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/customers/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_customers_id_get(client):
    """Test case for v1_customers_id_get

    Returns information about a single Customer. You may specify that Customer's ledger balance should be calculated.
    """
    params = [('needBalance', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/customers/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

