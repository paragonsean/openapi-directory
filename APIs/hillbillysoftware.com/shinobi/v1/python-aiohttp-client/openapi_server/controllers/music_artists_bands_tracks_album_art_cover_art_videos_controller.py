from typing import List, Dict
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
from openapi_server import util


async def musi_videos_get(request: web.Request, access_token, artist_id) -> web.Response:
    """Lists all videos available for this Artist / Band

    

    :param access_token: 
    :type access_token: str
    :param artist_id: 
    :type artist_id: str

    """
    return web.Response(status=200)


async def music_album_art_get(request: web.Request, access_token, album_id) -> web.Response:
    """Returns Albumart for passed AlbumID

    

    :param access_token: 
    :type access_token: str
    :param album_id: 
    :type album_id: str

    """
    return web.Response(status=200)


async def music_albums_get(request: web.Request, access_token, artist_id) -> web.Response:
    """Get albums from passed ArtistID

    

    :param access_token: 
    :type access_token: str
    :param artist_id: ID of artist or band to retrieve albums from
    :type artist_id: str

    """
    return web.Response(status=200)


async def music_artist_extended_get(request: web.Request, access_token, name) -> web.Response:
    """Provides extended information, which includes all known albums and music videos of artist / band

    

    :param access_token: 
    :type access_token: str
    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def music_by_music_brainz_get(request: web.Request, access_token, mbid) -> web.Response:
    """Get Artist / Band information on MusicBrainzID

    

    :param access_token: 
    :type access_token: str
    :param mbid: MusicBrainzID
    :type mbid: str

    """
    return web.Response(status=200)


async def music_cd_covers_get(request: web.Request, access_token, mbid) -> web.Response:
    """Gets CD art for passed MusicBrainzID

    

    :param access_token: 
    :type access_token: str
    :param mbid: MusicBrainzID
    :type mbid: str

    """
    return web.Response(status=200)


async def music_cover_art_by_name_get(request: web.Request, access_token, name) -> web.Response:
    """Retrieves artist / band Banner and logo based on artist or bandname

    

    :param access_token: 
    :type access_token: str
    :param name: Name of artist or band
    :type name: str

    """
    return web.Response(status=200)


async def music_cover_art_get(request: web.Request, access_token, artist_id) -> web.Response:
    """Retrieves artist / band Banner and logo based on ArtistID

    

    :param access_token: 
    :type access_token: str
    :param artist_id: ArtistID of artist or band
    :type artist_id: str

    """
    return web.Response(status=200)


async def music_get(request: web.Request, access_token, name) -> web.Response:
    """Get information about passed band name or artist

    

    :param access_token: 
    :type access_token: str
    :param name: Name (or part) of band or artist name
    :type name: str

    """
    return web.Response(status=200)


async def music_lyrics_by_song_get(request: web.Request, access_token, song) -> web.Response:
    """Get lyrics on song title

    

    :param access_token: 
    :type access_token: str
    :param song: Name or part of song name
    :type song: str

    """
    return web.Response(status=200)


async def music_lyrics_get(request: web.Request, access_token, name) -> web.Response:
    """Get lyrics for band or artist (record set limited to 25)

    

    :param access_token: 
    :type access_token: str
    :param name: Name (or partial) of band or artist (record set limited to 25)
    :type name: str

    """
    return web.Response(status=200)


async def music_lyricsby_album_id_get(request: web.Request, access_token, album_id) -> web.Response:
    """Returns all lyrics for requested AlbumID

    

    :param access_token: 
    :type access_token: str
    :param album_id: 
    :type album_id: str

    """
    return web.Response(status=200)


async def music_tracks_get(request: web.Request, access_token, album_id) -> web.Response:
    """Get all tracks from requested album

    

    :param access_token: 
    :type access_token: str
    :param album_id: AlbumID (can be retrieved via album endpoint)
    :type album_id: str

    """
    return web.Response(status=200)
