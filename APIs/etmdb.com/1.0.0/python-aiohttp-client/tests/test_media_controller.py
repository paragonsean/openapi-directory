# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_media_search_read(client):
    """Test case for media_search_read

    Return movie media search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/media/search/{movie_title}'.format(movie_title='movie_title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_media_searchall_read(client):
    """Test case for media_searchall_read

    Return cast media search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/media/searchall/{user}'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

