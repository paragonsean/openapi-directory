# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album_get_get200_response import AlbumGetGet200Response
from openapi_server.models.artist_albums_get_get200_response import ArtistAlbumsGetGet200Response


pytestmark = pytest.mark.asyncio

async def test_album_get_get(client):
    """Test case for album_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('album_id', 'album_id_example')]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/album.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_artist_albums_get_get(client):
    """Test case for artist_albums_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('artist_id', 'artist_id_example'),
                    ('s_release_date', 's_release_date_example'),
                    ('g_album_name', 'g_album_name_example'),
                    ('page_size', 3.4),
                    ('page', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/artist.albums.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

