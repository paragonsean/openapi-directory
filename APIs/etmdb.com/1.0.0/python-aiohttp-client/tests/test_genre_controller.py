# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_genre_search_read(client):
    """Test case for genre_search_read

    Return movie genre search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/genre/search/{movie_title}'.format(movie_title='movie_title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_genre_searchall_read(client):
    """Test case for genre_searchall_read

    Return movie genre search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/genre/searchall/{movie_genre_type}'.format(movie_genre_type='movie_genre_type_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

