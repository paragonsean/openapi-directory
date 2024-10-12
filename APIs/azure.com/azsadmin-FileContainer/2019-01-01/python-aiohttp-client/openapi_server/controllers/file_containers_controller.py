from typing import List, Dict
from aiohttp import web

from openapi_server.models.file_container import FileContainer
from openapi_server.models.file_container_parameters import FileContainerParameters
from openapi_server.models.file_containers_list import FileContainersList
from openapi_server import util


async def file_containers_create(request: web.Request, subscription_id, api_version, file_container_id, file_container_parameters) -> web.Response:
    """file_containers_create

    Creates a new file container.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param file_container_id: The file container identifier.
    :type file_container_id: str
    :param file_container_parameters: The parameters required to create a new file container.
    :type file_container_parameters: dict | bytes

    """
    file_container_parameters = FileContainerParameters.from_dict(file_container_parameters)
    return web.Response(status=200)


async def file_containers_delete(request: web.Request, subscription_id, file_container_id, api_version) -> web.Response:
    """Deletes specified file container.

    Delete an existing file container.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param file_container_id: The file container identifier.
    :type file_container_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def file_containers_get(request: web.Request, subscription_id, file_container_id, api_version) -> web.Response:
    """file_containers_get

    Retrieves the specific file container details.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param file_container_id: The file container identifier.
    :type file_container_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)


async def file_containers_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """file_containers_list

    Returns an array of file containers.

    :param subscription_id: Subscription credentials that uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param api_version: Client API Version.
    :type api_version: str

    """
    return web.Response(status=200)
