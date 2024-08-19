# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_tracks_to_playlist_request import AddTracksToPlaylistRequest
from openapi_server.models.change_playlist_details_request import ChangePlaylistDetailsRequest
from openapi_server.models.create_playlist_request import CreatePlaylistRequest
from openapi_server.models.follow_playlist_request import FollowPlaylistRequest
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.image_object import ImageObject
from openapi_server.models.paging_featured_playlist_object import PagingFeaturedPlaylistObject
from openapi_server.models.paging_playlist_object import PagingPlaylistObject
from openapi_server.models.paging_playlist_track_object import PagingPlaylistTrackObject
from openapi_server.models.playlist_object import PlaylistObject
from openapi_server.models.remove_tracks_playlist_request import RemoveTracksPlaylistRequest
from openapi_server.models.reorder_or_replace_playlists_tracks200_response import ReorderOrReplacePlaylistsTracks200Response
from openapi_server.models.reorder_or_replace_playlists_tracks_request import ReorderOrReplacePlaylistsTracksRequest


pytestmark = pytest.mark.asyncio

async def test_add_tracks_to_playlist(client):
    """Test case for add_tracks_to_playlist

    Add Items to Playlist 
    """
    body = openapi_server.AddTracksToPlaylistRequest()
    params = [('position', 0),
                    ('uris', 'spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/playlists/{playlist_id}/tracks'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_change_playlist_details(client):
    """Test case for change_playlist_details

    Change Playlist Details 
    """
    body = openapi_server.ChangePlaylistDetailsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/playlists/{playlist_id}'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_user_follows_playlist_0(client):
    """Test case for check_if_user_follows_playlist_0

    Check if Users Follow Playlist 
    """
    params = [('ids', 'jmperezperez,thelinmichael,wizzler')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/playlists/{playlist_id}/followers/contains'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_playlist(client):
    """Test case for create_playlist

    Create Playlist 
    """
    body = openapi_server.CreatePlaylistRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/users/{user_id}/playlists'.format(user_id='smedjan'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_follow_playlist_0(client):
    """Test case for follow_playlist_0

    Follow Playlist 
    """
    body = openapi_server.FollowPlaylistRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/playlists/{playlist_id}/followers'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_categories_playlists(client):
    """Test case for get_a_categories_playlists

    Get Category's Playlists 
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
        path='/v1/browse/categories/{category_id}/playlists'.format(category_id='dinner'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_a_list_of_current_users_playlists(client):
    """Test case for get_a_list_of_current_users_playlists

    Get Current User's Playlists 
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/playlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_featured_playlists(client):
    """Test case for get_featured_playlists

    Get Featured Playlists 
    """
    params = [('country', 'SE'),
                    ('locale', 'sv_SE'),
                    ('timestamp', '2014-10-23T09:00:00'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/browse/featured-playlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_users_playlists(client):
    """Test case for get_list_users_playlists

    Get User's Playlists 
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}/playlists'.format(user_id='smedjan'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playlist(client):
    """Test case for get_playlist

    Get Playlist 
    """
    params = [('market', 'ES'),
                    ('fields', 'items(added_by.id,track(name,href,album(name,href)))'),
                    ('additional_types', 'additional_types_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/playlists/{playlist_id}'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playlist_cover(client):
    """Test case for get_playlist_cover

    Get Playlist Cover Image 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/playlists/{playlist_id}/images'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playlists_tracks(client):
    """Test case for get_playlists_tracks

    Get Playlist Items 
    """
    params = [('market', 'ES'),
                    ('fields', 'items(added_by.id,track(name,href,album(name,href)))'),
                    ('limit', 20),
                    ('offset', 0),
                    ('additional_types', 'additional_types_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/playlists/{playlist_id}/tracks'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_tracks_playlist(client):
    """Test case for remove_tracks_playlist

    Remove Playlist Items 
    """
    body = openapi_server.RemoveTracksPlaylistRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/playlists/{playlist_id}/tracks'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reorder_or_replace_playlists_tracks(client):
    """Test case for reorder_or_replace_playlists_tracks

    Update Playlist Items 
    """
    body = openapi_server.ReorderOrReplacePlaylistsTracksRequest()
    params = [('uris', 'uris_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/playlists/{playlist_id}/tracks'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfollow_playlist_0(client):
    """Test case for unfollow_playlist_0

    Unfollow Playlist 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/playlists/{playlist_id}/followers'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("image/jpeg not supported by Connexion")
async def test_upload_custom_playlist_cover(client):
    """Test case for upload_custom_playlist_cover

    Add Custom Playlist Cover Image 
    """
    body = 'body_example'
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'image/jpeg',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/playlists/{playlist_id}/images'.format(playlist_id='3cEYpjA9oz9GiPac4AsH4n'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

