from typing import List, Dict
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_hls_audio_segment_legacy_aac(request: web.Request, item_id, segment_id) -> web.Response:
    """Gets the specified audio segment for an audio item.

    

    :param item_id: The item id.
    :type item_id: str
    :param segment_id: The segment id.
    :type segment_id: str

    """
    return web.Response(status=200)


async def get_hls_audio_segment_legacy_mp3(request: web.Request, item_id, segment_id) -> web.Response:
    """Gets the specified audio segment for an audio item.

    

    :param item_id: The item id.
    :type item_id: str
    :param segment_id: The segment id.
    :type segment_id: str

    """
    return web.Response(status=200)


async def get_hls_playlist_legacy(request: web.Request, item_id, playlist_id) -> web.Response:
    """Gets a hls video playlist.

    

    :param item_id: The video id.
    :type item_id: str
    :param playlist_id: The playlist id.
    :type playlist_id: str

    """
    return web.Response(status=200)


async def get_hls_video_segment_legacy(request: web.Request, item_id, playlist_id, segment_id, segment_container) -> web.Response:
    """Gets a hls video segment.

    

    :param item_id: The item id.
    :type item_id: str
    :param playlist_id: The playlist id.
    :type playlist_id: str
    :param segment_id: The segment id.
    :type segment_id: str
    :param segment_container: The segment container.
    :type segment_container: str

    """
    return web.Response(status=200)


async def stop_encoding_process(request: web.Request, device_id=None, play_session_id=None) -> web.Response:
    """Stops an active encoding.

    

    :param device_id: The device id of the client requesting. Used to stop encoding processes when needed.
    :type device_id: str
    :param play_session_id: The play session id.
    :type play_session_id: str

    """
    return web.Response(status=200)
