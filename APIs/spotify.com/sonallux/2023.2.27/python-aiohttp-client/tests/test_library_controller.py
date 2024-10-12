# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.change_playlist_details_request import ChangePlaylistDetailsRequest
from openapi_server.models.create_playlist_request import CreatePlaylistRequest
from openapi_server.models.follow_artists_users_request import FollowArtistsUsersRequest
from openapi_server.models.get_followed200_response import GetFollowed200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.paging_artist_object import PagingArtistObject
from openapi_server.models.paging_playlist_object import PagingPlaylistObject
from openapi_server.models.paging_saved_album_object import PagingSavedAlbumObject
from openapi_server.models.paging_saved_audiobook_object import PagingSavedAudiobookObject
from openapi_server.models.paging_saved_episode_object import PagingSavedEpisodeObject
from openapi_server.models.paging_saved_show_object import PagingSavedShowObject
from openapi_server.models.paging_saved_track_object import PagingSavedTrackObject
from openapi_server.models.paging_track_object import PagingTrackObject
from openapi_server.models.playlist_object import PlaylistObject
from openapi_server.models.remove_episodes_user_request import RemoveEpisodesUserRequest
from openapi_server.models.save_albums_user_request import SaveAlbumsUserRequest
from openapi_server.models.save_episodes_user_request import SaveEpisodesUserRequest
from openapi_server.models.save_shows_user_request import SaveShowsUserRequest
from openapi_server.models.save_tracks_user_request import SaveTracksUserRequest
from openapi_server.models.unfollow_artists_users_request import UnfollowArtistsUsersRequest


pytestmark = pytest.mark.asyncio

async def test_change_playlist_details_0(client):
    """Test case for change_playlist_details_0

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

async def test_check_current_user_follows_1(client):
    """Test case for check_current_user_follows_1

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

async def test_check_users_saved_albums_0(client):
    """Test case for check_users_saved_albums_0

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

async def test_check_users_saved_audiobooks_0(client):
    """Test case for check_users_saved_audiobooks_0

    Check User's Saved Audiobooks 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/audiobooks/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_episodes_0(client):
    """Test case for check_users_saved_episodes_0

    Check User's Saved Episodes 
    """
    params = [('ids', '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/episodes/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_shows_0(client):
    """Test case for check_users_saved_shows_0

    Check User's Saved Shows 
    """
    params = [('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/shows/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_check_users_saved_tracks_0(client):
    """Test case for check_users_saved_tracks_0

    Check User's Saved Tracks 
    """
    params = [('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/tracks/contains',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_playlist_0(client):
    """Test case for create_playlist_0

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

async def test_follow_artists_users_1(client):
    """Test case for follow_artists_users_1

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

async def test_get_a_list_of_current_users_playlists_0(client):
    """Test case for get_a_list_of_current_users_playlists_0

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

async def test_get_followed_0(client):
    """Test case for get_followed_0

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

async def test_get_users_saved_albums_0(client):
    """Test case for get_users_saved_albums_0

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

async def test_get_users_saved_audiobooks_0(client):
    """Test case for get_users_saved_audiobooks_0

    Get User's Saved Audiobooks 
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_episodes_0(client):
    """Test case for get_users_saved_episodes_0

    Get User's Saved Episodes 
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
        path='/v1/me/episodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_shows_0(client):
    """Test case for get_users_saved_shows_0

    Get User's Saved Shows 
    """
    params = [('limit', 20),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/me/shows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_tracks_0(client):
    """Test case for get_users_saved_tracks_0

    Get User's Saved Tracks 
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
        path='/v1/me/tracks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_top_artists_1(client):
    """Test case for get_users_top_artists_1

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

async def test_get_users_top_tracks_1(client):
    """Test case for get_users_top_tracks_1

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

async def test_remove_albums_user_0(client):
    """Test case for remove_albums_user_0

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

async def test_remove_audiobooks_user_0(client):
    """Test case for remove_audiobooks_user_0

    Remove User's Saved Audiobooks 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_episodes_user_0(client):
    """Test case for remove_episodes_user_0

    Remove User's Saved Episodes 
    """
    body = openapi_server.RemoveEpisodesUserRequest()
    params = [('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/episodes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_shows_user_0(client):
    """Test case for remove_shows_user_0

    Remove User's Saved Shows 
    """
    body = openapi_server.SaveShowsUserRequest()
    params = [('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ'),
                    ('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/shows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_tracks_user_0(client):
    """Test case for remove_tracks_user_0

    Remove User's Saved Tracks 
    """
    body = openapi_server.SaveAlbumsUserRequest()
    params = [('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/me/tracks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_albums_user_0(client):
    """Test case for save_albums_user_0

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


pytestmark = pytest.mark.asyncio

async def test_save_audiobooks_user_0(client):
    """Test case for save_audiobooks_user_0

    Save Audiobooks for Current User 
    """
    params = [('ids', '18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/audiobooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_episodes_user_0(client):
    """Test case for save_episodes_user_0

    Save Episodes for Current User 
    """
    body = openapi_server.SaveEpisodesUserRequest()
    params = [('ids', '77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/episodes',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_shows_user_0(client):
    """Test case for save_shows_user_0

    Save Shows for Current User 
    """
    body = openapi_server.SaveShowsUserRequest()
    params = [('ids', '5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/shows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_save_tracks_user_0(client):
    """Test case for save_tracks_user_0

    Save Tracks for Current User 
    """
    body = openapi_server.SaveTracksUserRequest()
    params = [('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/me/tracks',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unfollow_artists_users_1(client):
    """Test case for unfollow_artists_users_1

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

