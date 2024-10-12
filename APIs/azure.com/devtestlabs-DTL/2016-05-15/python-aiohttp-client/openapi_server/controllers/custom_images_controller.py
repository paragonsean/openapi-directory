from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.custom_image import CustomImage
from openapi_server.models.response_with_continuation_custom_image import ResponseWithContinuationCustomImage
from openapi_server import util


async def custom_images_create_or_update(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, custom_image) -> web.Response:
    """custom_images_create_or_update

    Create or replace an existing custom image. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the custom image.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param custom_image: A custom image.
    :type custom_image: dict | bytes

    """
    custom_image = CustomImage.from_dict(custom_image)
    return web.Response(status=200)


async def custom_images_delete(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """custom_images_delete

    Delete custom image. This operation can take a while to complete.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the custom image.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str

    """
    return web.Response(status=200)


async def custom_images_get(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, expand=None) -> web.Response:
    """custom_images_get

    Get custom image.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param name: The name of the custom image.
    :type name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;vm)&#39;
    :type expand: str

    """
    return web.Response(status=200)


async def custom_images_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, expand=None, filter=None, top=None, orderby=None) -> web.Response:
    """custom_images_list

    List custom images in a given lab.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param expand: Specify the $expand query. Example: &#39;properties($select&#x3D;vm)&#39;
    :type expand: str
    :param filter: The filter to apply to the operation.
    :type filter: str
    :param top: The maximum number of resources to return from the operation.
    :type top: int
    :param orderby: The ordering expression for the results, using OData notation.
    :type orderby: str

    """
    return web.Response(status=200)
