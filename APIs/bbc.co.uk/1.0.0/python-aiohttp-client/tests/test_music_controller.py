# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.music_popularity_artists import MusicPopularityArtists
from openapi_server.models.music_popularity_error import MusicPopularityError
from openapi_server.models.music_popularity_playlists import MusicPopularityPlaylists
from openapi_server.models.music_popularity_tracks import MusicPopularityTracks
from openapi_server.models.personalised_music_batch_request import PersonalisedMusicBatchRequest
from openapi_server.models.personalised_music_error_response import PersonalisedMusicErrorResponse
from openapi_server.models.personalised_music_request import PersonalisedMusicRequest
from openapi_server.models.personalised_music_response import PersonalisedMusicResponse
from openapi_server.models.personalised_music_success import PersonalisedMusicSuccess


pytestmark = pytest.mark.asyncio

async def test_delete_personalised_music_favourites_by_type_by_id(client):
    """Test case for delete_personalised_music_favourites_by_type_by_id

    Favourite Track or Clip
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/music/favourites/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_personalised_music_follows_by_type_by_id(client):
    """Test case for delete_personalised_music_follows_by_type_by_id

    Followed Network, Category, Artist, Playlist and Genre
    """
    params = [('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='DELETE',
        path='/my/music/follows/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_popular_artist_by_id(client):
    """Test case for get_music_popular_artist_by_id

    Single Artist Popularity
    """
    params = [('since', 'since_example'),
                    ('until', 'until_example'),
                    ('decomposed', True)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/music/popular/artists/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_popular_artists(client):
    """Test case for get_music_popular_artists

    Popular Artists
    """
    params = [('since', 'since_example'),
                    ('until', 'until_example'),
                    ('decomposed', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/music/popular/artists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_popular_playlist_by_id(client):
    """Test case for get_music_popular_playlist_by_id

    Single Playlist Popularity
    """
    params = [('since', 'since_example'),
                    ('until', 'until_example'),
                    ('decomposed', True)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/music/popular/playlists/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_popular_playlists(client):
    """Test case for get_music_popular_playlists

    Popular Playlists
    """
    params = [('since', 'since_example'),
                    ('until', 'until_example'),
                    ('decomposed', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/music/popular/playlists',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_popular_track_by_id(client):
    """Test case for get_music_popular_track_by_id

    Single Track Popularity
    """
    params = [('since', 'since_example'),
                    ('until', 'until_example'),
                    ('network', 'network_example'),
                    ('programme', 'programme_example'),
                    ('artist', 'artist_example'),
                    ('decomposed', True)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/music/popular/tracks/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_music_popular_tracks(client):
    """Test case for get_music_popular_tracks

    Popular Tracks
    """
    params = [('since', 'since_example'),
                    ('until', 'until_example'),
                    ('network', 'network_example'),
                    ('programme', 'programme_example'),
                    ('artist', 'artist_example'),
                    ('decomposed', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/music/popular/tracks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_music_favourites(client):
    """Test case for get_personalised_music_favourites

    Favourite Tracks or Clips
    """
    params = [('offset', 56),
                    ('limit', 56),
                    ('action', 'action_example'),
                    ('music-data', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/favourites',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_music_favourites_by_type(client):
    """Test case for get_personalised_music_favourites_by_type

    Favourite Tracks or Clips by Type
    """
    params = [('action', 'action_example'),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/favourites/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_music_favourites_by_type_by_id(client):
    """Test case for get_personalised_music_favourites_by_type_by_id

    Favourite Track or Clip
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/favourites/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_music_follows(client):
    """Test case for get_personalised_music_follows

    Followed Networks, Categories, Artists, Playlists and Genres
    """
    params = [('action', 'action_example'),
                    ('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/follows',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_music_follows_by_type(client):
    """Test case for get_personalised_music_follows_by_type

    Followed Networks, Categories, Artists, Playlists and Genres by Type
    """
    params = [('action', 'action_example'),
                    ('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True),
                    ('offset', 56),
                    ('limit', 56)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/follows/{type}'.format(type='type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_personalised_music_follows_by_type_by_id(client):
    """Test case for get_personalised_music_follows_by_type_by_id

    Followed Network, Category, Artist, Playlist and Genre
    """
    params = [('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True)]
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='GET',
        path='/my/music/follows/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_music_favourites_batch(client):
    """Test case for post_personalised_music_favourites_batch

    Favourite Tracks or Clips
    """
    body = {"added_at":"added_at","domain":"domain","context":"context","meta_data":{"key":"key"},"action":"action","id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/favourites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_music_favourites_by_type_by_id(client):
    """Test case for post_personalised_music_favourites_by_type_by_id

    Favourite Track or Clip
    """
    body = {"added_at":"added_at","context":"context","meta_data":{"key":"key"},"action":"action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/favourites/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_music_follows_batch(client):
    """Test case for post_personalised_music_follows_batch

    Followed Networks, Categories, Artists, Playlists and Genres
    """
    body = {"added_at":"added_at","domain":"domain","context":"context","meta_data":{"key":"key"},"action":"action","id":"id","type":"type"}
    params = [('action', 'action_example'),
                    ('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/follows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_personalised_music_follows_by_type_by_id(client):
    """Test case for post_personalised_music_follows_by_type_by_id

    Followed Network, Category, Artist, Playlist and Genre
    """
    body = {"added_at":"added_at","context":"context","meta_data":{"key":"key"},"action":"action"}
    params = [('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='POST',
        path='/my/music/follows/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_music_favourites_batch(client):
    """Test case for put_personalised_music_favourites_batch

    Favourite Tracks or Clips
    """
    body = {"added_at":"added_at","domain":"domain","context":"context","meta_data":{"key":"key"},"action":"action","id":"id","type":"type"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/music/favourites',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_music_favourites_by_type_by_id(client):
    """Test case for put_personalised_music_favourites_by_type_by_id

    Favourite Track or Clip
    """
    body = {"added_at":"added_at","context":"context","meta_data":{"key":"key"},"action":"action"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/music/favourites/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_music_follows_batch(client):
    """Test case for put_personalised_music_follows_batch

    Followed Networks, Categories, Artists, Playlists and Genres
    """
    body = {"added_at":"added_at","domain":"domain","context":"context","meta_data":{"key":"key"},"action":"action","id":"id","type":"type"}
    params = [('action', 'action_example'),
                    ('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/music/follows',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_personalised_music_follows_by_type_by_id(client):
    """Test case for put_personalised_music_follows_by_type_by_id

    Followed Network, Category, Artist, Playlist and Genre
    """
    body = {"added_at":"added_at","context":"context","meta_data":{"key":"key"},"action":"action"}
    params = [('music-data', True),
                    ('music_context', 'music_context_example'),
                    ('music_within_uk', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Bearer OAUTH_TOKEN',
        'x_authentication_provider': 'idv5',
        'x_api_key': 'x_api_key_example',
    }
    response = await client.request(
        method='PUT',
        path='/my/music/follows/{type}/{id}'.format(type='type_example', id='id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

