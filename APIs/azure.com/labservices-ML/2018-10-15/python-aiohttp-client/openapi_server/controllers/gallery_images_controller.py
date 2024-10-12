from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_image import GalleryImage
from openapi_server.models.gallery_image_fragment import GalleryImageFragment
from openapi_server.models.response_with_continuation_gallery_image import ResponseWithContinuationGalleryImage
from openapi_server import util


async def gallery_images_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, gallery_image_name, api_version, gallery_image) -> web.Response:
    """gallery_images_create_or_update

    Create or replace an existing Gallery Image.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param gallery_image_name: The name of the gallery Image.
    :type gallery_image_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param gallery_image: Represents an image from the Azure Marketplace
    :type gallery_image: dict | bytes

    """
    gallery_image = GalleryImage.from_dict(gallery_image)
    return web.Response(status=200)


async def gallery_images_delete(request: web.Request, subscription_id, resource_group_name, lab_account_name, gallery_image_name, api_version) -> web.Response:
    """gallery_images_delete

    Delete gallery image.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param gallery_image_name: The name of the gallery Image.
    :type gallery_image_name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_images_get(request: web.Request, subscription_id, resource_group_name, lab_account_name, gallery_image_name, api_version, expand=None) -> web.Response:
    """gallery_images_get

    Get gallery image

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param gallery_image_name: The name of the gallery Image.
    :type gallery_image_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;author)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def gallery_images_list(request: web.Request, subscription_id, resource_group_name, lab_account_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """gallery_images_list

    List gallery images in a given lab account.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;author)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)


async def gallery_images_update(request: web.Request, subscription_id, resource_group_name, lab_account_name, gallery_image_name, api_version, gallery_image) -> web.Response:
    """gallery_images_update

    Modify properties of gallery images.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_account_name: The name of the lab Account.
    :type lab_account_name: str
    :param gallery_image_name: The name of the gallery Image.
    :type gallery_image_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param gallery_image: Represents an image from the Azure Marketplace
    :type gallery_image: dict | bytes

    """
    gallery_image = GalleryImageFragment.from_dict(gallery_image)
    return web.Response(status=200)
