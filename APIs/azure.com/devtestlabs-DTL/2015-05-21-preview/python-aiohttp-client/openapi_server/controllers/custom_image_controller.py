from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.custom_image import CustomImage
from openapi_server.models.response_with_continuation_custom_image import ResponseWithContinuationCustomImage
from openapi_server import util


async def custom_image_create_or_update_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version, custom_image) -> web.Response:
    """custom_image_create_or_update_resource

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
    :param custom_image: 
    :type custom_image: dict | bytes

    """
    custom_image = CustomImage.from_dict(custom_image)
    return web.Response(status=200)


async def custom_image_delete_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """custom_image_delete_resource

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


async def custom_image_get_resource(request: web.Request, subscription_id, resource_group_name, lab_name, name, api_version) -> web.Response:
    """custom_image_get_resource

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

    """
    return web.Response(status=200)


async def custom_image_list(request: web.Request, subscription_id, resource_group_name, lab_name, api_version, filter=None, top=None, order_by=None) -> web.Response:
    """custom_image_list

    List custom images.

    :param subscription_id: The subscription ID.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param lab_name: The name of the lab.
    :type lab_name: str
    :param api_version: Client API version.
    :type api_version: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param order_by: 
    :type order_by: str

    """
    return web.Response(status=200)
