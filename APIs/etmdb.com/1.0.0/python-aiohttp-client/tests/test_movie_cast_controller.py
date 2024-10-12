# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_movie_cast_search_read(client):
    """Test case for movie_cast_search_read

    Return movie cast search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/movie-cast/search/{movie_title}'.format(movie_title='movie_title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_movie_cast_searchall_read(client):
    """Test case for movie_cast_searchall_read

    Return movie cast search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/movie-cast/searchall/{param}'.format(param='param_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

