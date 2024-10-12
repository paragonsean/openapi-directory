from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request import BadRequest
from openapi_server.models.captions_list_response import CaptionsListResponse
from openapi_server.models.captions_update_payload import CaptionsUpdatePayload
from openapi_server.models.not_found import NotFound
from openapi_server.models.subtitle import Subtitle
from openapi_server import util


async def d_elete_videos_video_id_captions_language(request: web.Request, video_id, language) -> web.Response:
    """Delete a caption

    Delete a caption in a specific language by providing the video ID for the video you want to delete the caption from and the language the caption is in.

    :param video_id: The unique identifier for the video you want to delete a caption from.
    :type video_id: str
    :param language: A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    :type language: str

    """
    return web.Response(status=200)


async def g_et_videos_video_id_captions(request: web.Request, video_id, current_page=None, page_size=None) -> web.Response:
    """List video captions

    Retrieve a list of available captions for the videoId you provide.

    :param video_id: The unique identifier for the video you want to retrieve a list of captions for.
    :type video_id: str
    :param current_page: Choose the number of search results to return per page. Minimum value: 1
    :type current_page: int
    :param page_size: Results per page. Allowed values 1-100, default is 25.
    :type page_size: int

    """
    return web.Response(status=200)


async def g_et_videos_video_id_captions_language(request: web.Request, video_id, language) -> web.Response:
    """Show a caption

    Display a caption for a video in a specific language. If the language is available, the caption is returned. Otherwise, you will get a response indicating the caption was not found. Tutorials that use the [captions endpoint](https://api.video/blog/endpoints/captions).

    :param video_id: The unique identifier for the video you want captions for.
    :type video_id: str
    :param language: A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation
    :type language: str

    """
    return web.Response(status=200)


async def p_atch_videos_video_id_captions_language(request: web.Request, video_id, language, body=None) -> web.Response:
    """Update caption

    To have the captions on automatically, use this PATCH to set default: true.

    :param video_id: The unique identifier for the video you want to have automatic captions for. 
    :type video_id: str
    :param language: A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
    :type language: str
    :param body: 
    :type body: dict | bytes

    """
    body = CaptionsUpdatePayload.from_dict(body)
    return web.Response(status=200)


async def p_ost_videos_video_id_captions_language(request: web.Request, video_id, language, file) -> web.Response:
    """Upload a caption

    Upload a VTT file to add captions to your video.  Read our [captioning tutorial](https://api.video/blog/tutorials/adding-captions) for more details.

    :param video_id: The unique identifier for the video you want to add a caption to.
    :type video_id: str
    :param language: A valid BCP 47 language representation.
    :type language: str
    :param file: The video text track (VTT) you want to upload.
    :type file: str

    """
    return web.Response(status=200)
