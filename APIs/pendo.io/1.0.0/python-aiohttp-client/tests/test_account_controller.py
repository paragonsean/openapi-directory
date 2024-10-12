# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.accounts_id_put_request import AccountsIdPutRequest


pytestmark = pytest.mark.asyncio

async def test_accounts_get(client):
    """Test case for accounts_get

    Query accounts
    """
    params = [('limit', 3.4),
                    ('start', 3.4),
                    ('order_dir', 'order_dir_example'),
                    ('order_by', 'order_by_example')]
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_id_delete(client):
    """Test case for accounts_id_delete

    Delete an Account
    """
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{id}'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_id_get(client):
    """Test case for accounts_id_get

    Get an Account
    """
    headers = { 
        'Accept': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{id}'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_id_put(client):
    """Test case for accounts_id_put

    Update an Account
    """
    account = openapi_server.AccountsIdPutRequest()
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/accounts/{id}'.format(id=3.4),
        headers=headers,
        json=account,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_id_tags_delete(client):
    """Test case for accounts_id_tags_delete

    Delete custom Account tags
    """
    headers = { 
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/accounts/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_accounts_id_tags_get(client):
    """Test case for accounts_id_tags_get

    Get custom Account tags
    """
    headers = { 
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/accounts/{id}/tags'.format(id=3.4),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_accounts_id_tags_post(client):
    """Test case for accounts_id_tags_post

    Overwrite current custom Account tags with the given tags
    """
    tags = None
    headers = { 
        'Content-Type': 'application/json',
        'userApiKey (request header)': 'special-key',
        'userApiKey (query parameter)': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/accounts/{id}/tags'.format(id=3.4),
        headers=headers,
        json=tags,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

