from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.image import Image
from openapi_server.models.image_ids import ImageIds
from openapi_server import util


async def list_management_image_add_image(request: web.Request, list_id, tag=None, label=None) -> web.Response:
    """list_management_image_add_image

    Add an image to the list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param tag: Tag for the image.
    :type tag: int
    :param label: The image label.
    :type label: str

    """
    return web.Response(status=200)


async def list_management_image_delete_all_images(request: web.Request, list_id) -> web.Response:
    """list_management_image_delete_all_images

    Deletes all images from the list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)


async def list_management_image_delete_image(request: web.Request, list_id, image_id) -> web.Response:
    """list_management_image_delete_image

    Deletes an image from the list with list Id and image Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str
    :param image_id: Id of the image.
    :type image_id: str

    """
    return web.Response(status=200)


async def list_management_image_get_all_image_ids(request: web.Request, list_id) -> web.Response:
    """list_management_image_get_all_image_ids

    Gets all image Ids from the list with list Id equal to list Id passed.

    :param list_id: List Id of the image list.
    :type list_id: str

    """
    return web.Response(status=200)
