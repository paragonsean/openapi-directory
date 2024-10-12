# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_album(client):
    """Test case for get_instant_mix_from_album

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Albums/{id}/InstantMix'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_artists(client):
    """Test case for get_instant_mix_from_artists

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Artists/{id}/InstantMix'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_item(client):
    """Test case for get_instant_mix_from_item

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Items/{id}/InstantMix'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_music_genre(client):
    """Test case for get_instant_mix_from_music_genre

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/MusicGenres/{name}/InstantMix'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_music_genres(client):
    """Test case for get_instant_mix_from_music_genres

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/MusicGenres/{id}/InstantMix'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_playlist(client):
    """Test case for get_instant_mix_from_playlist

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Playlists/{id}/InstantMix'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_instant_mix_from_song(client):
    """Test case for get_instant_mix_from_song

    Creates an instant playlist based on a given song.
    """
    params = [('userId', 'user_id_example'),
                    ('limit', 56),
                    ('fields', [openapi_server.ItemFields()]),
                    ('enableImages', True),
                    ('enableUserData', True),
                    ('imageTypeLimit', 56),
                    ('enableImageTypes', [openapi_server.ImageType()])]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Songs/{id}/InstantMix'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

