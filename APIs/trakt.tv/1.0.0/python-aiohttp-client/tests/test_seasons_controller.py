# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_all_people_for_a_season(client):
    """Test case for get_all_people_for_a_season

    Get all people for a season
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/people'.format(id='game-of-thrones', season=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_season_comments(client):
    """Test case for get_all_season_comments

    Get all season comments
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/comments/{sort}'.format(id='game-of-thrones', season=1, sort='newest'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_season_translations(client):
    """Test case for get_all_season_translations

    Get all season translations
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/translations/{language}'.format(id='game-of-thrones', season=1, language='es'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_seasons_for_a_show(client):
    """Test case for get_all_seasons_for_a_show

    Get all seasons for a show
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons'.format(id='game-of-thrones'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_lists_containing_this_season(client):
    """Test case for get_lists_containing_this_season

    Get lists containing this season
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/lists/{type}/{sort}'.format(id='game-of-thrones', season=1, type='personal', sort='popular'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_season_ratings(client):
    """Test case for get_season_ratings

    Get season ratings
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/ratings'.format(id='game-of-thrones', season=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_season_stats(client):
    """Test case for get_season_stats

    Get season stats
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/stats'.format(id='game-of-thrones', season=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_single_season_for_a_show(client):
    """Test case for get_single_season_for_a_show

    Get single season for a show
    """
    params = [('translations', 'es')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}'.format(id='game-of-thrones', season=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shows_id_seasons_season_watching_get(client):
    """Test case for shows_id_seasons_season_watching_get

    Get users watching right now
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/shows/{id}/seasons/{season}/watching'.format(id='game-of-thrones', season=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

