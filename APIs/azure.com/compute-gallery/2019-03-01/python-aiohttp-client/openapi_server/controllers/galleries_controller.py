from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery import Gallery
from openapi_server.models.gallery_list import GalleryList
from openapi_server import util


async def galleries_create_or_update(request: web.Request, subscription_id, resource_group_name, gallery_name, api_version, gallery) -> web.Response:
    """galleries_create_or_update

    Create or update a Shared Image Gallery.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery. The allowed characters are alphabets and numbers with dots and periods allowed in the middle. The maximum length is 80 characters.
    :type gallery_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param gallery: Parameters supplied to the create or update Shared Image Gallery operation.
    :type gallery: dict | bytes

    """
    gallery = Gallery.from_dict(gallery)
    return web.Response(status=200)


async def galleries_delete(request: web.Request, subscription_id, resource_group_name, gallery_name, api_version) -> web.Response:
    """galleries_delete

    Delete a Shared Image Gallery.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery to be deleted.
    :type gallery_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def galleries_get(request: web.Request, subscription_id, resource_group_name, gallery_name, api_version) -> web.Response:
    """galleries_get

    Retrieves information about a Shared Image Gallery.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery.
    :type gallery_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def galleries_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """galleries_list

    List galleries under a subscription.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def galleries_list_by_resource_group(request: web.Request, subscription_id, resource_group_name, api_version) -> web.Response:
    """galleries_list_by_resource_group

    List galleries under a resource group.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
