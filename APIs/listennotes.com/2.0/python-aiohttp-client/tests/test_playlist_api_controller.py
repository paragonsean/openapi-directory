# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.playlist_response import PlaylistResponse
from openapi_server.models.playlists_response import PlaylistsResponse


pytestmark = pytest.mark.asyncio

async def test_get_playlist_by_id(client):
    """Test case for get_playlist_by_id

    Fetch a playlist's info and items (i.e., episodes or podcasts).
    """
    params = [('type', episode_list),
                    ('last_timestamp_ms', 0),
                    ('sort', recent_added_first)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/playlists/{id}'.format(id='m1pe7z60bsw'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playlists(client):
    """Test case for get_playlists

    Fetch a list of your playlists.
    """
    params = [('sort', recent_added_first),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
        'x_listen_api_key': 'x_listen_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/playlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

