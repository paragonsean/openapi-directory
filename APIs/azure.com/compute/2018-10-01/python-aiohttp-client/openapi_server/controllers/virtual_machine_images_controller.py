from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_machine_image import VirtualMachineImage
from openapi_server.models.virtual_machine_image_resource import VirtualMachineImageResource
from openapi_server import util


async def virtual_machine_images_get(request: web.Request, location, publisher_name, offer, skus, version, api_version, subscription_id) -> web.Response:
    """virtual_machine_images_get

    Gets a virtual machine image.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: A valid image publisher.
    :type publisher_name: str
    :param offer: A valid image publisher offer.
    :type offer: str
    :param skus: A valid image SKU.
    :type skus: str
    :param version: A valid image SKU version.
    :type version: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_images_list(request: web.Request, location, publisher_name, offer, skus, api_version, subscription_id, filter=None, top=None, orderby=None) -> web.Response:
    """virtual_machine_images_list

    Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: A valid image publisher.
    :type publisher_name: str
    :param offer: A valid image publisher offer.
    :type offer: str
    :param skus: A valid image SKU.
    :type skus: str
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


async def virtual_machine_images_list_offers(request: web.Request, location, publisher_name, api_version, subscription_id) -> web.Response:
    """virtual_machine_images_list_offers

    Gets a list of virtual machine image offers for the specified location and publisher.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: A valid image publisher.
    :type publisher_name: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_images_list_publishers(request: web.Request, location, api_version, subscription_id) -> web.Response:
    """virtual_machine_images_list_publishers

    Gets a list of virtual machine image publishers for the specified Azure location.

    :param location: The name of a supported Azure region.
    :type location: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def virtual_machine_images_list_skus(request: web.Request, location, publisher_name, offer, api_version, subscription_id) -> web.Response:
    """virtual_machine_images_list_skus

    Gets a list of virtual machine image SKUs for the specified location, publisher, and offer.

    :param location: The name of a supported Azure region.
    :type location: str
    :param publisher_name: A valid image publisher.
    :type publisher_name: str
    :param offer: A valid image publisher offer.
    :type offer: str
    :param api_version: Client Api Version.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)
