from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.file_delete_response import FileDeleteResponse
from openapi_server.models.file_upload_response import FileUploadResponse
from openapi_server.models.image_size_request import ImageSizeRequest
from openapi_server.models.image_upload_response import ImageUploadResponse
from openapi_server.models.only_user_id_request import OnlyUserIDRequest
from openapi_server import util


async def delete_file_0(request: web.Request, type, id, url=None) -> web.Response:
    """Delete file

    Deletes previously uploaded file  Required permissions: - DeleteAttachment 

    :param type: Automatically added
    :type type: str
    :param id: Automatically added
    :type id: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def delete_image_0(request: web.Request, type, id, url=None) -> web.Response:
    """Delete image

    Deletes previously uploaded image  Required permissions: - DeleteAttachment 

    :param type: Automatically added
    :type type: str
    :param id: Automatically added
    :type id: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def upload_file_0(request: web.Request, type, id, file=None, user=None) -> web.Response:
    """Upload file

    Uploads file  Required permissions: - UploadAttachment 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param file: file field
    :type file: str
    :param user: 
    :type user: dict | bytes

    """
    user = OnlyUserIDRequest.from_dict(user)
    return web.Response(status=200)


async def upload_image_0(request: web.Request, type, id, file=None, upload_sizes=None, user=None) -> web.Response:
    """Upload image

    Uploads image  Required permissions: - UploadAttachment 

    :param type: 
    :type type: str
    :param id: 
    :type id: str
    :param file: 
    :type file: str
    :param upload_sizes: field with JSON-encoded array of image size configurations
    :type upload_sizes: list | bytes
    :param user: 
    :type user: dict | bytes

    """
    upload_sizes = [ImageSizeRequest.from_dict(d) for d in upload_sizes]
    user = OnlyUserIDRequest.from_dict(user)
    return web.Response(status=200)
