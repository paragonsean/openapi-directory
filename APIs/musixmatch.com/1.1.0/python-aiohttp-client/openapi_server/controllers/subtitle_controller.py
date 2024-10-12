from typing import List, Dict
from aiohttp import web

from openapi_server.models.matcher_subtitle_get_get200_response import MatcherSubtitleGetGet200Response
from openapi_server import util


async def matcher_subtitle_get_get(request: web.Request, format=None, param_callback=None, q_track=None, q_artist=None, f_subtitle_length=None, f_subtitle_length_max_deviation=None) -> web.Response:
    """matcher_subtitle_get_get

    

    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str
    :param q_track: The song title
    :type q_track: str
    :param q_artist:  The song artist
    :type q_artist: str
    :param f_subtitle_length: Filter by subtitle length in seconds
    :type f_subtitle_length: 
    :param f_subtitle_length_max_deviation: Max deviation for a subtitle length in seconds
    :type f_subtitle_length_max_deviation: 

    """
    return web.Response(status=200)


async def track_subtitle_get_get(request: web.Request, track_id, format=None, param_callback=None) -> web.Response:
    """track_subtitle_get_get

    

    :param track_id: The musiXmatch track id
    :type track_id: str
    :param format: output format: json, jsonp, xml.
    :type format: str
    :param param_callback: jsonp callback
    :type param_callback: str

    """
    return web.Response(status=200)
