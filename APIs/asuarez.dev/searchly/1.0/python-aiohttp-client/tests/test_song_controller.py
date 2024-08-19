# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_response_song import APIResponseSong


pytestmark = pytest.mark.asyncio

async def test_src_searchly_api_v1_controllers_song_search(client):
    """Test case for src_searchly_api_v1_controllers_song_search

    API endpoint to search songs from the database given a query
    """
    params = [('query', 'Miley Cyrus')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/song/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

