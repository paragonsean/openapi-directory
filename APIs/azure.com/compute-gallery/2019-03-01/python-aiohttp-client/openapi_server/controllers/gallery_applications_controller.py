from typing import List, Dict
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.gallery_application import GalleryApplication
from openapi_server.models.gallery_application_list import GalleryApplicationList
from openapi_server import util


async def gallery_applications_create_or_update(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, api_version, gallery_application) -> web.Response:
    """gallery_applications_create_or_update

    Create or update a gallery Application Definition.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery in which the Application Definition is to be created.
    :type gallery_name: str
    :param gallery_application_name: The name of the gallery Application Definition to be created or updated. The allowed characters are alphabets and numbers with dots, dashes, and periods allowed in the middle. The maximum length is 80 characters.
    :type gallery_application_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param gallery_application: Parameters supplied to the create or update gallery Application operation.
    :type gallery_application: dict | bytes

    """
    gallery_application = GalleryApplication.from_dict(gallery_application)
    return web.Response(status=200)


async def gallery_applications_delete(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, api_version) -> web.Response:
    """gallery_applications_delete

    Delete a gallery Application.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery in which the Application Definition is to be deleted.
    :type gallery_name: str
    :param gallery_application_name: The name of the gallery Application Definition to be deleted.
    :type gallery_application_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_applications_get(request: web.Request, subscription_id, resource_group_name, gallery_name, gallery_application_name, api_version) -> web.Response:
    """gallery_applications_get

    Retrieves information about a gallery Application Definition.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery from which the Application Definitions are to be retrieved.
    :type gallery_name: str
    :param gallery_application_name: The name of the gallery Application Definition to be retrieved.
    :type gallery_application_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def gallery_applications_list_by_gallery(request: web.Request, subscription_id, resource_group_name, gallery_name, api_version) -> web.Response:
    """gallery_applications_list_by_gallery

    List gallery Application Definitions in a gallery.

    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param gallery_name: The name of the Shared Application Gallery from which Application Definitions are to be listed.
    :type gallery_name: str
    :param api_version: Client Api Version.
    :type api_version: str

    """
    return web.Response(status=200)
