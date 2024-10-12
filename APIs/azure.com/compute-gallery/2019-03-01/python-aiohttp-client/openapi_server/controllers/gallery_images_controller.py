from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_image import GalleryImage
from openapi_server.models.gallery_image_list import GalleryImageList
from openapi_server import util


async def gallery_images_create_or_update(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, api_version, gallery_image) -> web.Response:
    """gallery_images_create_or_update

    Create or update a gallery Image Definition.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition is to be created.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
    :type gallery_image_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param gallery_image: Parameters supplied to the create or update gallery image operation.
    :type gallery_image: dict | bytes

    """
    gallery_image = GalleryImage.from_dict(gallery_image)
    return web.Response(status=200)


async def gallery_images_delete(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, api_version) -> web.Response:
    """gallery_images_delete

    Delete a gallery image.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition is to be deleted.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition to be deleted.
    :type gallery_image_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_images_get(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, api_version) -> web.Response:
    """gallery_images_get

    Retrieves information about a gallery Image Definition.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition to be retrieved.
    :type gallery_image_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_images_list_by_gallery(request: web.Request, subscription_id, resource_group_name, gallery_name, api_version) -> web.Response:
    """gallery_images_list_by_gallery

    List gallery Image Definitions in a gallery.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery from which Image Definitions are to be listed.
    :type gallery_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
