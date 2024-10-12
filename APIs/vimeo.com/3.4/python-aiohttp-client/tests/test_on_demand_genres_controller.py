# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_genre import OnDemandGenre
from openapi_server.models.on_demand_page import OnDemandPage


pytestmark = pytest.mark.asyncio

async def test_add_vod_genre(client):
    """Test case for add_vod_genre

    Add a genre to an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.genre+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/ondemand/pages/{ondemand_id}/genres/{genre_id}'.format(genre_id='animation', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vod_genre(client):
    """Test case for delete_vod_genre

    Remove a genre from an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.genre+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}/genres/{genre_id}'.format(genre_id='animation', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genre_vod(client):
    """Test case for get_genre_vod

    Get a specific On Demand page in a genre
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/genres/{genre_id}/pages/{ondemand_id}'.format(genre_id='animation', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_genre_vods(client):
    """Test case for get_genre_vods

    Get all the On Demand pages in a genre
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/genres/{genre_id}/pages'.format(genre_id='animation'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_genre(client):
    """Test case for get_vod_genre

    Get a specific On Demand genre
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.genre+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/genres/{genre_id}'.format(genre_id='animation'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_genre_by_ondemand_id(client):
    """Test case for get_vod_genre_by_ondemand_id

    Check whether an On Demand page belongs to a genre
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.genre+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/genres/{genre_id}'.format(genre_id='animation', ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_genres(client):
    """Test case for get_vod_genres

    Get all On Demand genres
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.genre+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/genres',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod_genres_by_ondemand_id(client):
    """Test case for get_vod_genres_by_ondemand_id

    Get all the genres of an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.genre+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}/genres'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

