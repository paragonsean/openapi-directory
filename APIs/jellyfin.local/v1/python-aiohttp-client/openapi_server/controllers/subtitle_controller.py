from typing import List, Dict
from aiohttp import web

from openapi_server.models.font_file import FontFile
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.remote_subtitle_info import RemoteSubtitleInfo
from openapi_server.models.upload_subtitle_dto import UploadSubtitleDto
from openapi_server import util


async def delete_subtitle(request: web.Request, item_id, index) -> web.Response:
    """Deletes an external subtitle file.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param index: The index of the subtitle file.
    :type index: int

    """
    return web.Response(status=200)


async def download_remote_subtitles(request: web.Request, item_id, subtitle_id) -> web.Response:
    """Downloads a remote subtitle.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param subtitle_id: The subtitle id.
    :type subtitle_id: str

    """
    return web.Response(status=200)


async def get_fallback_font(request: web.Request, name) -> web.Response:
    """Gets a fallback font file.

    

    :param name: The name of the fallback font file to get.
    :type name: str

    """
    return web.Response(status=200)


async def get_fallback_font_list(request: web.Request, ) -> web.Response:
    """Gets a list of available fallback font files.

    


    """
    return web.Response(status=200)


async def get_remote_subtitles(request: web.Request, id) -> web.Response:
    """Gets the remote subtitles.

    

    :param id: The item id.
    :type id: str

    """
    return web.Response(status=200)


async def get_subtitle(request: web.Request, item_id, media_source_id, index, format, end_position_ticks=None, copy_timestamps=None, add_vtt_time_map=None, start_position_ticks=None) -> web.Response:
    """Gets subtitles in a specified format.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param media_source_id: The media source id.
    :type media_source_id: str
    :param index: The subtitle stream index.
    :type index: int
    :param format: The format of the returned subtitle.
    :type format: str
    :param end_position_ticks: Optional. The end position of the subtitle in ticks.
    :type end_position_ticks: int
    :param copy_timestamps: Optional. Whether to copy the timestamps.
    :type copy_timestamps: bool
    :param add_vtt_time_map: Optional. Whether to add a VTT time map.
    :type add_vtt_time_map: bool
    :param start_position_ticks: Optional. The start position of the subtitle in ticks.
    :type start_position_ticks: int

    """
    return web.Response(status=200)


async def get_subtitle_playlist(request: web.Request, item_id, index, media_source_id, segment_length) -> web.Response:
    """Gets an HLS subtitle playlist.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param index: The subtitle stream index.
    :type index: int
    :param media_source_id: The media source id.
    :type media_source_id: str
    :param segment_length: The subtitle segment length.
    :type segment_length: int

    """
    return web.Response(status=200)


async def get_subtitle_with_ticks(request: web.Request, item_id, media_source_id, index, start_position_ticks, format, end_position_ticks=None, copy_timestamps=None, add_vtt_time_map=None) -> web.Response:
    """Gets subtitles in a specified format.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param media_source_id: The media source id.
    :type media_source_id: str
    :param index: The subtitle stream index.
    :type index: int
    :param start_position_ticks: Optional. The start position of the subtitle in ticks.
    :type start_position_ticks: int
    :param format: The format of the returned subtitle.
    :type format: str
    :param end_position_ticks: Optional. The end position of the subtitle in ticks.
    :type end_position_ticks: int
    :param copy_timestamps: Optional. Whether to copy the timestamps.
    :type copy_timestamps: bool
    :param add_vtt_time_map: Optional. Whether to add a VTT time map.
    :type add_vtt_time_map: bool

    """
    return web.Response(status=200)


async def search_remote_subtitles(request: web.Request, item_id, language, is_perfect_match=None) -> web.Response:
    """Search remote subtitles.

    

    :param item_id: The item id.
    :type item_id: str
    :type item_id: str
    :param language: The language of the subtitles.
    :type language: str
    :param is_perfect_match: Optional. Only show subtitles which are a perfect match.
    :type is_perfect_match: bool

    """
    return web.Response(status=200)


async def upload_subtitle(request: web.Request, item_id, body) -> web.Response:
    """Upload an external subtitle file.

    

    :param item_id: The item the subtitle belongs to.
    :type item_id: str
    :type item_id: str
    :param body: The request body.
    :type body: dict | bytes

    """
    body = UploadSubtitleDto.from_dict(body)
    return web.Response(status=200)
