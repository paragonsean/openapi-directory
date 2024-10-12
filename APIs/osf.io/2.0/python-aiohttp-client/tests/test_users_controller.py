# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.addon_account import AddonAccount
from openapi_server.models.institution import Institution
from openapi_server.models.node import Node
from openapi_server.models.preprint import Preprint
from openapi_server.models.user import User
from openapi_server.models.user_addon import UserAddon


pytestmark = pytest.mark.asyncio

async def test_users_addon_accounts_list(client):
    """Test case for users_addon_accounts_list

    List all addon accounts
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/addons/{provider}/accounts'.format(user_id='user_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_addon_accounts_read(client):
    """Test case for users_addon_accounts_read

    Retrieve an addon account
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/addons/{provider}/accounts/{account_id}'.format(user_id='user_id_example', provider='provider_example', account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_addons_list(client):
    """Test case for users_addons_list

    List all user addons
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/addons'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_addons_read(client):
    """Test case for users_addons_read

    Retrieve a user addon
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/addons/{provider}'.format(user_id='user_id_example', provider='provider_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_institutions_list(client):
    """Test case for users_institutions_list

    List all institutions
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/institutions'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list(client):
    """Test case for users_list

    List all users
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_nodes_list(client):
    """Test case for users_nodes_list

    List all nodes
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/nodes'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_partial_update(client):
    """Test case for users_partial_update

    Update a user
    """
    body = {"data":{"attributes":{"full_name":"Casey M. Rollins","middle_names":"Marie"},"id":"{user_id}","type":"users"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_preprints_list(client):
    """Test case for users_preprints_list

    List all preprints
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/preprints'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_read(client):
    """Test case for users_read

    Retrieve a user
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_registrations_list(client):
    """Test case for users_registrations_list

    List all registrations
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user_id}/registrations'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

