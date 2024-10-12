from typing import List, Dict
from aiohttp import web

from openapi_server.models.generic_error import GenericError
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.image_metadata import ImageMetadata
from openapi_server import util


async def image_delete_images_id_delete(request: web.Request, id) -> web.Response:
    """Delete image

    This endpoint allows you to delete images hosted in the LinQR storage.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def image_list_all_images_get(request: web.Request, ) -> web.Response:
    """List all images

    This endpoint allows you to list images hosted in the LinQR storage. If there are no images hosted, an empty array is returned.


    """
    return web.Response(status=200)


async def image_list_images_id_get(request: web.Request, id) -> web.Response:
    """List image

    This endpoint allows you to list single image hosted in the LinQR storage.

    :param id: 
    :type id: str

    """
    return web.Response(status=200)


async def image_upload_images_post(request: web.Request, image) -> web.Response:
    """Upload image

    This endpoint allows you to upload images to LinQR storage. In the response, metadata of the submitted image is sent, including the identifier used by other endpoints from the &#x60;Image management&#x60; group for image identification.

    :param image: Binary file to be uploaded into LinQR storage. Maximum single file size is 1MiB (1,048,576 bytes).
    :type image: str

    """
    return web.Response(status=200)
