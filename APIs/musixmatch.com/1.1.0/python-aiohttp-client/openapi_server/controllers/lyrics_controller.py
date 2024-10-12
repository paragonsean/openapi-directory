from typing import List, Dict
from aiohttp import web

from openapi_server.models.matcher_lyrics_get_get200_response import MatcherLyricsGetGet200Response
from openapi_server import util


async def matcher_lyrics_get_get(request: web.Request, format=None, param_callback=None, q_track=None, q_artist=None) -> web.Response:
    """matcher_lyrics_get_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param q_track: The song title
    :type q_track: str
    :param q_artist: The song artist
    :type q_artist: str

    """
    return web.Response(status=200)


async def track_lyrics_get_get(request: web.Request, track_id, format=None, param_callback=None) -> web.Response:
    """track_lyrics_get_get

    

    :param track_id: The musiXmatch track id
    :type track_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str

    """
    return web.Response(status=200)
