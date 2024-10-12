# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_movie_recommendations(client):
    """Test case for get_movie_recommendations

    Get movie recommendations
    """
    params = [('ignore_collected', 'false'),
                    ('ignore_watchlisted', 'false')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/recommendations/movies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_show_recommendations(client):
    """Test case for get_show_recommendations

    Get show recommendations
    """
    params = [('ignore_collected', 'false'),
                    ('ignore_watchlisted', 'false')]
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/recommendations/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hide_a_movie_recommendation(client):
    """Test case for hide_a_movie_recommendation

    Hide a movie recommendation
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/recommendations/movies/{id}'.format(id='922'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hide_a_show_recommendation(client):
    """Test case for hide_a_show_recommendation

    Hide a show recommendation
    """
    headers = { 
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/recommendations/shows/{id}'.format(id='922'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

