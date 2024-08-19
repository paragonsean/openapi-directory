# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.episode_object import EpisodeObject
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_multiple_episodes200_response import GetMultipleEpisodes200Response
from openapi_server.models.paging_saved_episode_object import PagingSavedEpisodeObject
from openapi_server.models.paging_simplified_episode_object import PagingSimplifiedEpisodeObject
from openapi_server.models.remove_episodes_user_request import RemoveEpisodesUserRequest
from openapi_server.models.save_episodes_user_request import SaveEpisodesUserRequest


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_episodes(client):
    """Test case for check_users_saved_episodes

    Check User's Saved Episodes 
    """
    params = [('ids', '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/episodes/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_shows_episodes_0(client):
    """Test case for get_a_shows_episodes_0

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

async def test_get_an_episode(client):
    """Test case for get_an_episode

    Get Episode 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/episodes/{id}'.format(id='512ojhOuo1ktJprKbVcKyQ'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_episodes(client):
    """Test case for get_multiple_episodes

    Get Several Episodes 
    """
    params = [('ids', '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf'),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/episodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_episodes(client):
    """Test case for get_users_saved_episodes

    Get User's Saved Episodes 
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
        path='/v1/me/episodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_episodes_user(client):
    """Test case for remove_episodes_user

    Remove User's Saved Episodes 
    """
    body = openapi_server.RemoveEpisodesUserRequest()
    params = [('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/episodes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_episodes_user(client):
    """Test case for save_episodes_user

    Save Episodes for Current User 
    """
    body = openapi_server.SaveEpisodesUserRequest()
    params = [('ids', '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/episodes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

