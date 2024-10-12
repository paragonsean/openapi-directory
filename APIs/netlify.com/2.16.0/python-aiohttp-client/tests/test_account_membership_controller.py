# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_membership import AccountMembership
from openapi_server.models.account_setup import AccountSetup
from openapi_server.models.account_update_setup import AccountUpdateSetup
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_cancel_account(client):
    """Test case for cancel_account

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_account(client):
    """Test case for create_account

    
    """
    account_setup = openapi_server.AccountSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/accounts',
        headers=headers,
        json=account_setup,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_accounts_for_user(client):
    """Test case for list_accounts_for_user

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/accounts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account(client):
    """Test case for update_account

    
    """
    account_update_setup = openapi_server.AccountUpdateSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/accounts/{account_id}'.format(account_id='account_id_example'),
        headers=headers,
        json=account_update_setup,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

