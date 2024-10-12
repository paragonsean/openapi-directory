# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album_object import AlbumObject
from openapi_server.models.get_multiple_albums200_response import GetMultipleAlbums200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_new_releases200_response import GetNewReleases200Response
from openapi_server.models.paging_saved_album_object import PagingSavedAlbumObject
from openapi_server.models.paging_simplified_album_object import PagingSimplifiedAlbumObject
from openapi_server.models.paging_simplified_track_object import PagingSimplifiedTrackObject
from openapi_server.models.save_albums_user_request import SaveAlbumsUserRequest


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_albums(client):
    """Test case for check_users_saved_albums

    Check User's Saved Albums 
    """
    params = [('ids', '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/albums/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_album(client):
    """Test case for get_an_album

    Get Album 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/albums/{id}'.format(id='4aawyAB9vmqN3uQ7FjRGTy'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_albums_tracks(client):
    """Test case for get_an_albums_tracks

    Get Album Tracks 
    """
    params = [('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/albums/{id}/tracks'.format(id='4aawyAB9vmqN3uQ7FjRGTy'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_an_artists_albums_0(client):
    """Test case for get_an_artists_albums_0

    Get Artist's Albums 
    """
    params = [('include_groups', 'single,appears_on'),
                    ('market', 'ES'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists/{id}/albums'.format(id='0TnOYISbd1XYRBk9myaseg'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_multiple_albums(client):
    """Test case for get_multiple_albums

    Get Several Albums 
    """
    params = [('ids', '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc'),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/albums',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_new_releases(client):
    """Test case for get_new_releases

    Get New Releases 
    """
    params = [('country', 'SE'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/browse/new-releases',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_albums(client):
    """Test case for get_users_saved_albums

    Get User's Saved Albums 
    """
    params = [('limit', 20),
                    ('offset', 0),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/albums',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_albums_user(client):
    """Test case for remove_albums_user

    Remove Users' Saved Albums 
    """
    body = openapi_server.SaveAlbumsUserRequest()
    params = [('ids', '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/albums',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_albums_user(client):
    """Test case for save_albums_user

    Save Albums for Current User 
    """
    body = openapi_server.SaveAlbumsUserRequest()
    params = [('ids', '382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/albums',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

