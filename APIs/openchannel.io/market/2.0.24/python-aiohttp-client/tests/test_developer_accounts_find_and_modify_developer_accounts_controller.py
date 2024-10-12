# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.developer_account import DeveloperAccount
from openapi_server.models.developer_account_pages import DeveloperAccountPages


pytestmark = pytest.mark.asyncio

async def test_developer_accounts_developer_account_id_delete(client):
    """Test case for developer_accounts_developer_account_id_delete

    Removes the developer account
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/developerAccounts/{developer_account_id}'.format(developer_account_id='developer_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developer_accounts_developer_account_id_get(client):
    """Test case for developer_accounts_developer_account_id_get

    Returns a single developer account
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/developerAccounts/{developer_account_id}'.format(developer_account_id='developer_account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developer_accounts_developer_account_id_patch(client):
    """Test case for developer_accounts_developer_account_id_patch

    Updates the developer account fields
    """
    params = [('developerId', 'developer_id_example'),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/developerAccounts/{developer_account_id}'.format(developer_account_id='developer_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developer_accounts_developer_account_id_post(client):
    """Test case for developer_accounts_developer_account_id_post

    Updates the developer account or adds the developer account if it doesn't exist
    """
    params = [('developerId', 'developer_id_example'),
                    ('email', 'email_example'),
                    ('name', 'name_example'),
                    ('customData', 'custom_data_example')]
    headers = { 
        'Accept': '*/*',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/v2/developerAccounts/{developer_account_id}'.format(developer_account_id='developer_account_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_developer_accounts_get(client):
    """Test case for developer_accounts_get

    Returns a paginated list of developerAccounts
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
        path='/v2/developerAccounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

