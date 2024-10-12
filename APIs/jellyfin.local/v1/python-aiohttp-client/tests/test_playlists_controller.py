# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.create_playlist_dto import CreatePlaylistDto
from openapi_server.models.image_type import ImageType
from openapi_server.models.item_fields import ItemFields
from openapi_server.models.playlist_creation_result import PlaylistCreationResult


pytestmark = pytest.mark.asyncio

async def test_add_to_playlist(client):
    """Test case for add_to_playlist

    Adds items to a playlist.
    """
    params = [('ids', ['ids_example']),
                    ('userId', 'user_id_example')]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Playlists/{playlist_id}/Items'.format(playlist_id='playlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_playlist(client):
    """Test case for create_playlist

    Creates a new playlist.
    """
    body = {"UserId":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Ids":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"MediaType":"MediaType","Name":"Name"}
    params = [('name', 'name_example'),
                    ('ids', ['ids_example']),
                    ('userId', 'user_id_example'),
                    ('mediaType', 'media_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Playlists',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playlist_items(client):
    """Test case for get_playlist_items

    Gets the original items of a playlist.
    """
    params = [('userId', 'user_id_example'),
                    ('startIndex', 56),
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
        path='/Playlists/{playlist_id}/Items'.format(playlist_id='playlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_move_item(client):
    """Test case for move_item

    Moves a playlist item.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Playlists/{playlist_id}/Items/{item_id}/Move/{new_index}'.format(playlist_id='playlist_id_example', item_id='item_id_example', new_index=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_from_playlist(client):
    """Test case for remove_from_playlist

    Removes items from a playlist.
    """
    params = [('entryIds', ['entry_ids_example'])]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Playlists/{playlist_id}/Items'.format(playlist_id='playlist_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

