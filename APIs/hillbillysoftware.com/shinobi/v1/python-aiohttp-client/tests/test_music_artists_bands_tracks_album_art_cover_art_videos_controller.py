# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.album_art import AlbumArt
from openapi_server.models.album_tracks import AlbumTracks
from openapi_server.models.artist_art import ArtistArt
from openapi_server.models.band_albums import BandAlbums
from openapi_server.models.band_info import BandInfo
from openapi_server.models.band_info_extended import BandInfoExtended
from openapi_server.models.cd_cover_art import CDCoverArt
from openapi_server.models.lyric import Lyric
from openapi_server.models.music_video import MusicVideo


pytestmark = pytest.mark.asyncio

async def test_musi_videos_get(client):
    """Test case for musi_videos_get

    Lists all videos available for this Artist / Band
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Videos/{access_token}/{artist_id}'.format(access_token='access_token_example', artist_id='artist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_album_art_get(client):
    """Test case for music_album_art_get

    Returns Albumart for passed AlbumID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Albums/Art/{access_token}/{album_id}'.format(access_token='access_token_example', album_id='album_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_albums_get(client):
    """Test case for music_albums_get

    Get albums from passed ArtistID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Albums/{access_token}/{artist_id}'.format(access_token='access_token_example', artist_id='artist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_artist_extended_get(client):
    """Test case for music_artist_extended_get

    Provides extended information, which includes all known albums and music videos of artist / band
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Artist/Extended/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_by_music_brainz_get(client):
    """Test case for music_by_music_brainz_get

    Get Artist / Band information on MusicBrainzID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Albums/MusicBrainzID/{access_token}/{mbid}'.format(access_token='access_token_example', mbid='mbid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_cd_covers_get(client):
    """Test case for music_cd_covers_get

    Gets CD art for passed MusicBrainzID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Albums/CoverArt/{access_token}/{mbid}'.format(access_token='access_token_example', mbid='mbid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_cover_art_by_name_get(client):
    """Test case for music_cover_art_by_name_get

    Retrieves artist / band Banner and logo based on artist or bandname
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Artist/Art/Name/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_cover_art_get(client):
    """Test case for music_cover_art_get

    Retrieves artist / band Banner and logo based on ArtistID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Artist/Art/ID/{access_token}/{artist_id}'.format(access_token='access_token_example', artist_id='artist_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_get(client):
    """Test case for music_get

    Get information about passed band name or artist
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Artist/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_lyrics_by_song_get(client):
    """Test case for music_lyrics_by_song_get

    Get lyrics on song title
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Lyrics/BySong/{access_token}/{song}'.format(access_token='access_token_example', song='song_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_lyrics_get(client):
    """Test case for music_lyrics_get

    Get lyrics for band or artist (record set limited to 25)
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Lyrics/ByName/{access_token}/{name}'.format(access_token='access_token_example', name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_lyricsby_album_id_get(client):
    """Test case for music_lyricsby_album_id_get

    Returns all lyrics for requested AlbumID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Lyrics/AlbumID/{access_token}/{album_id}'.format(access_token='access_token_example', album_id='album_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_music_tracks_get(client):
    """Test case for music_tracks_get

    Get all tracks from requested album
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/Music/Tracks/{access_token}/{album_id}'.format(access_token='access_token_example', album_id='album_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

