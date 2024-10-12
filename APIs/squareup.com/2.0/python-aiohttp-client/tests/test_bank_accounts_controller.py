# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_bank_account_by_v1_id_response import GetBankAccountByV1IdResponse
from openapi_server.models.get_bank_account_response import GetBankAccountResponse
from openapi_server.models.list_bank_accounts_response import ListBankAccountsResponse


pytestmark = pytest.mark.asyncio

async def test_get_bank_account(client):
    """Test case for get_bank_account

    GetBankAccount
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bank-accounts/{bank_account_id}'.format(bank_account_id='bank_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_bank_account_by_v1_id(client):
    """Test case for get_bank_account_by_v1_id

    GetBankAccountByV1Id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bank-accounts/by-v1-id/{v1_bank_account_id}'.format(v1_bank_account_id='v1_bank_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_bank_accounts(client):
    """Test case for list_bank_accounts

    ListBankAccounts
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 56),
                    ('location_id', 'location_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/bank-accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

