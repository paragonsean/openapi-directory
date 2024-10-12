# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts
from openapi_server.models.new_account import NewAccount


pytestmark = pytest.mark.asyncio

async def test_add_account(client):
    """Test case for add_account

    Add a new account
    """
    body = openapi_server.NewAccount()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/accounts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_by_id(client):
    """Test case for get_account_by_id

    Retrieve the details of a fire.com Account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/accounts/{ican}'.format(ican=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_accounts(client):
    """Test case for get_accounts

    List all fire.com Accounts
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

