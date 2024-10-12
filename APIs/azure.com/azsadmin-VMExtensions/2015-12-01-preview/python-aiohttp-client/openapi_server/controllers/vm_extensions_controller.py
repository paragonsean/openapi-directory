from typing import List, Dict
from aiohttp import web

from openapi_server.models.vm_extension import VMExtension
from openapi_server.models.vm_extension_parameters import VMExtensionParameters
from openapi_server import util


async def v_m_extensions_create(request: web.Request, subscription_id, location, publisher, type, version, api_version, extension) -> web.Response:
    """Create a Virtual Machine Extension Image.

    Create a Virtual Machine Extension Image with publisher, version.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param publisher: Name of the publisher.
    :type publisher: str
    :param type: Type of extension.
    :type type: str
    :param version: The version of the resource.
    :type version: str
    :param api_version: Client API Version.
    :type api_version: str
    :param extension: Virtual Machine Extension Image creation properties.
    :type extension: dict | bytes

    """
    extension = VMExtensionParameters.from_dict(extension)
    return web.Response(status=200)


async def v_m_extensions_delete(request: web.Request, subscription_id, location, publisher, type, version, api_version) -> web.Response:
    """Deletes a Virtual Machine Extension Image.

    Deletes specified Virtual Machine Extension Image.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param publisher: Name of the publisher.
    :type publisher: str
    :param type: Type of extension.
    :type type: str
    :param version: The version of the resource.
    :type version: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def v_m_extensions_get(request: web.Request, subscription_id, location, publisher, type, version, api_version) -> web.Response:
    """Returns requested Virtual Machine Extension Image.

    Returns requested Virtual Machine Extension Image matching publisher, type, version.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param publisher: Name of the publisher.
    :type publisher: str
    :param type: Type of extension.
    :type type: str
    :param version: The version of the resource.
    :type version: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def v_m_extensions_list(request: web.Request, subscription_id, location, api_version) -> web.Response:
    """Returns a list of all Virtual Machine Extension Images.

    List of all Virtual Machine Extension Images for the current location are returned.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param location: Location of the resource.
    :type location: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
