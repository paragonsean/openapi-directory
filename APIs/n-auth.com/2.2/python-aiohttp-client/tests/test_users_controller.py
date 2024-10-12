# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.accounts import Accounts
from openapi_server.models.users import Users


pytestmark = pytest.mark.asyncio

async def test_delete_user(client):
    """Test case for delete_user

    Delete a specific user
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/users/{userid}'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_accounts(client):
    """Test case for delete_user_accounts

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

async def test_delete_user_attribute(client):
    """Test case for delete_user_attribute

    Delete specific attribute of a specific user
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/users/{userid}/attributes/{attributekey}'.format(serverid='serverid_example', userid='userid_example', attributekey='attributekey_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_user_attributes(client):
    """Test case for delete_user_attributes

    Delete all attributes of a specific user
    """
    headers = { 
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/servers/{serverid}/users/{userid}/attributes'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

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

async def test_get_user_attributes(client):
    """Test case for get_user_attributes

    Get all attributes of a specific user
    """
    headers = { 
        'Accept': 'text/plain',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/servers/{serverid}/users/{userid}/attributes'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users(client):
    """Test case for get_users

    Get all users
    """
    params = [('filter', 'filter_example'),
                    ('search', 'search_example'),
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
        path='/servers/{serverid}/users'.format(serverid='serverid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_register_user(client):
    """Test case for register_user

    Register a userid for the currently logged in account.
    """
    params = [('userid', 'userid_example')]
    headers = { 
        'x_nonce': 'x_nonce_example',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/sessions/registeruser'.format(serverid='serverid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_set_user_attributes(client):
    """Test case for set_user_attributes

    Set all attributes of a specific user
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/servers/{serverid}/users/{userid}/attributes'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_update_user_attributes(client):
    """Test case for update_user_attributes

    Update specified attributes of a specific user
    """
    attributes = None
    headers = { 
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'role_id': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/servers/{serverid}/users/{userid}/attributes'.format(serverid='serverid_example', userid='userid_example'),
        headers=headers,
        json=attributes,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

