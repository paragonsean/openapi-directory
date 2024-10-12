# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts import Accounts


pytestmark = pytest.mark.asyncio

async def test_delete_account(client):
    """Test case for delete_account

    Delete specific account
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/accounts/{accountid}'.format(serverid='serverid_example', accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_accounts_0(client):
    """Test case for delete_user_accounts_0

    Delete all accounts of a specific user
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/users/{userid}/accounts'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account(client):
    """Test case for get_account

    Get specific account
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/accounts/{accountid}'.format(serverid='serverid_example', accountid=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_accounts(client):
    """Test case for get_all_accounts

    Get all accounts
    """
    params = [('filter', 'filter_example'),
                    ('limit', 56),
                    ('marker', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/accounts'.format(serverid='serverid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_0(client):
    """Test case for get_user_0

    Get all accounts of a specific user
    """
    params = [('limit', 56),
                    ('marker', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/users/{userid}/accounts'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account(client):
    """Test case for update_account

    Update specific account
    """
    params = [('blocked', True)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}/accounts/{accountid}'.format(serverid='serverid_example', accountid=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_account_user(client):
    """Test case for update_account_user

    Update user of the given account.
    """
    params = [('userid', 'userid_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}/accounts/{accountid}/user'.format(serverid='serverid_example', accountid=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

