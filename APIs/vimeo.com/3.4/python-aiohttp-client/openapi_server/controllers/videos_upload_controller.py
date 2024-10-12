from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.upload_attempt import UploadAttempt
from openapi_server.models.upload_video_alt1_request import UploadVideoAlt1Request
from openapi_server.models.video import Video
from openapi_server import util


async def complete_streaming_upload(request: web.Request, upload, user_id, signature, video_file_id) -> web.Response:
    """Complete a user&#39;s streaming upload

    

    :param upload: The ID of the upload attempt.
    :type upload: 
    :param user_id: The ID of the user.
    :type user_id: 
    :param signature: The crypto signature of the completed upload.
    :type signature: str
    :param video_file_id: The ID of the uploaded file.
    :type video_file_id: 

    """
    return web.Response(status=200)


async def get_upload_attempt(request: web.Request, upload, user_id) -> web.Response:
    """Get a user&#39;s upload attempt

    

    :param upload: The ID of the upload attempt.
    :type upload: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def upload_video(request: web.Request, user_id, body) -> web.Response:
    """Upload a video

    Begin the video upload process. For more information, see our [upload documentation](https://developer.vimeo.com/api/upload/videos).

    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = UploadVideoAlt1Request.from_dict(body)
    return web.Response(status=200)


async def upload_video_alt1(request: web.Request, body) -> web.Response:
    """Upload a video

    Begin the video upload process. For more information, see our [upload documentation](https://developer.vimeo.com/api/upload/videos).

    :param body: 
    :type body: dict | bytes

    """
    body = UploadVideoAlt1Request.from_dict(body)
    return web.Response(status=200)
