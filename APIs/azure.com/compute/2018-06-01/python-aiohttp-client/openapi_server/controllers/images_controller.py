from typing import List, Dict
from aiohttp import web

from openapi_server.models.image import Image
from openapi_server.models.image_list_result import ImageListResult
from openapi_server.models.image_update import ImageUpdate
from openapi_server import util


async def images_create_or_update(request: web.Request, resource_group_name, image_name, api_version, subscription_id, parameters) -> web.Response:
    """images_create_or_update

    Create or update an image.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_name: The name of the image.
    :type image_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Create Image operation.
    :type parameters: dict | bytes

    """
    parameters = Image.from_dict(parameters)
    return web.Response(status=200)


async def images_delete(request: web.Request, resource_group_name, image_name, api_version, subscription_id) -> web.Response:
    """images_delete

    Deletes an Image.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_name: The name of the image.
    :type image_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def images_get(request: web.Request, resource_group_name, image_name, api_version, subscription_id, expand=None) -> web.Response:
    """images_get

    Gets an image.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_name: The name of the image.
    :type image_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def images_list(request: web.Request, api_version, subscription_id) -> web.Response:
    """images_list

    Gets the list of Images in the subscription. Use nextLink property in the response to get the next page of Images. Do this till nextLink is null to fetch all the Images.

    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def images_list_by_resource_group(request: web.Request, resource_group_name, api_version, subscription_id) -> web.Response:
    """images_list_by_resource_group

    Gets the list of images under a resource group.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def images_update(request: web.Request, resource_group_name, image_name, api_version, subscription_id, parameters) -> web.Response:
    """images_update

    Update an image.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param image_name: The name of the image.
    :type image_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Parameters supplied to the Update Image operation.
    :type parameters: dict | bytes

    """
    parameters = ImageUpdate.from_dict(parameters)
    return web.Response(status=200)
