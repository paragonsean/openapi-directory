# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.label import Label
from openapi_server.models.presence import Presence
from openapi_server.models.support_info import SupportInfo
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_get_label(client):
    """Test case for get_label

    Returns all user labels
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/labels',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_presence(client):
    """Test case for get_presence

    Gets the presence status
    """
    params = [('userIds', ['user_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/presence',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile(client):
    """Test case for get_profile

    Gets the authenticated user's profile information
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_support_info(client):
    """Test case for get_support_info

    Gets the support information
    """
    headers = { 
        'Accept': '*/*',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/supportinfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_by_email_address(client):
    """Test case for get_user_by_email_address

    Get user by email
    """
    params = [('secondaryLookup', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/{email_address}/getUserByEmail'.format(email_address='email_address_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_by_id(client):
    """Test case for get_user_by_id

    Gets the user's profile information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_presence(client):
    """Test case for get_user_presence

    Gets the presence status
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/{id}/presence'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_user(client):
    """Test case for search_user

    Search for users
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_users_list(client):
    """Test case for search_users_list

    Search multiple users.
    """
    params = [('name', ['name_example']),
                    ('returnFullUserInfo', False),
                    ('secondaryLookup', False)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest/v2/users/list',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_set_user_presence(client):
    """Test case for set_user_presence

    Updates the presence status
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Bearer special-key',
    }
    data = {
        'clear_dnd': False,
        'dnd_until': '2013-10-20T19:20:30+01:00',
        'state': 'state_example',
        'status_message': 'status_message_example'
        }
    response = await client.request(
        method='PUT',
        path='/rest/v2/users/presence',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

