# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_a_single_episode_for_a_show(client):
    """Test case for get_a_single_episode_for_a_show

    Get a single episode for a show
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}'.format(id='game-of-thrones', season=1, episode=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_episode_comments(client):
    """Test case for get_all_episode_comments

    Get all episode comments
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/comments/{sort}'.format(id='game-of-thrones', season=1, episode=1, sort='newest'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_episode_translations(client):
    """Test case for get_all_episode_translations

    Get all episode translations
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/translations/{language}'.format(id='game-of-thrones', season=1, episode=1, language='es'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_people_for_an_episode(client):
    """Test case for get_all_people_for_an_episode

    Get all people for an episode
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/people'.format(id='game-of-thrones', season=1, episode=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episode_ratings(client):
    """Test case for get_episode_ratings

    Get episode ratings
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/ratings'.format(id='game-of-thrones', season=1, episode=12),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episode_stats(client):
    """Test case for get_episode_stats

    Get episode stats
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/stats'.format(id='game-of-thrones', season=1, episode=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_containing_this_episode(client):
    """Test case for get_lists_containing_this_episode

    Get lists containing this episode
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/lists/{type}/{sort}'.format(id='game-of-thrones', season=1, episode=1, type='personal', sort='popular'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shows_id_seasons_season_episodes_episode_watching_get(client):
    """Test case for shows_id_seasons_season_episodes_episode_watching_get

    Get users watching right now
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/episodes/{episode}/watching'.format(id='game-of-thrones', season=1, episode=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

