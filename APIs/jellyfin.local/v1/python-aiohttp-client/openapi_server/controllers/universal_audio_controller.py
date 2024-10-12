from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def get_universal_audio_stream(request: web.Request, item_id, container=None, media_source_id=None, device_id=None, user_id=None, audio_codec=None, max_audio_channels=None, transcoding_audio_channels=None, max_streaming_bitrate=None, audio_bit_rate=None, start_time_ticks=None, transcoding_container=None, transcoding_protocol=None, max_audio_sample_rate=None, max_audio_bit_depth=None, enable_remote_media=None, break_on_non_key_frames=None, enable_redirection=None) -> web.Response:
    """Gets an audio stream.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param container: Optional. The audio container.
    :type container: List[str]
    :param media_source_id: The media version id, if playing an alternate version.
    :type media_source_id: str
    :param device_id: The device id of the client requesting. Used to stop encoding processes when needed.
    :type device_id: str
    :param user_id: Optional. The user id.
    :type user_id: str
    :type user_id: str
    :param audio_codec: Optional. The audio codec to transcode to.
    :type audio_codec: str
    :param max_audio_channels: Optional. The maximum number of audio channels.
    :type max_audio_channels: int
    :param transcoding_audio_channels: Optional. The number of how many audio channels to transcode to.
    :type transcoding_audio_channels: int
    :param max_streaming_bitrate: Optional. The maximum streaming bitrate.
    :type max_streaming_bitrate: int
    :param audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
    :type audio_bit_rate: int
    :param start_time_ticks: Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms.
    :type start_time_ticks: int
    :param transcoding_container: Optional. The container to transcode to.
    :type transcoding_container: str
    :param transcoding_protocol: Optional. The transcoding protocol.
    :type transcoding_protocol: str
    :param max_audio_sample_rate: Optional. The maximum audio sample rate.
    :type max_audio_sample_rate: int
    :param max_audio_bit_depth: Optional. The maximum audio bit depth.
    :type max_audio_bit_depth: int
    :param enable_remote_media: Optional. Whether to enable remote media.
    :type enable_remote_media: bool
    :param break_on_non_key_frames: Optional. Whether to break on non key frames.
    :type break_on_non_key_frames: bool
    :param enable_redirection: Whether to enable redirection. Defaults to true.
    :type enable_redirection: bool

    """
    return web.Response(status=200)


async def head_universal_audio_stream(request: web.Request, item_id, container=None, media_source_id=None, device_id=None, user_id=None, audio_codec=None, max_audio_channels=None, transcoding_audio_channels=None, max_streaming_bitrate=None, audio_bit_rate=None, start_time_ticks=None, transcoding_container=None, transcoding_protocol=None, max_audio_sample_rate=None, max_audio_bit_depth=None, enable_remote_media=None, break_on_non_key_frames=None, enable_redirection=None) -> web.Response:
    """Gets an audio stream.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param container: Optional. The audio container.
    :type container: List[str]
    :param media_source_id: The media version id, if playing an alternate version.
    :type media_source_id: str
    :param device_id: The device id of the client requesting. Used to stop encoding processes when needed.
    :type device_id: str
    :param user_id: Optional. The user id.
    :type user_id: str
    :type user_id: str
    :param audio_codec: Optional. The audio codec to transcode to.
    :type audio_codec: str
    :param max_audio_channels: Optional. The maximum number of audio channels.
    :type max_audio_channels: int
    :param transcoding_audio_channels: Optional. The number of how many audio channels to transcode to.
    :type transcoding_audio_channels: int
    :param max_streaming_bitrate: Optional. The maximum streaming bitrate.
    :type max_streaming_bitrate: int
    :param audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
    :type audio_bit_rate: int
    :param start_time_ticks: Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms.
    :type start_time_ticks: int
    :param transcoding_container: Optional. The container to transcode to.
    :type transcoding_container: str
    :param transcoding_protocol: Optional. The transcoding protocol.
    :type transcoding_protocol: str
    :param max_audio_sample_rate: Optional. The maximum audio sample rate.
    :type max_audio_sample_rate: int
    :param max_audio_bit_depth: Optional. The maximum audio bit depth.
    :type max_audio_bit_depth: int
    :param enable_remote_media: Optional. Whether to enable remote media.
    :type enable_remote_media: bool
    :param break_on_non_key_frames: Optional. Whether to break on non key frames.
    :type break_on_non_key_frames: bool
    :param enable_redirection: Whether to enable redirection. Defaults to true.
    :type enable_redirection: bool

    """
    return web.Response(status=200)
