from typing import List, Dict
from aiohttp import web

from openapi_server.models.play_method import PlayMethod
from openapi_server.models.playback_progress_info import PlaybackProgressInfo
from openapi_server.models.playback_start_info import PlaybackStartInfo
from openapi_server.models.playback_stop_info import PlaybackStopInfo
from openapi_server.models.repeat_mode import RepeatMode
from openapi_server.models.user_item_data_dto import UserItemDataDto
from openapi_server import util


async def mark_played_item(request: web.Request, user_id, item_id, date_played=None) -> web.Response:
    """Marks an item as played for user.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param date_played: Optional. The date the item was played.
    :type date_played: str

    """
    date_played = util.deserialize_datetime(date_played)
    return web.Response(status=200)


async def mark_unplayed_item(request: web.Request, user_id, item_id) -> web.Response:
    """Marks an item as unplayed for user.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str

    """
    return web.Response(status=200)


async def on_playback_progress(request: web.Request, user_id, item_id, media_source_id=None, position_ticks=None, audio_stream_index=None, subtitle_stream_index=None, volume_level=None, play_method=None, live_stream_id=None, play_session_id=None, repeat_mode=None, is_paused=None, is_muted=None) -> web.Response:
    """Reports a user&#39;s playback progress.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param media_source_id: The id of the MediaSource.
    :type media_source_id: str
    :param position_ticks: Optional. The current position, in ticks. 1 tick &#x3D; 10000 ms.
    :type position_ticks: int
    :param audio_stream_index: The audio stream index.
    :type audio_stream_index: int
    :param subtitle_stream_index: The subtitle stream index.
    :type subtitle_stream_index: int
    :param volume_level: Scale of 0-100.
    :type volume_level: int
    :param play_method: The play method.
    :type play_method: dict | bytes
    :param live_stream_id: The live stream id.
    :type live_stream_id: str
    :param play_session_id: The play session id.
    :type play_session_id: str
    :param repeat_mode: The repeat mode.
    :type repeat_mode: dict | bytes
    :param is_paused: Indicates if the player is paused.
    :type is_paused: bool
    :param is_muted: Indicates if the player is muted.
    :type is_muted: bool

    """
    play_method = .from_dict(play_method)
    repeat_mode = .from_dict(repeat_mode)
    return web.Response(status=200)


async def on_playback_start(request: web.Request, user_id, item_id, media_source_id=None, audio_stream_index=None, subtitle_stream_index=None, play_method=None, live_stream_id=None, play_session_id=None, can_seek=None) -> web.Response:
    """Reports that a user has begun playing an item.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param media_source_id: The id of the MediaSource.
    :type media_source_id: str
    :param audio_stream_index: The audio stream index.
    :type audio_stream_index: int
    :param subtitle_stream_index: The subtitle stream index.
    :type subtitle_stream_index: int
    :param play_method: The play method.
    :type play_method: dict | bytes
    :param live_stream_id: The live stream id.
    :type live_stream_id: str
    :param play_session_id: The play session id.
    :type play_session_id: str
    :param can_seek: Indicates if the client can seek.
    :type can_seek: bool

    """
    play_method = .from_dict(play_method)
    return web.Response(status=200)


async def on_playback_stopped(request: web.Request, user_id, item_id, media_source_id=None, next_media_type=None, position_ticks=None, live_stream_id=None, play_session_id=None) -> web.Response:
    """Reports that a user has stopped playing an item.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param item_id: Item id.
    :type item_id: str
    :type item_id: str
    :param media_source_id: The id of the MediaSource.
    :type media_source_id: str
    :param next_media_type: The next media type that will play.
    :type next_media_type: str
    :param position_ticks: Optional. The position, in ticks, where playback stopped. 1 tick &#x3D; 10000 ms.
    :type position_ticks: int
    :param live_stream_id: The live stream id.
    :type live_stream_id: str
    :param play_session_id: The play session id.
    :type play_session_id: str

    """
    return web.Response(status=200)


async def ping_playback_session(request: web.Request, play_session_id=None) -> web.Response:
    """Pings a playback session.

    

    :param play_session_id: Playback session id.
    :type play_session_id: str

    """
    return web.Response(status=200)


async def report_playback_progress(request: web.Request, body=None) -> web.Response:
    """Reports playback progress within a session.

    

    :param body: The playback progress info.
    :type body: dict | bytes

    """
    body = PlaybackProgressInfo.from_dict(body)
    return web.Response(status=200)


async def report_playback_start(request: web.Request, body=None) -> web.Response:
    """Reports playback has started within a session.

    

    :param body: The playback start info.
    :type body: dict | bytes

    """
    body = PlaybackStartInfo.from_dict(body)
    return web.Response(status=200)


async def report_playback_stopped(request: web.Request, body=None) -> web.Response:
    """Reports playback has stopped within a session.

    

    :param body: The playback stop info.
    :type body: dict | bytes

    """
    body = PlaybackStopInfo.from_dict(body)
    return web.Response(status=200)
