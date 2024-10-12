from typing import List, Dict
from aiohttp import web

from openapi_server.models.apii_paged_response_global_resources_shared_models_global_image import APIIPagedResponseGlobalResourcesSharedModelsGlobalImage
from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.global_resources_shared_models_global_image import GlobalResourcesSharedModelsGlobalImage
from openapi_server import util


async def global_images_delete_file(request: web.Request, id) -> web.Response:
    """Mark a file as &#39;Removed&#39;. Disables download of the image and hides metadata from GET all method

    No Documentation Found.

    :param id: The GlobalImage&#39;s id.
    :type id: str

    """
    return web.Response(status=200)


async def global_images_get_global_image(request: web.Request, id) -> web.Response:
    """Gets a GlobalImage&#39;s metadata.

    No Documentation Found.

    :param id: The GlobalImage&#39;s id.
    :type id: str

    """
    return web.Response(status=200)


async def global_images_get_global_image_contents(request: web.Request, id, is_full_image=None) -> web.Response:
    """Download the contents of a GlobalImage. The current State of the GlobalImage should be &#39;Available&#39;.

    No Documentation Found.

    :param id: The global image metadata id.
    :type id: str
    :param is_full_image: Indicated whether to download the full image or the thumbnail. Defaults to &#39;true&#39;.
    :type is_full_image: bool

    """
    return web.Response(status=200)


async def global_images_get_global_images(request: web.Request, search=None, category_id=None, publisher=None, include_deleted=None, limit=None, offset=None) -> web.Response:
    """Get a paged response of GlobalImage.

    No Documentation Found.

    :param search: Optional. Searches for matching global images with the matching Category Name, Publisher or Description
    :type search: str
    :param category_id: 
    :type category_id: str
    :param publisher: 
    :type publisher: str
    :param include_deleted: Indicates whether to include GlobalImages marked as removed.
    :type include_deleted: bool
    :param limit: Optional. The page limit. The default page limit is 10.
    :type limit: int
    :param offset: Optional. The page offset. The default page offset is 0.
    :type offset: int

    """
    return web.Response(status=200)


async def global_images_post_global_image(request: web.Request, body, override_publisher_or_date=None) -> web.Response:
    """Create the metadata for a GlobalImage before uploading. The State should be &#39;Created&#39;.

    No Documentation Found.

    :param body: The file&#39;s metadata.
    :type body: dict | bytes
    :param override_publisher_or_date: Whether to set the publisher and date to the provided values.
    :type override_publisher_or_date: bool

    """
    body = GlobalResourcesSharedModelsGlobalImage.from_dict(body)
    return web.Response(status=200)


async def global_images_put_global_image(request: web.Request, id, body, override_publisher_or_date=None) -> web.Response:
    """Update the metadata for an image.

    Update the metadata for an image. Size may not be modified by the client.                   Set status to &#39;Available&#39; to publish an image. Both the image and thumbnail must be uploaded.                  Set status to &#39;Created&#39; to reset an image&#39;s contents and re-upload.                   A file may only be &#39;Removed&#39; by the DELETE method.

    :param id: The GlobalImage&#39;s id.
    :type id: str
    :param body: The GlobalImage&#39;s metadata
    :type body: dict | bytes
    :param override_publisher_or_date: Whether to set the publisher and date to the provided values.
    :type override_publisher_or_date: bool

    """
    body = GlobalResourcesSharedModelsGlobalImage.from_dict(body)
    return web.Response(status=200)


async def global_images_put_global_image_contents(request: web.Request, id, is_full_image=None) -> web.Response:
    """Upload the contents of a GlobalImage. The current State of the File for the GlobalImage should be &#39;Created&#39;.

    Both the image and thumbnail must be uploaded.                  Set isFullImage &#x3D; &#39;True&#39; for Full Image, isFullImage &#x3D; &#39;False&#39; for Thumbnail

    :param id: The global image metadata id.
    :type id: str
    :param is_full_image: Indicated whether this is the full image or the thumbnail. Defaults to &#39;true&#39;.
    :type is_full_image: bool

    """
    return web.Response(status=200)
