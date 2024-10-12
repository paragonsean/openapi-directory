from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.chapter import Chapter
from openapi_server.models.chapters_list_response import ChaptersListResponse
from openapi_server.models.not_found import NotFound
from openapi_server import util


async def d_elete_videos_video_id_chapters_language(request: web.Request, video_id, language) -> web.Response:
    """Delete a chapter

    

    :param video_id: The unique identifier for the video you want to delete a chapter from. 
    :type video_id: str
    :param language: A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    :type language: str

    """
    return web.Response(status=200)


async def g_et_videos_video_id_chapters(request: web.Request, video_id, current_page=None, page_size=None) -> web.Response:
    """List video chapters

    Retrieve a list of all chapters for a specified video.

    :param video_id: The unique identifier for the video you want to retrieve a list of chapters for.
    :type video_id: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_videos_video_id_chapters_language(request: web.Request, video_id, language) -> web.Response:
    """Show a chapter

    Chapters help your viewers find the sections of the video they are most interested in viewing. Tutorials that use the [chapters endpoint](https://api.video/blog/endpoints/chapters).

    :param video_id: The unique identifier for the video you want to show a chapter for.
    :type video_id: str
    :param language: A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    :type language: str

    """
    return web.Response(status=200)


async def p_ost_videos_video_id_chapters_language(request: web.Request, video_id, language, file) -> web.Response:
    """Upload a chapter

    Chapters help break the video into sections. Read our [tutorial](https://api.video/blog/tutorials/adding-chapters-to-your-videos) for more details.

    :param video_id: The unique identifier for the video you want to upload a chapter for.
    :type video_id: str
    :param language: A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    :type language: str
    :param file: The VTT file describing the chapters you want to upload.
    :type file: str

    """
    return web.Response(status=200)
