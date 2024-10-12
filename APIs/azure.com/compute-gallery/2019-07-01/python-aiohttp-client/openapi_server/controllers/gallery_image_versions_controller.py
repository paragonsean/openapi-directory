from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_image_version import GalleryImageVersion
from openapi_server.models.gallery_image_version_list import GalleryImageVersionList
from openapi_server.models.gallery_image_version_update import GalleryImageVersionUpdate
from openapi_server import util


async def gallery_image_versions_create_or_update(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, gallery_image_version_name, api_version, gallery_image_version) -> web.Response:
    """gallery_image_versions_create_or_update

    Create or update a gallery Image Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition in which the Image Version is to be created.
    :type gallery_image_name: str
    :param gallery_image_version_name: The name of the gallery Image Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt;
    :type gallery_image_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param gallery_image_version: Parameters supplied to the create or update gallery Image Version operation.
    :type gallery_image_version: dict | bytes

    """
    gallery_image_version = GalleryImageVersion.from_dict(gallery_image_version)
    return web.Response(status=200)


async def gallery_image_versions_delete(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, gallery_image_version_name, api_version) -> web.Response:
    """gallery_image_versions_delete

    Delete a gallery Image Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition in which the Image Version resides.
    :type gallery_image_name: str
    :param gallery_image_version_name: The name of the gallery Image Version to be deleted.
    :type gallery_image_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_image_versions_get(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, gallery_image_version_name, api_version, expand=None) -> web.Response:
    """gallery_image_versions_get

    Retrieves information about a gallery Image Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition in which the Image Version resides.
    :type gallery_image_name: str
    :param gallery_image_version_name: The name of the gallery Image Version to be retrieved.
    :type gallery_image_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def gallery_image_versions_list_by_gallery_image(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, api_version) -> web.Response:
    """gallery_image_versions_list_by_gallery_image

    List gallery Image Versions in a gallery Image Definition.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
    :type gallery_name: str
    :param gallery_image_name: The name of the Shared Image Gallery Image Definition from which the Image Versions are to be listed.
    :type gallery_image_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_image_versions_update(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_image_name, gallery_image_version_name, api_version, gallery_image_version) -> web.Response:
    """gallery_image_versions_update

    Update a gallery Image Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Image Gallery in which the Image Definition resides.
    :type gallery_name: str
    :param gallery_image_name: The name of the gallery Image Definition in which the Image Version is to be updated.
    :type gallery_image_name: str
    :param gallery_image_version_name: The name of the gallery Image Version to be updated. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt;
    :type gallery_image_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param gallery_image_version: Parameters supplied to the update gallery Image Version operation.
    :type gallery_image_version: dict | bytes

    """
    gallery_image_version = GalleryImageVersionUpdate.from_dict(gallery_image_version)
    return web.Response(status=200)
