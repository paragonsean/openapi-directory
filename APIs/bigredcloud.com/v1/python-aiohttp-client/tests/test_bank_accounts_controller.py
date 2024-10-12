# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bank_account_dto import BankAccountDto
from openapi_server.models.batch_item_bank_account_dto import BatchItemBankAccountDto
from openapi_server.models.page_result_bank_account_query_dto import PageResultBankAccountQueryDto


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_delete(client):
    """Test case for bank_accounts_delete

    Removes an existing Bank Account.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/bankAccounts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_get(client):
    """Test case for bank_accounts_get

    Returns a list of company's Bank Account. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \"id\" and \"acCode\" fields.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/bankAccounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_post(client):
    """Test case for bank_accounts_post

    Creates a new Bank Account.
    """
    body = {"acCode":"B1","accountName":"","accountNumber":"83700896","address":["Address Line 1","Address Line 2"],"bankFeedSource":0,"businessIdentifierCodes":"AIBKIE2D","categoryId":41704,"creditorScheme":"XXXX","details":"Bank_1","id":1,"internationalBankAccountNumber":"IE67 BOFI 9027 0925 7277 59","isDefaultBank":False,"lastChq":"000005","nominalAcCode":"B101","oBalance":0,"sortCode":"900284","timestamp":"QUFBQUFBQUFDcXc9"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/bankAccounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_process_batch(client):
    """Test case for bank_accounts_process_batch

    Processes a batch of Bank Accounts.
    """
    body = [openapi_server.BatchItemBankAccountDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/bankAccounts/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_bank_accounts_put(client):
    """Test case for bank_accounts_put

    Updates an existing Bank Account.
    """
    body = {"acCode":"B1","accountName":"","accountNumber":"83700896","address":["Address Line 1","Address Line 2"],"bankFeedSource":0,"businessIdentifierCodes":"AIBKIE2D","categoryId":41704,"creditorScheme":"XXXX","details":"Bank_1","id":1,"internationalBankAccountNumber":"IE67 BOFI 9027 0925 7277 59","isDefaultBank":False,"lastChq":"000005","nominalAcCode":"B101","oBalance":0,"sortCode":"900284","timestamp":"QUFBQUFBQUFDcXc9"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/bankAccounts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_bank_accounts_id_get(client):
    """Test case for v1_bank_accounts_id_get

    Returns information about a single Bank Account.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/bankAccounts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

