from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_machine_extension_image import VirtualMachineExtensionImage
from openapi_server import util


async def virtual_machine_extension_images_get(request: web.Request, location, publisher_name, type, version, api_version, subscription_id) -> web.Response:
    """virtual_machine_extension_images_get

    Gets a virtual machine extension image.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: 
    :type publisher_name: str
    :param type: 
    :type type: str
    :param version: 
    :type version: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_extension_images_list_types(request: web.Request, location, publisher_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_extension_images_list_types

    Gets a list of virtual machine extension image types.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: 
    :type publisher_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_extension_images_list_versions(request: web.Request, location, publisher_name, type, api_version, subscription_id, filter=None, top=None, orderby=None) -> web.Response:
    """virtual_machine_extension_images_list_versions

    Gets a list of virtual machine extension image versions.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: 
    :type publisher_name: str
    :param type: 
    :type type: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: The filter to apply on the operation.
    :type filter: str
    :param top: 
    :type top: int
    :param orderby: 
    :type orderby: str

    """
    return web.Response(status=200)
