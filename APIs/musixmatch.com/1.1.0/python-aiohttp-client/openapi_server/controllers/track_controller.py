from typing import List, Dict
from aiohttp import web

from openapi_server.models.album_tracks_get_get200_response import AlbumTracksGetGet200Response
from openapi_server.models.chart_tracks_get_get200_response import ChartTracksGetGet200Response
from openapi_server.models.matcher_track_get_get200_response import MatcherTrackGetGet200Response
from openapi_server import util


async def album_tracks_get_get(request: web.Request, album_id, format=None, param_callback=None, f_has_lyrics=None, page=None, page_size=None) -> web.Response:
    """album_tracks_get_get

    

    :param album_id: The musiXmatch album id
    :type album_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param f_has_lyrics: When set, filter only contents with lyrics
    :type f_has_lyrics: str
    :param page: Define the page number for paginated results
    :type page: 
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 

    """
    return web.Response(status=200)


async def chart_tracks_get_get(request: web.Request, format=None, param_callback=None, page=None, page_size=None, country=None, f_has_lyrics=None) -> web.Response:
    """chart_tracks_get_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param page: Define the page number for paginated results
    :type page: 
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 
    :param country: A valid ISO 3166 country code
    :type country: str
    :param f_has_lyrics: When set, filter only contents with lyrics
    :type f_has_lyrics: str

    """
    return web.Response(status=200)


async def matcher_track_get_get(request: web.Request, format=None, param_callback=None, q_artist=None, q_track=None, f_has_lyrics=None, f_has_subtitle=None) -> web.Response:
    """matcher_track_get_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param q_artist: The song artist
    :type q_artist: str
    :param q_track: The song title
    :type q_track: str
    :param f_has_lyrics: When set, filter only contents with lyrics
    :type f_has_lyrics: 
    :param f_has_subtitle: When set, filter only contents with subtitles
    :type f_has_subtitle: 

    """
    return web.Response(status=200)


async def track_get_get(request: web.Request, track_id, format=None, param_callback=None) -> web.Response:
    """track_get_get

    

    :param track_id: The musiXmatch track id
    :type track_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str

    """
    return web.Response(status=200)


async def track_search_get(request: web.Request, format=None, param_callback=None, q_track=None, q_artist=None, q_lyrics=None, f_artist_id=None, f_music_genre_id=None, f_lyrics_language=None, f_has_lyrics=None, s_artist_rating=None, s_track_rating=None, quorum_factor=None, page_size=None, page=None) -> web.Response:
    """track_search_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param q_track: The song title
    :type q_track: str
    :param q_artist: The song artist
    :type q_artist: str
    :param q_lyrics: Any word in the lyrics
    :type q_lyrics: str
    :param f_artist_id: When set, filter by this artist id
    :type f_artist_id: 
    :param f_music_genre_id: When set, filter by this music category id
    :type f_music_genre_id: 
    :param f_lyrics_language: Filter by the lyrics language (en,it,..)
    :type f_lyrics_language: 
    :param f_has_lyrics: When set, filter only contents with lyrics
    :type f_has_lyrics: 
    :param s_artist_rating: Sort by our popularity index for artists (asc|desc)
    :type s_artist_rating: str
    :param s_track_rating: Sort by our popularity index for tracks (asc|desc)
    :type s_track_rating: str
    :param quorum_factor: Search only a part of the given query string.Allowed range is (0.1 – 0.9)
    :type quorum_factor: 
    :param page_size: Define the page size for paginated results.Range is 1 to 100.
    :type page_size: 
    :param page: Define the page number for paginated results
    :type page: 

    """
    return web.Response(status=200)
