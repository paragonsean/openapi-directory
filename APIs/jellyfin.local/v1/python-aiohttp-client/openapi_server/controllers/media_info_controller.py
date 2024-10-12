from typing import List, Dict
from aiohttp import web

from openapi_server.models.live_stream_response import LiveStreamResponse
from openapi_server.models.open_live_stream_dto import OpenLiveStreamDto
from openapi_server.models.playback_info_dto import PlaybackInfoDto
from openapi_server.models.playback_info_response import PlaybackInfoResponse
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def close_live_stream(request: web.Request, live_stream_id) -> web.Response:
    """Closes a media source.

    

    :param live_stream_id: The livestream id.
    :type live_stream_id: str

    """
    return web.Response(status=200)


async def get_bitrate_test_bytes(request: web.Request, size=None) -> web.Response:
    """Tests the network with a request with the size of the bitrate.

    

    :param size: The bitrate. Defaults to 102400.
    :type size: int

    """
    return web.Response(status=200)


async def get_playback_info(request: web.Request, item_id, user_id) -> web.Response:
    """Gets live playback media info for an item.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param user_id: The user id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_posted_playback_info(request: web.Request, item_id, user_id=None, max_streaming_bitrate=None, start_time_ticks=None, audio_stream_index=None, subtitle_stream_index=None, max_audio_channels=None, media_source_id=None, live_stream_id=None, auto_open_live_stream=None, enable_direct_play=None, enable_direct_stream=None, enable_transcoding=None, allow_video_stream_copy=None, allow_audio_stream_copy=None, body=None) -> web.Response:
    """Gets live playback media info for an item.

    For backwards compatibility parameters can be sent via Query or Body, with Query having higher precedence.

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param max_streaming_bitrate: The maximum streaming bitrate.
    :type max_streaming_bitrate: int
    :param start_time_ticks: The start time in ticks.
    :type start_time_ticks: int
    :param audio_stream_index: The audio stream index.
    :type audio_stream_index: int
    :param subtitle_stream_index: The subtitle stream index.
    :type subtitle_stream_index: int
    :param max_audio_channels: The maximum number of audio channels.
    :type max_audio_channels: int
    :param media_source_id: The media source id.
    :type media_source_id: str
    :param live_stream_id: The livestream id.
    :type live_stream_id: str
    :param auto_open_live_stream: Whether to auto open the livestream.
    :type auto_open_live_stream: bool
    :param enable_direct_play: Whether to enable direct play. Default: true.
    :type enable_direct_play: bool
    :param enable_direct_stream: Whether to enable direct stream. Default: true.
    :type enable_direct_stream: bool
    :param enable_transcoding: Whether to enable transcoding. Default: true.
    :type enable_transcoding: bool
    :param allow_video_stream_copy: Whether to allow to copy the video stream. Default: true.
    :type allow_video_stream_copy: bool
    :param allow_audio_stream_copy: Whether to allow to copy the audio stream. Default: true.
    :type allow_audio_stream_copy: bool
    :param body: The playback info.
    :type body: dict | bytes

    """
    body = PlaybackInfoDto.from_dict(body)
    return web.Response(status=200)


async def open_live_stream(request: web.Request, open_token=None, user_id=None, play_session_id=None, max_streaming_bitrate=None, start_time_ticks=None, audio_stream_index=None, subtitle_stream_index=None, max_audio_channels=None, item_id=None, enable_direct_play=None, enable_direct_stream=None, body=None) -> web.Response:
    """Opens a media source.

    

    :param open_token: The open token.
    :type open_token: str
    :param user_id: The user id.
    :type user_id: str
    :type user_id: str
    :param play_session_id: The play session id.
    :type play_session_id: str
    :param max_streaming_bitrate: The maximum streaming bitrate.
    :type max_streaming_bitrate: int
    :param start_time_ticks: The start time in ticks.
    :type start_time_ticks: int
    :param audio_stream_index: The audio stream index.
    :type audio_stream_index: int
    :param subtitle_stream_index: The subtitle stream index.
    :type subtitle_stream_index: int
    :param max_audio_channels: The maximum number of audio channels.
    :type max_audio_channels: int
    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param enable_direct_play: Whether to enable direct play. Default: true.
    :type enable_direct_play: bool
    :param enable_direct_stream: Whether to enable direct stream. Default: true.
    :type enable_direct_stream: bool
    :param body: The open live stream dto.
    :type body: dict | bytes

    """
    body = OpenLiveStreamDto.from_dict(body)
    return web.Response(status=200)
