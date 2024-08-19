# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.user_account import UserAccount
from openapi_server.models.user_account_pages import UserAccountPages


pytestmark = pytest.mark.asyncio

async def test_user_accounts_get(client):
    """Test case for user_accounts_get

    Returns a paginated list of userAccounts
    """
    params = [('query', 'query_example'),
                    ('sort', 'sort_example'),
                    ('pageNumber', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/userAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_accounts_user_account_id_delete(client):
    """Test case for user_accounts_user_account_id_delete

    Removes the user account
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/userAccounts/{user_account_id}'.format(user_account_id='user_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_accounts_user_account_id_get(client):
    """Test case for user_accounts_user_account_id_get

    Returns a single user account
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/userAccounts/{user_account_id}'.format(user_account_id='user_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_accounts_user_account_id_patch(client):
    """Test case for user_accounts_user_account_id_patch

    Updates the user account fields
    """
    params = [('userId', 'user_id_example'),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/userAccounts/{user_account_id}'.format(user_account_id='user_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_user_accounts_user_account_id_post(client):
    """Test case for user_accounts_user_account_id_post

    Updates the user account or adds the user account if it doesn't exist
    """
    params = [('userId', 'user_id_example'),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/userAccounts/{user_account_id}'.format(user_account_id='user_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

