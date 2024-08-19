# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.follow_artists_users_request import FollowArtistsUsersRequest
from openapi_server.models.follow_playlist_request import FollowPlaylistRequest
from openapi_server.models.get_followed200_response import GetFollowed200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.paging_artist_object import PagingArtistObject
from openapi_server.models.paging_playlist_object import PagingPlaylistObject
from openapi_server.models.paging_track_object import PagingTrackObject
from openapi_server.models.private_user_object import PrivateUserObject
from openapi_server.models.public_user_object import PublicUserObject
from openapi_server.models.unfollow_artists_users_request import UnfollowArtistsUsersRequest


pytestmark = pytest.mark.asyncio

async def test_check_current_user_follows(client):
    """Test case for check_current_user_follows

    Check If User Follows Artists or Users 
    """
    params = [('type', 'artist'),
                    ('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/following/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_if_user_follows_playlist(client):
    """Test case for check_if_user_follows_playlist

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

async def test_follow_artists_users(client):
    """Test case for follow_artists_users

    Follow Artists or Users 
    """
    body = openapi_server.FollowArtistsUsersRequest()
    params = [('type', 'artist'),
                    ('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/following',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_follow_playlist(client):
    """Test case for follow_playlist

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

async def test_get_current_users_profile(client):
    """Test case for get_current_users_profile

    Get Current User's Profile 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_followed(client):
    """Test case for get_followed

    Get Followed Artists 
    """
    params = [('type', 'artist'),
                    ('after', '0I2XqVXqHScXjHhk6AYYRe'),
                    ('limit', 20)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/following',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_list_users_playlists_0(client):
    """Test case for get_list_users_playlists_0

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

async def test_get_users_profile(client):
    """Test case for get_users_profile

    Get User's Profile 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/users/{user_id}'.format(user_id='smedjan'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_top_artists(client):
    """Test case for get_users_top_artists

    Get User's Top Artists 
    """
    params = [('time_range', 'medium_term'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/top/artists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_top_tracks(client):
    """Test case for get_users_top_tracks

    Get User's Top Tracks 
    """
    params = [('time_range', 'medium_term'),
                    ('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/top/tracks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfollow_artists_users(client):
    """Test case for unfollow_artists_users

    Unfollow Artists or Users 
    """
    body = openapi_server.UnfollowArtistsUsersRequest()
    params = [('type', 'artist'),
                    ('ids', '2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/following',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfollow_playlist(client):
    """Test case for unfollow_playlist

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

