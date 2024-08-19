# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_shows200_response import GetMultipleShows200Response
from openapi_server.models.paging_saved_show_object import PagingSavedShowObject
from openapi_server.models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from openapi_server.models.show_object import ShowObject


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_shows(client):
    """Test case for check_users_saved_shows

    Check User's Saved Shows 
    """
    params = [('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/shows/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_show(client):
    """Test case for get_a_show

    Get Show 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shows/{id}'.format(id='38bS44xjbVVZ3No3ByF1dJ'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_shows_episodes(client):
    """Test case for get_a_shows_episodes

    Get Show Episodes 
    """
    params = [('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shows/{id}/episodes'.format(id='38bS44xjbVVZ3No3ByF1dJ'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_shows(client):
    """Test case for get_multiple_shows

    Get Several Shows 
    """
    params = [('market', 'ES'),
                    ('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_shows(client):
    """Test case for get_users_saved_shows

    Get User's Saved Shows 
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_shows_user(client):
    """Test case for remove_shows_user

    Remove User's Saved Shows 
    """
    params = [('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ'),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_shows_user(client):
    """Test case for save_shows_user

    Save Shows for Current User 
    """
    params = [('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

