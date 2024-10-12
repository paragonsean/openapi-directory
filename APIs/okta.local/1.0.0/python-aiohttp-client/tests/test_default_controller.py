# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_clear_user_sessions(client):
    """Test case for clear_user_sessions

    Clear User Sessions
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/users/{user_id}/sessions'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_find_user(client):
    """Test case for find_user

    Find User
    """
    params = [('q', 'user')]
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_get_assigned_app_links(client):
    """Test case for get_assigned_app_links

    Get Assigned App Links
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}/appLinks'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_get_current_user(client):
    """Test case for get_current_user

    Get Current User
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_get_groups_for_user(client):
    """Test case for get_groups_for_user

    Get Groups for User
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}/groups'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_get_user(client):
    """Test case for get_user

    Get User
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/users/{user_id}'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/octet-stream not supported by Connexion")
async def test_reset_factors(client):
    """Test case for reset_factors

    Reset Factors
    """
    headers = { 
        'Content-Type': 'application/octet-stream',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/users/{user_id}/lifecycle/reset_factors'.format(user_id='user_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

