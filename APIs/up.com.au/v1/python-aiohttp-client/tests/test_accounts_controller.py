# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_type_enum import AccountTypeEnum
from openapi_server.models.get_account_response import GetAccountResponse
from openapi_server.models.list_accounts_response import ListAccountsResponse
from openapi_server.models.ownership_type_enum import OwnershipTypeEnum


pytestmark = pytest.mark.asyncio

async def test_accounts_get(client):
    """Test case for accounts_get

    List accounts
    """
    params = [('page[size]', 30),
                    ('filter[accountType]', openapi_server.AccountTypeEnum()),
                    ('filter[ownershipType]', openapi_server.OwnershipTypeEnum())]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_id_get(client):
    """Test case for accounts_id_get

    Retrieve account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{id}'.format(id='92b41408-6b7b-4fca-982b-3fb1fdd77220'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

