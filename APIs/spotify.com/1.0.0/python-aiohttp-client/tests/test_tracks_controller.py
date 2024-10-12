# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_tracks_to_playlist_request import AddTracksToPlaylistRequest
from openapi_server.models.audio_analysis_object import AudioAnalysisObject
from openapi_server.models.audio_features_object import AudioFeaturesObject
from openapi_server.models.get_an_artists_top_tracks200_response import GetAnArtistsTopTracks200Response
from openapi_server.models.get_multiple_albums401_response import GetMultipleAlbums401Response
from openapi_server.models.get_several_audio_features200_response import GetSeveralAudioFeatures200Response
from openapi_server.models.get_users_top_artists_and_tracks200_response import GetUsersTopArtistsAndTracks200Response
from openapi_server.models.paging_playlist_track_object import PagingPlaylistTrackObject
from openapi_server.models.paging_saved_track_object import PagingSavedTrackObject
from openapi_server.models.paging_simplified_track_object import PagingSimplifiedTrackObject
from openapi_server.models.recommendations_object import RecommendationsObject
from openapi_server.models.remove_tracks_playlist_request import RemoveTracksPlaylistRequest
from openapi_server.models.reorder_or_replace_playlists_tracks200_response import ReorderOrReplacePlaylistsTracks200Response
from openapi_server.models.reorder_or_replace_playlists_tracks_request import ReorderOrReplacePlaylistsTracksRequest
from openapi_server.models.save_albums_user_request import SaveAlbumsUserRequest
from openapi_server.models.save_tracks_user_request import SaveTracksUserRequest
from openapi_server.models.track_object import TrackObject


pytestmark = pytest.mark.asyncio

async def test_add_tracks_to_playlist_0(client):
    """Test case for add_tracks_to_playlist_0

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

async def test_check_users_saved_tracks(client):
    """Test case for check_users_saved_tracks

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

async def test_get_an_albums_tracks_0(client):
    """Test case for get_an_albums_tracks_0

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

async def test_get_an_artists_top_tracks_0(client):
    """Test case for get_an_artists_top_tracks_0

    Get Artist's Top Tracks 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/artists/{id}/top-tracks'.format(id='0TnOYISbd1XYRBk9myaseg'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audio_analysis(client):
    """Test case for get_audio_analysis

    Get Track's Audio Analysis 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audio-analysis/{id}'.format(id='11dFghVXANMlKmJXsNCbNl'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_audio_features(client):
    """Test case for get_audio_features

    Get Track's Audio Features 
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audio-features/{id}'.format(id='11dFghVXANMlKmJXsNCbNl'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_playlists_tracks_0(client):
    """Test case for get_playlists_tracks_0

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

async def test_get_recommendations(client):
    """Test case for get_recommendations

    Get Recommendations 
    """
    params = [('limit', 20),
                    ('market', 'ES'),
                    ('seed_artists', '4NHQUGzhtTLFvgF5SZesLK'),
                    ('seed_genres', 'classical,country'),
                    ('seed_tracks', '0c6xIDDpzE81m2q797ordA'),
                    ('min_acousticness', 3.4),
                    ('max_acousticness', 3.4),
                    ('target_acousticness', 3.4),
                    ('min_danceability', 3.4),
                    ('max_danceability', 3.4),
                    ('target_danceability', 3.4),
                    ('min_duration_ms', 56),
                    ('max_duration_ms', 56),
                    ('target_duration_ms', 56),
                    ('min_energy', 3.4),
                    ('max_energy', 3.4),
                    ('target_energy', 3.4),
                    ('min_instrumentalness', 3.4),
                    ('max_instrumentalness', 3.4),
                    ('target_instrumentalness', 3.4),
                    ('min_key', 56),
                    ('max_key', 56),
                    ('target_key', 56),
                    ('min_liveness', 3.4),
                    ('max_liveness', 3.4),
                    ('target_liveness', 3.4),
                    ('min_loudness', 3.4),
                    ('max_loudness', 3.4),
                    ('target_loudness', 3.4),
                    ('min_mode', 56),
                    ('max_mode', 56),
                    ('target_mode', 56),
                    ('min_popularity', 56),
                    ('max_popularity', 56),
                    ('target_popularity', 56),
                    ('min_speechiness', 3.4),
                    ('max_speechiness', 3.4),
                    ('target_speechiness', 3.4),
                    ('min_tempo', 3.4),
                    ('max_tempo', 3.4),
                    ('target_tempo', 3.4),
                    ('min_time_signature', 56),
                    ('max_time_signature', 56),
                    ('target_time_signature', 56),
                    ('min_valence', 3.4),
                    ('max_valence', 3.4),
                    ('target_valence', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/recommendations',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_several_audio_features(client):
    """Test case for get_several_audio_features

    Get Tracks' Audio Features 
    """
    params = [('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/audio-features',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_several_tracks(client):
    """Test case for get_several_tracks

    Get Several Tracks 
    """
    params = [('market', 'ES'),
                    ('ids', '7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tracks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_track(client):
    """Test case for get_track

    Get Track 
    """
    params = [('market', 'ES')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/tracks/{id}'.format(id='11dFghVXANMlKmJXsNCbNl'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_users_saved_tracks(client):
    """Test case for get_users_saved_tracks

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

async def test_get_users_top_artists_and_tracks_0(client):
    """Test case for get_users_top_artists_and_tracks_0

    Get User's Top Items 
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
        path='/v1/me/top/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_tracks_playlist_0(client):
    """Test case for remove_tracks_playlist_0

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

async def test_remove_tracks_user(client):
    """Test case for remove_tracks_user

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

async def test_reorder_or_replace_playlists_tracks_0(client):
    """Test case for reorder_or_replace_playlists_tracks_0

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

async def test_save_tracks_user(client):
    """Test case for save_tracks_user

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

