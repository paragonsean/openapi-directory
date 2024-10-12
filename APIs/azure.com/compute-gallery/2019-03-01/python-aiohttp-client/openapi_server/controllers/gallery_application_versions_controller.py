from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_application_version import GalleryApplicationVersion
from openapi_server.models.gallery_application_version_list import GalleryApplicationVersionList
from openapi_server import util


async def gallery_application_versions_create_or_update(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, gallery_application_version_name, api_version, gallery_application_version) -> web.Response:
    """gallery_application_versions_create_or_update

    Create or update a gallery Application Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery in which the Application Definition resides.
    :type gallery_name: str
    :param gallery_application_name: The name of the gallery Application Definition in which the Application Version is to be created.
    :type gallery_application_name: str
    :param gallery_application_version_name: The name of the gallery Application Version to be created. Needs to follow semantic version name pattern: The allowed characters are digit and period. Digits must be within the range of a 32-bit integer. Format: &lt;MajorVersion&gt;.&lt;MinorVersion&gt;.&lt;Patch&gt;
    :type gallery_application_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param gallery_application_version: Parameters supplied to the create or update gallery Application Version operation.
    :type gallery_application_version: dict | bytes

    """
    gallery_application_version = GalleryApplicationVersion.from_dict(gallery_application_version)
    return web.Response(status=200)


async def gallery_application_versions_delete(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, gallery_application_version_name, api_version) -> web.Response:
    """gallery_application_versions_delete

    Delete a gallery Application Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery in which the Application Definition resides.
    :type gallery_name: str
    :param gallery_application_name: The name of the gallery Application Definition in which the Application Version resides.
    :type gallery_application_name: str
    :param gallery_application_version_name: The name of the gallery Application Version to be deleted.
    :type gallery_application_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_application_versions_get(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, gallery_application_version_name, api_version, expand=None) -> web.Response:
    """gallery_application_versions_get

    Retrieves information about a gallery Application Version.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery in which the Application Definition resides.
    :type gallery_name: str
    :param gallery_application_name: The name of the gallery Application Definition in which the Application Version resides.
    :type gallery_application_name: str
    :param gallery_application_version_name: The name of the gallery Application Version to be retrieved.
    :type gallery_application_version_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param expand: The expand expression to apply on the operation.
    :type expand: str

    """
    return web.Response(status=200)


async def gallery_application_versions_list_by_gallery_application(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, api_version) -> web.Response:
    """gallery_application_versions_list_by_gallery_application

    List gallery Application Versions in a gallery Application Definition.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery in which the Application Definition resides.
    :type gallery_name: str
    :param gallery_application_name: The name of the Shared Application Gallery Application Definition from which the Application Versions are to be listed.
    :type gallery_application_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
