# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_watchlist_search_read(client):
    """Test case for watchlist_search_read

    Return watchlist search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/watchlist/search/{movie_title}'.format(movie_title='movie_title_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_watchlist_searchall_read(client):
    """Test case for watchlist_searchall_read

    Return watchlist search result
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/v1/watchlist/searchall/{param}'.format(param='param_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

