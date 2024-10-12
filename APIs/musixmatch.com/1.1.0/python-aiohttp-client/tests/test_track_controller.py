# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album_tracks_get_get200_response import AlbumTracksGetGet200Response
from openapi_server.models.chart_tracks_get_get200_response import ChartTracksGetGet200Response
from openapi_server.models.matcher_track_get_get200_response import MatcherTrackGetGet200Response


pytestmark = pytest.mark.asyncio

async def test_album_tracks_get_get(client):
    """Test case for album_tracks_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('album_id', 'album_id_example'),
                    ('f_has_lyrics', 'f_has_lyrics_example'),
                    ('page', 3.4),
                    ('page_size', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/album.tracks.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_chart_tracks_get_get(client):
    """Test case for chart_tracks_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('page', 3.4),
                    ('page_size', 3.4),
                    ('country', 'us'),
                    ('f_has_lyrics', 'f_has_lyrics_example')]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/chart.tracks.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_matcher_track_get_get(client):
    """Test case for matcher_track_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('q_artist', 'q_artist_example'),
                    ('q_track', 'q_track_example'),
                    ('f_has_lyrics', 3.4),
                    ('f_has_subtitle', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/matcher.track.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_track_get_get(client):
    """Test case for track_get_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('track_id', 'track_id_example')]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/track.get',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_track_search_get(client):
    """Test case for track_search_get

    
    """
    params = [('format', 'json'),
                    ('callback', 'param_callback_example'),
                    ('q_track', 'q_track_example'),
                    ('q_artist', 'q_artist_example'),
                    ('q_lyrics', 'q_lyrics_example'),
                    ('f_artist_id', 3.4),
                    ('f_music_genre_id', 3.4),
                    ('f_lyrics_language', 3.4),
                    ('f_has_lyrics', 3.4),
                    ('s_artist_rating', 's_artist_rating_example'),
                    ('s_track_rating', 's_track_rating_example'),
                    ('quorum_factor', 1.0),
                    ('page_size', 3.4),
                    ('page', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/ws/1.1/track.search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

