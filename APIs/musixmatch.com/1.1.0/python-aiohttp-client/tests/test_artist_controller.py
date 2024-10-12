# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.artist_get_get200_response import ArtistGetGet200Response
from openapi_server.models.artist_related_get_get200_response import ArtistRelatedGetGet200Response
from openapi_server.models.chart_artists_get_get200_response import ChartArtistsGetGet200Response


pytestmark = pytest.mark.asyncio

async def test_artist_get_get(client):
    """Test case for artist_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('artist_id', 'artist_id_example')]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/artist.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artist_related_get_get(client):
    """Test case for artist_related_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('artist_id', 'artist_id_example'),
                    ('page_size', 3.4),
                    ('page', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/artist.related.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artist_search_get(client):
    """Test case for artist_search_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('q_artist', 'q_artist_example'),
                    ('f_artist_id', 3.4),
                    ('page', 3.4),
                    ('page_size', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/artist.search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_artists_get_get(client):
    """Test case for chart_artists_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('page', 3.4),
                    ('page_size', 3.4),
                    ('country', 'us')]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/chart.artists.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

