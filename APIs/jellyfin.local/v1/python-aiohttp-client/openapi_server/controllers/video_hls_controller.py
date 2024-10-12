from typing import List, Dict
from aiohttp import web

from openapi_server.models.encoding_context import EncodingContext
from openapi_server.models.subtitle_delivery_method import SubtitleDeliveryMethod
from openapi_server import util


async def get_live_hls_stream(request: web.Request, item_id, container=None, static=None, params=None, tag=None, device_profile_id=None, play_session_id=None, segment_container=None, segment_length=None, min_segments=None, media_source_id=None, device_id=None, audio_codec=None, enable_auto_stream_copy=None, allow_video_stream_copy=None, allow_audio_stream_copy=None, break_on_non_key_frames=None, audio_sample_rate=None, max_audio_bit_depth=None, audio_bit_rate=None, audio_channels=None, max_audio_channels=None, profile=None, level=None, framerate=None, max_framerate=None, copy_timestamps=None, start_time_ticks=None, width=None, height=None, video_bit_rate=None, subtitle_stream_index=None, subtitle_method=None, max_ref_frames=None, max_video_bit_depth=None, require_avc=None, de_interlace=None, require_non_anamorphic=None, transcoding_max_audio_channels=None, cpu_core_limit=None, live_stream_id=None, enable_mpegts_m2_ts_mode=None, video_codec=None, subtitle_codec=None, transcode_reasons=None, audio_stream_index=None, video_stream_index=None, context=None, stream_options=None, max_width=None, max_height=None, enable_subtitles_in_manifest=None) -> web.Response:
    """Gets a hls live stream.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param container: The audio container.
    :type container: str
    :param static: Optional. If true, the original file will be streamed statically without any encoding. Use either no url extension or the original file extension. true/false.
    :type static: bool
    :param params: The streaming parameters.
    :type params: str
    :param tag: The tag.
    :type tag: str
    :param device_profile_id: Optional. The dlna device profile id to utilize.
    :type device_profile_id: str
    :param play_session_id: The play session id.
    :type play_session_id: str
    :param segment_container: The segment container.
    :type segment_container: str
    :param segment_length: The segment lenght.
    :type segment_length: int
    :param min_segments: The minimum number of segments.
    :type min_segments: int
    :param media_source_id: The media version id, if playing an alternate version.
    :type media_source_id: str
    :param device_id: The device id of the client requesting. Used to stop encoding processes when needed.
    :type device_id: str
    :param audio_codec: Optional. Specify a audio codec to encode to, e.g. mp3. If omitted the server will auto-select using the url&#39;s extension. Options: aac, mp3, vorbis, wma.
    :type audio_codec: str
    :param enable_auto_stream_copy: Whether or not to allow automatic stream copy if requested values match the original source. Defaults to true.
    :type enable_auto_stream_copy: bool
    :param allow_video_stream_copy: Whether or not to allow copying of the video stream url.
    :type allow_video_stream_copy: bool
    :param allow_audio_stream_copy: Whether or not to allow copying of the audio stream url.
    :type allow_audio_stream_copy: bool
    :param break_on_non_key_frames: Optional. Whether to break on non key frames.
    :type break_on_non_key_frames: bool
    :param audio_sample_rate: Optional. Specify a specific audio sample rate, e.g. 44100.
    :type audio_sample_rate: int
    :param max_audio_bit_depth: Optional. The maximum audio bit depth.
    :type max_audio_bit_depth: int
    :param audio_bit_rate: Optional. Specify an audio bitrate to encode to, e.g. 128000. If omitted this will be left to encoder defaults.
    :type audio_bit_rate: int
    :param audio_channels: Optional. Specify a specific number of audio channels to encode to, e.g. 2.
    :type audio_channels: int
    :param max_audio_channels: Optional. Specify a maximum number of audio channels to encode to, e.g. 2.
    :type max_audio_channels: int
    :param profile: Optional. Specify a specific an encoder profile (varies by encoder), e.g. main, baseline, high.
    :type profile: str
    :param level: Optional. Specify a level for the encoder profile (varies by encoder), e.g. 3, 3.1.
    :type level: str
    :param framerate: Optional. A specific video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
    :type framerate: float
    :param max_framerate: Optional. A specific maximum video framerate to encode to, e.g. 23.976. Generally this should be omitted unless the device has specific requirements.
    :type max_framerate: float
    :param copy_timestamps: Whether or not to copy timestamps when transcoding with an offset. Defaults to false.
    :type copy_timestamps: bool
    :param start_time_ticks: Optional. Specify a starting offset, in ticks. 1 tick &#x3D; 10000 ms.
    :type start_time_ticks: int
    :param width: Optional. The fixed horizontal resolution of the encoded video.
    :type width: int
    :param height: Optional. The fixed vertical resolution of the encoded video.
    :type height: int
    :param video_bit_rate: Optional. Specify a video bitrate to encode to, e.g. 500000. If omitted this will be left to encoder defaults.
    :type video_bit_rate: int
    :param subtitle_stream_index: Optional. The index of the subtitle stream to use. If omitted no subtitles will be used.
    :type subtitle_stream_index: int
    :param subtitle_method: Optional. Specify the subtitle delivery method.
    :type subtitle_method: dict | bytes
    :param max_ref_frames: Optional.
    :type max_ref_frames: int
    :param max_video_bit_depth: Optional. The maximum video bit depth.
    :type max_video_bit_depth: int
    :param require_avc: Optional. Whether to require avc.
    :type require_avc: bool
    :param de_interlace: Optional. Whether to deinterlace the video.
    :type de_interlace: bool
    :param require_non_anamorphic: Optional. Whether to require a non anamorphic stream.
    :type require_non_anamorphic: bool
    :param transcoding_max_audio_channels: Optional. The maximum number of audio channels to transcode.
    :type transcoding_max_audio_channels: int
    :param cpu_core_limit: Optional. The limit of how many cpu cores to use.
    :type cpu_core_limit: int
    :param live_stream_id: The live stream id.
    :type live_stream_id: str
    :param enable_mpegts_m2_ts_mode: Optional. Whether to enable the MpegtsM2Ts mode.
    :type enable_mpegts_m2_ts_mode: bool
    :param video_codec: Optional. Specify a video codec to encode to, e.g. h264. If omitted the server will auto-select using the url&#39;s extension. Options: h265, h264, mpeg4, theora, vpx, wmv.
    :type video_codec: str
    :param subtitle_codec: Optional. Specify a subtitle codec to encode to.
    :type subtitle_codec: str
    :param transcode_reasons: Optional. The transcoding reason.
    :type transcode_reasons: str
    :param audio_stream_index: Optional. The index of the audio stream to use. If omitted the first audio stream will be used.
    :type audio_stream_index: int
    :param video_stream_index: Optional. The index of the video stream to use. If omitted the first video stream will be used.
    :type video_stream_index: int
    :param context: Optional. The MediaBrowser.Model.Dlna.EncodingContext.
    :type context: dict | bytes
    :param stream_options: Optional. The streaming options.
    :type stream_options: Dict[str, str]
    :param max_width: Optional. The max width.
    :type max_width: int
    :param max_height: Optional. The max height.
    :type max_height: int
    :param enable_subtitles_in_manifest: Optional. Whether to enable subtitles in the manifest.
    :type enable_subtitles_in_manifest: bool

    """
    subtitle_method = .from_dict(subtitle_method)
    context = .from_dict(context)
    return web.Response(status=200)
